from classes.weather import Weather
from classes.cell import Cell
from classes.plant import *

# TODO сделать синглтоном 
class Map:   
    
    def __init__(self, nums, xy, partition, numOfClim) :
        # размеры Карты
        self.sizeX, self.sizeY = xy

        # разбиение. На сколько кусочков будет поделена одна еденица измерения
        self.partition = int(partition)
        if self.partition <= 0 : raise Exception("Неверно задано значение разбиения. class Map")

        # погода. Погода управляет такими состояниями как солнце,влажность, ветер ... её характеристики зависят от климата
        self.weather = Weather(numOfClim)
        
        # количество делений, на которые разбито поле
        x, y = self.sizeX * self.partition, self.sizeY * self.partition

        # массив клеток Карты
        self.cells = []
        for i in range(y) : self.cells.append([Cell() for i in range(x)])

        # объекты, от которых создаются остальные растения этого же типа
        self.typesOfPlant = [PlantSpruce(), PlantMaple()]
        
        # список всех растений, находящихся на карте в настоящий момент
        self.plantsList = []
        self._setPlantsList(nums)

    
    def _findIndexs(self, x, y) :
        if x > self.sizeX or y > self.sizeY : raise Exception("Координаты выходят за границы карты")
        
        j = int((x * self.partition) // 1)
        i = int((y * self.partition) // 1)

        return i, j

    def _setPlantsList(self, nums) :

        from random import uniform

        for indx in range(len(self.typesOfPlant)) :
            n = nums[indx]
            for count in range(n) :

                def xyToCorrect(maxSize) :
                    answr = round(uniform(0, maxSize), 2)
                    answr = max(0.01, answr)
                    answr = min(answr, maxSize - 1)
                    return answr             

                x = xyToCorrect(self.sizeX)
                y = xyToCorrect(self.sizeY)

                newPlant = Plant(x, y, self.typesOfPlant[indx], self.partition)
                
                self.plantsList.append(newPlant)
                
                i, j = self._findIndexs(x, y)
                self.cells[i][j].setPlant(newPlant)

    # Полный цикл необходимых дел для растений
    def oneStep(self) :
        self.weather.newWeather()
        self._toFeed()
        self._toGrow()
        self._toAudit()

    #TODO доделать
    def _toAudit(self) :
        from random import uniform

        dieList = []

        for plant in self.plantsList :

            # Искусственное ограничение, к сожалению
            if len(self.plantsList) <= 500 :

                if plant.readyToBreed() :
                    
                    def xyToCorrect(sizeX, maxSize) :
                        answr = round(uniform(sizeX - 2, sizeX + 2), 2)
                        answr = max(0.01, answr)
                        answr = min(answr, maxSize - 1)
                        return answr             

                    x = xyToCorrect(plant.centerX, self.sizeX)
                    y = xyToCorrect(plant.centerY, self.sizeY)

                    babyPlant = Plant(x, y, plant.plantType, self.partition)

                    self.plantsList.append(babyPlant)
                    
                    i, j = self._findIndexs(x, y)
                    self.cells[i][j].setPlant(babyPlant)

            if plant.haveDie() :
                plant.die()

                iMax, jMax = plant.mask.shape
                iPC, jPC = self._findIndexs(plant.centerX, plant.centerY)

                for i in range(iMax) :
                    for j in range(jMax) :
                        if plant.mask[i][j] == True :
                            #iPC, jPC = self._findIndexs(plant.centerX, plant.centerY)

                            deltaI, deltaJ = plant.iMC - i, plant.jMC - j

                            # TODO На самом деле нельзя редактировать
                            # потому что удалится что-то другое 
                            def __ijRight(ind, maxI) :
                                if ind < 0 : return False
                                elif ind >= maxI : return False
                                return True

                            iCell, jCell = iPC - deltaI, jPC - deltaJ
                            
                            if __ijRight(iCell , len(self.cells)) == False : break
                            if __ijRight(jCell, len(self.cells[0])) == False : break
                                
                            self.cells[iCell][jCell].plantsList.remove(plant)
                            self.cells[iCell][jCell].toFertilize(plant.getHeight())
                
                dieList.append(plant)
        # Удаление растения из карты
        for plant in dieList :
            self.plantsList.remove(plant)

    def _toFeed(self) :

        sun = self.weather.getSun()
        window = self.weather.getWindow()
        moisture = self.weather.getMoisture()

        # количество строк
        for i in range(len(self.cells)) :
            # количество столбцов
            for j in range(len(self.cells[0])) :

                if self.cells[i][j].havePlant() :
                    
                    # Накормить растения солнцем, ветром, влагой
                    self._sunWindMoisture(i, j, sun, window, moisture)
                    
                    # Накормить растения землей
                    self.cells[i][j].groundFeed()

        temperature = self.weather.getTemperature()
        
        # накормить растения температурой
        for plant in self.plantsList :
            plant.tempReaction(temperature)

    # вспомогательная функция, считает сколько достанется еды растениям в клетке
    # подходит для кормления Солнцем, Ветром, Влагой
    def _sunWindMoisture(self, i, j, sun, wind, moisture) :
        # Чтобы покушать солнце : посчитать сколько растеньев вокруге всего n
            # Для каждого расстения на клетке
                # посчитать сколько растеньев вокруге выше данного растения m
                # столько солнца достанется = (n - m) / m    
            
        n = self.__findN(i, j)
        
        for plant in self.cells[i][j].plantsList :
            
            m = self.__findM(i, j, plant.height)
            if m >= n : raise Exception("Дерьевьев выше данного больше или столько же, чем всего деревев")
            k = (n - m) / n
            plant.sunReaction(sun * k)
            plant.windReaction(wind * k)
            plant.moistureReaction(moisture * k)
    
    # Вспомогательная функция: найти n - количество растений в ближайших клетках, находящихся по периметру данной клетки 
    def __findN(self, i, j) :
        n = 0

        iMin, jMin, iMax, jMax = self.__ijMinMax(i, j)

        # Количество строк
        for y in range(iMin, iMax) :
            # Количсевто столбцов
            for x in range(jMin, jMax) :
                n += len(self.cells[y][x].plantsList)
        return n
    # Вспомогательная функция: найти m - кол-во растений в ближайших клетках, находящихся по периметру данной клетки,
    # которые ВЫШЕ данного растения 
    def __findM(self, i, j, height) :
        m = 0

        iMin, jMin, iMax, jMax = self.__ijMinMax(i, j)

        # Количество строк
        for y in range(iMin, iMax) :
            # Количсевто столбцов
            for x in range(jMin, jMax) :
                for plant in self.cells[y][x].plantsList :
                    if plant.height > height : m += 1
                    # Внутри одной клетки растения сортированны по высоте
                    # так что можно перестать перебирать растения, если нашлось <=, дальше будут такиеже или ниже
                    else : break
        return m
    # Вспомогательная функция: найти индексы, в пределах которых находятся те клетки (которые по периметру)
    def __ijMinMax(self, i, j) :
        iMin, jMin = i - 1, j - 1
        if iMin < 0 : iMin = 0
        if jMin < 0 : jMin = 0
        
        iMax, jMax = i + 2, j + 2
        if iMax > len(self.cells) : iMax = len(self.cells)
        if jMax > len(self.cells[0]) : jMax = len(self.cells[0])
        
        return iMin, jMin, iMax, jMax
    
    

    #
    def _toGrow(self) :
        # Сортировать растения по уровнюздоровья, сначала должны расти самые крепенькие
        sorted(self.plantsList, key=lambda plant: plant.getHealth(), reverse = True)

        for plant in self.plantsList :                          

            # TODO увеличить возраст
            plant.changeAge()

            if plant.healthy() :

                # Увеличиваем радиус разростания дерева
                plant.maskRadius += 1
                # Двигаем индексы старата маски( в которые нужно наростить растение)
                plant.iMask -= 1
                plant.jMask -= 1
                # Находим индексы старта в поле клеток ( в которые нужно наростить растение)
                # Находим как разность индексов центра и радиуса 
                iPC, jPC = self._findIndexs(plant.centerX, plant.centerY)
                # Если i,j, выходят за пределы поля, их изменяем
                def __ijRedact( ind, maxI) :
                    if ind < 0 : ind = 0
                    elif ind >= maxI : ind = maxI - 1
                    # Подстраховка
                    if maxI == 0 : ind = 0
                    return ind

                iCellStart = __ijRedact(iPC - plant.maskRadius, len(self.cells))
                jCellStart = __ijRedact(jPC - plant.maskRadius, len(self.cells[0]))
                
                # Находиминдексы, в которых нужно остановиться наращивать растение                
                iCellStop = __ijRedact(iPC + plant.maskRadius + 1, len(self.cells))
                jCellStop = __ijRedact(jPC + plant.maskRadius + 1, len(self.cells[0]))


                for i in range(iCellStart, iCellStop) :
                    for j in range(jCellStart, jCellStop) :
                        # Если растение в этой клетке еще не нарощено, т.е. растение не принадлежит этой клетке
                        #проверить с помощью макси
                        iMask = plant.iMC - (iPC - i)
                        jMask = plant.jMC - (jPC - j)
                        
                        tmpMaxi, tmpMaxj = plant.mask.shape
                        if iMask < 0 or iMask >= int(tmpMaxi) : break
                        if jMask < 0 or jMask >= int(tmpMaxj) : break

                        if plant.mask[iMask][jMask] == False :
                            #Проверить, достаточно ли освещено это место
                            n, m = self.__findN(i, j), self.__findM(i, j, plant.getHeight())
                            if n != 0 : sun = (n - m) / n
                            else : sun = 1 # Случай если клетка совершенно не занята

                            if sun >= plant.plantType.getSun() :
                                # Наростить растение
                                self.cells[i][j].setPlant(plant)
                                plant.mask[iMask][jMask] = True
                                plant.crown += 1

                # Увеличить высоту дерева
                plant.changeHeight()



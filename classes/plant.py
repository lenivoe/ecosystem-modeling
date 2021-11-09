class LiveObjOnMap :

    MAX_HEIGHT = 30 # САМОЕ САМОЕ БОЛЬШОЕ ЗНАЧЕНИЕ, нужно для отрисовки
    #MAX_SIZE = 5 # метров

    def __init__(self, centerX, centerY) :
        self.alive = True
        self.centerX = centerX
        self.centerY = centerY
    
    def die(self) :
        self.alive = False

from classes.plantTypes import *
from numpy import zeros, bool8
from numpy import *

class Plant(LiveObjOnMap) :
    
    def __init__(self, centerX, centerY, plantTypeABC, partition):
        super().__init__(centerX, centerY)
        self.height = 0.01
        self.crown = 1
        self.health = 1
        self.procentOfLife = 0
        self.plantType = plantTypeABC

        self.countOfBreed = 0

        self.partition = partition
        self.MAX_SIZE = self.plantType.MAX_SIZE
        self.MAX_HEIGHT = self.plantType.MAX_HEIGHT

        maxSize = self.MAX_SIZE * partition
        self.mask = zeros((maxSize, maxSize), dtype = bool8)
        self.iMC = maxSize // 2
        self.jMC = maxSize // 2
        self.iMask = maxSize // 2
        self.jMask = maxSize // 2
        self.mask[self.iMask][self.jMask] = True
        self.maskRadius = 0
        self.maskCount = 1

    def sunReaction(self, sun) :
        self.health += self.plantType.sunReaction(sun)
    
    def windReaction(self, wind) :
        self.health += self.plantType.windReaction(wind)

    def tempReaction(self, temperature) :
        self.health += self.plantType.tempReaction(temperature)
    
    def moistureReaction(self, moisture) :
        self.health += self.plantType.moistureReaction(moisture)

    def groundReaction(self, ground, volumeOfPlant) :
        self.health += self.plantType.groundReaction(ground, volumeOfPlant)
    
    def healthy(self) :
        if self.health >= 1 : return True
        return False
    
    def typeOfPlant(self) :
        return self.plantType

    def haveDie(self) :
        if self.health <= 0 : return True
        if self.alive == False : return True
        return False

    def getHeight(self) :
        return self.height

    def getHealth(self) :
        return self.health

    def getVolume(self) :
        return self.height * self.crown

    def getCrown(self) :
        return self.crown

    def getName(self) :
        return self.plantType.name

    def getProcOfLife(self) :
        return self.procentOfLife

    def changeAge(self) :
        # Находим за сколько шагов растение достигнет максимального размера (диаметра)
        # при условии что каждый шаг растет на одну клетку. Одна клетка = 1м / partition
        # делим 100% на количество шагов, полученный результат прибавляем к возрасту 
        steps = self.MAX_SIZE  * self.partition
        self.procentOfLife += 1 / steps
        # Если растение дорослодо своего пика, то оно умирает
        if self.procentOfLife >= 1 : self.die()
        
    def changeHeight(self) :
        # Находим за сколько шагов растение достигнет максимального размера (диаметра)
        # при условии что каждый шаг растет на одну клетку. Одна клетка = 1м / partition
        # делим MAX_Height на количество шагов, полученный результат прибавляем к высоте
        # плюс полученный выше результат умнажаем на остаток от целого числа здоровья
        # и прибавляем к итоговой высоте  
        steps = self.MAX_SIZE  * self.partition
        self.height = self.health + self.MAX_HEIGHT / steps + (self.MAX_HEIGHT / steps) * (self.health % 1)
        # Если растение дорослодо своего пика, то оно умирает
        if self.height >= self.MAX_HEIGHT : self.die()

    def readyToBreed(self) :
        if self.countOfBreed < self.plantType.maxCountOfBreed :
            self.countOfBreed += 1
            #if random.randint(0, 2) == 0 :
            if self.health >= 1 :
                if self.procentOfLife > 0 and self.alive : 
                    self.health = 1
                    return True
        return False

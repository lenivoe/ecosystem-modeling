class Cell :

    def __init__(self) :
        from random import uniform

        self.ground = uniform(0.0, 1)
        # Список растений, сортированный по убыванию высоты
        self.plantsList = []
    
    def setPlant(self, plant) :
        self.plantsList.append(plant)
        # TODO может, можно куда-то перенести сортировку, чтобы не каждый раз при  добавлении сортировать?
        sorted(self.plantsList, key=lambda plant: plant.getHeight(), reverse = True)
    
    def getHeighOfHighestPlant(self) :
        if len(self.plantsList) > 0 :
            return round(self.plantsList[0].getHeight(), 2)
        return None

    def getNameOfHighestPlant(self) :
        if len(self.plantsList) > 0 :
            return self.plantsList[0].getName()
        return "Земля"

    def getAgeOfHighestPlant(self) :
        if len(self.plantsList) > 0 :
            return round(self.plantsList[0].getProcOfLife(), 2)
        return None


    def havePlant(self) :
        return len(self.plantsList) > 0

    # TODO адекватно посчитать как удобрится клетка
    def toFertilize(self, h) :
        self.ground += h / 10

    def groundFeed(self) :
        # Принцип работы как кормление солнцем, ветром, влагой...
        n = len(self.plantsList)
        
        for plant in self.plantsList :
            m = 0
            for p in self.plantsList :
                if p.getVolume() > plant.getVolume() : m += 1
            if m >= n : raise Exception("Деревьев большего объема больше, чем всего деревьев в клетке")
            k = (n - m) / n
            plant.groundReaction(self.ground * k, plant.getCrown())
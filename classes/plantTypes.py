from abc import ABC, abstractmethod
class PlantTypeABC(ABC) :
    
    @abstractmethod
    def __init__(self):
        # Свойства : влажность, солнечность, ветер, температура
        self.name = ...
        self.properties = ...
        self.stamina = ...
        self.age = ...

        self.MAX_SIZE = ...
        self.MAX_HEIGHT = ...

        self.maxCountOfBreed = ...

        """Инициализировать значения"""

    @abstractmethod
    def sunReaction(self, sun) :
        """Реакция на солнце"""

    @abstractmethod
    def windReaction(self, wind) :
        """"""
    
    @abstractmethod
    def tempReaction(self, temperature) :
        """"""

    @abstractmethod
    def moistureReaction(self, moisture) :
        """"""
    
    @abstractmethod
    def groundReaction(self, ground) :
        """"""

    def calculateHealth(self, nameOfProp, p) :
        delta = abs(self.properties[nameOfProp] - p)
        # Сколько максимум может быть процентов
        a = 1 / len(self.properties)
        if delta <= self.stamina :
            # Сколько процентов нужно вычесть из максимума
            b = delta / self.stamina
            # Итог
            return a - a * b
        else :
            if self.stamina < 0.5 :
                b = delta / 1 - self.stamina * 2
            else : b = a
            return - (b * a)

    def calculateHealthGround(self, p, crownOfPlant) :
        delta = abs(self.properties["ground"] - p)
        # Сколько максимум может быть процентов
        a = 1 / (len(self.properties) * crownOfPlant)
        if delta <= self.stamina :
            # Сколько процентов нужно вычесть из максимума
            b = delta / self.stamina
            # Итог
            return a - a * b
        else :
            if self.stamina < 0.5 :
                b = delta / 1 - self.stamina * 2
            else : b = a
            return - (b * a)

# Растение - Ель
class PlantSpruce(PlantTypeABC) :
    # MAX_SIZE = 5
    # MAX_HEIGHT = 30
    def __init__(self) :

        # TODO заменить земельку на замусоренность земельки, мб
        self.name = "Ель"
        
        self.MAX_SIZE = 5
        self.MAX_HEIGHT = 30

        self.maxCountOfBreed = 24

        self.properties = {
        'moisture': 0.8, 
        'sun': 0.6,
        'window': 0.8,
        'temperature': 0.6,
        'ground' : 0.8 }
        
        # Коэффициент стойкости
        self.stamina = 0.1

        # Возраст растения
        self.age = 120

    def sunReaction(self, sun):
        health = super().calculateHealth('sun', sun)
        return health

    def windReaction(self, window) :
        health = super().calculateHealth('window', window)
        return health
    
    def tempReaction(self, temperature) :
        health = super().calculateHealth('temperature', temperature)
        return health
    
    def moistureReaction(self, moisture) :
        health = super().calculateHealth('moisture', moisture)
        return health

    def groundReaction(self, ground, crownOfPlant) :
        health = super().calculateHealthGround(ground, crownOfPlant)
        return health

    def getSun(self) :
        return self.properties['sun']

# Растение - Клён
class PlantMaple(PlantTypeABC) :

    def __init__(self) :

        self.name = "Клён"
        
        self.MAX_SIZE = 5
        self.MAX_HEIGHT = 30

        self.maxCountOfBreed = 30

        self.properties = {
        'moisture': 0.5, 
        'sun': 0.6,
        'window': 0.5,
        'temperature': 0.6,
        'ground' : 0.8 }
        
        # Коэффициент стойкости
        self.stamina = 0.2

        # Возраст растения
        self.age = 120

    def sunReaction(self, sun):
        health = super().calculateHealth('sun', sun)
        return health

    def windReaction(self, window) :
        health = super().calculateHealth('window', window)
        return health
    
    def tempReaction(self, temperature) :
        health = super().calculateHealth('temperature', temperature)
        return health
    
    def moistureReaction(self, moisture) :
        health = super().calculateHealth('moisture', moisture)
        return health

    def groundReaction(self, ground, crownOfPlant) :
        health = super().calculateHealthGround(ground, crownOfPlant)
        return health

    def getSun(self) :
        return self.properties['sun']


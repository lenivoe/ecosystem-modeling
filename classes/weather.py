class Weather :
    namesOfClimates = ("Жаркий солнечный климат", "Влажный теневой климат" )
        
    def __init__(self, numOfClim) :
        self.typesOfClimates = (ClimateHot(), ClimateWet() )

        if len(self.typesOfClimates) != len(Weather.namesOfClimates) :
            raise Exception("Количество климотов и их названий не совпадают!")

        self.climate = self.typesOfClimates[numOfClim]

    def newWeather(self) :
        self.climate.changeWether()
    
    def getSun(self) :
        return self.climate.params["sun"]
    
    def getWindow(self) :
        return self.climate.params["window"]

    def getTemperature(self) :
        return self.climate.params["temperature"]

    def getMoisture(self) :
        return self.climate.params["moisture"]
    
    def getNamesOfClimates() :
        return Weather.namesOfClimates
    
    
from abc import ABC, abstractmethod
class ClimateABC(ABC) :
    
    @abstractmethod
    def __init__(self):
        ...
    
    @abstractmethod
    def changeWether(self) :
        ...

class ClimateHot(ClimateABC) :
#
# TODO: разобраться с единицами измерения
#
    def __init__(self) :

        self.params = dict()
        self.changeWether()
        
    def changeWether(self):
        from random import uniform
        # сухой
        self.params["moisture"] = round(uniform(0.5, 1), 3)
        # солнечный
        self.params["sun"] = round(uniform(0.8, 1), 3)
        # ветренный
        self.params["window"] = round(uniform(0.0, 1), 3)
        # жаркий
        self.params["temperature"] = round(uniform(0.7, 1), 3)

        # TODO он вернет значения погоды вообще?
        return self.params.values()

class ClimateWet(ClimateABC) :
#
# TODO: разобраться с единицами измерения
#
    def __init__(self) :

        self.params = dict()
        self.changeWether()
        
    def changeWether(self):
        from random import uniform
        # сухой
        self.params["moisture"] = round(uniform(0.7, 1), 3)
        # солнечный
        self.params["sun"] = round(uniform(0.4, 0.7), 3)
        # ветренный
        self.params["window"] = round(uniform(0.7, 0.9), 3)
        # жаркий
        self.params["temperature"] = round(uniform(0.5, 0.7), 3)

        # TODO он вернет значения погоды вообще?
        return self.params.values()

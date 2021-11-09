from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from initDialogUi import Ui_Dialog
 
class InitDialog(QDialog):
    def __init__(self, mainForm) :
        super(QDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.mainForm = mainForm
        
        self.spinBoxes = [
            self.ui.spinBox_1,
            self.ui.spinBox_2,
            self.ui.spinBox_3,
            self.ui.spinBox_4 ]
        
        from classes.weather import Weather

        comboBoxItems = Weather.getNamesOfClimates()
        for item in comboBoxItems :
            self.ui.comboBox_Climates.addItem(str(item))        
   
    # Метод собирает информацию из Spinboxs о том, сколько каких растений нужно высадить
    def getSpinBoxInf(self) :
        nums = []
        for spinBox in self.spinBoxes :
            nums.append(spinBox.value())
        
        return nums

    def getXY(self) :
        x = self.ui.spinBoxX.value()
        y = self.ui.spinBoxY.value()

        return (x,y)

    def getPartition(self) :
        return self.ui.spinBox_Partition.value()

    def getNumOfClim(self) :
        return self.ui.comboBox_Climates.currentIndex()

        

from PyQt5.QtWidgets import *
from mainFormUi import Ui_mainForm
from initDialog import InitDialog
from PyQt5.QtCore import QTimer

from classes.map import *
from classes.ofForm.cellWidget import *
 
class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.ui = Ui_mainForm()
        self.ui.setupUi(self)

        self.setWindowTitle("Растительное сообщество")

        self.map = None
        
        self.timer = QTimer(self)
        # Соединение сигнала timeout() со слотом updateTime()
        self.timer.timeout.connect(self.__nextDay)
        self.timer.setInterval(1000)
        # Интервалы с которыми может срабатывать таймер.
        # Первый - самая низкая скорость 
        self._timeIntervals = [2000, 1500, 1000, 750, 500]
        self._time_NORM_INTERVAL = 1000

        # Поле
        self.grid = self.ui.gridLayout_Map

        self.initDialog = InitDialog(self)
        self.initDialog.setWindowTitle("Новая симуляция")

        # Кнопка "начать новую симуляцию"
        self.ui.initButton.clicked.connect(self._showInitDialog)

        # Кнопка "Пауза". Соединение сигнала и слота
        self.ui.pushButton_Pause.clicked.connect(self._timePause)

        # Кнопка "Быстрее". Соединение сигнала и слота
        self.ui.pushButton_Faster.clicked.connect(self._timeFaster)

        # Кнопка "Медленнее". Соединение сигнала и слота
        self.ui.pushButton_Slower.clicked.connect(self._timeSlower)

    def __nextDay(self):

        self.map.oneStep()

        self._redrawMap()

        self._changeInformation()

        if len(self.map.plantsList) == 0 :
            self.timer.stop()
        

    # Реакция на нажатие кнопки Пауза    
    def _timePause(self) :
        if self.timer.isActive() :
            self.timer.stop()
            self.ui.pushButton_Pause.setText("|>")

            self.ui.pushButton_Faster.setText(">")
            self.ui.pushButton_Slower.setText("<")
        else:
            self.timer.setInterval(self._time_NORM_INTERVAL)
            self.timer.start()
            self.ui.pushButton_Pause.setText("||")

    # Реакция на нажатие кнопки Быстрее
    def _timeFaster(self) :
        # Если таймер идет
        if self.timer.isActive() :
            i = self._timeIntervals.index(self.timer.interval())
            # Если скорость можно увеличить, то индекс интервала 
            # будет меньше максимального индекса
            if i < len(self._timeIntervals) - 1 :
                self.timer.setInterval(self._timeIntervals[i + 1])
                # Изменить подписи кнопок перемотки
                str = self.ui.pushButton_Faster.text()
                str += '>'
                self.ui.pushButton_Faster.setText(str)

                self.ui.pushButton_Slower.setText('<')
        else :
            #Если Таймер на паузе, эмитируем нажатие кнопки "Пауза"
            self._timePause()

    # Реакция на нажатие кнопки
    def _timeSlower(self) :
        # Если таймер идет
        if self.timer.isActive() :
            i = self._timeIntervals.index(self.timer.interval())
            # Если скорость можно уменьшить, то индекс интервала 
            # будет больше 0 
            if i  > 0 :
                self.timer.setInterval(self._timeIntervals[i - 1])
                # Изменить подписи кнопок перемотки
                str = self.ui.pushButton_Slower.text()
                str += '<'
                self.ui.pushButton_Slower.setText(str)

                self.ui.pushButton_Faster.setText('>')
        else :
            #Если Таймер на паузе, эмитируем нажатие кнопки "Пауза"
            self._timePause()
        
    def _showInitDialog(self) :
        self.timer.stop()

        # Если пользователь подтвердил, что хочет создать карту
        if self.initDialog.exec() == 1 :

            # Включить кнопки управления скоростью симуляции
            self.ui.pushButton_Slower.setEnabled(True)
            self.ui.pushButton_Pause.setEnabled(True)
            self.ui.pushButton_Faster.setEnabled(True)

            # Считать данные из формы
            nums = self.initDialog.getSpinBoxInf()
            self.xy = self.initDialog.getXY()
            self.partition = self.initDialog.getPartition()
            self.numOfClim = int(self.initDialog.getNumOfClim())

            # Создать интеллектуальную модель карты
            self.map = Map(nums, self.xy, self.partition, self.numOfClim)

            # Отрисовать карту
            self._drawMap()
            self._changeInformation()
        
        if self.map is not None :
            self.timer.start()

    def _redrawMap(self) :
        try :

            for i in range(len(self.map.cells)) :

                for j in range(len(self.map.cells[0])) :
                
                    w = self.grid.itemAtPosition(i, j).widget()
                
                    h = self.map.cells[i][j].getHeighOfHighestPlant()
                    w.checkColor(h)
                
                    msg = self.map.cells[i][j].getNameOfHighestPlant()
                    if h is not None : msg += '\n' + 'Высота: '+ str(h)
                    
                    age = self.map.cells[i][j].getAgeOfHighestPlant()
                    if age is not None : msg += '\n' + 'Процент жизни: '+ str(age)
                
                    w.setToolTip(msg)
        except Exception as e :
            print(e, i, j)



    def _drawMap(self) :
        #Сначала очистить карту, если она уже была создана ранее
        if self.grid.isEmpty() is False :
            for i in range(self.grid.rowCount()) :
                for j in range(self.grid.columnCount()) :
                    w = self.grid.itemAtPosition(i, j).widget()
                    self.grid.removeWidget(w)
                    w.setParent(None)
                    
        self.grid.setSpacing(1)
        self.grid.setSizeConstraint(QLayout.SetFixedSize)

        xSize, ySize = self.xy
        xSize *= self.partition
        ySize *= self.partition

        for i in range(ySize) :
            for j in range(xSize) :
                h = self.map.cells[i][j].getHeighOfHighestPlant()
                w = CellWidget(j, i, self.partition, h)

                self.grid.addWidget(w, i, j)

    def _changeInformation(self) :
        msg = str(len(self.map.plantsList))
        self.ui.label_CountOfPlants.setText(msg)
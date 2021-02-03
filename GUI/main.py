import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_Dialog

#ser = 0


app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#Просиходит поиск портов и вывод их в comboBox.
ports = serial.tools.list_ports.comports()
for port in ports:
    print('Нашли порт '+ port.device)
    ui.comboBox.addItem(port.device)


def on_click(self):
    try:
        prnt("clic \n")
        comboText = ui.comboBox.currentText() # ComboBox (comboText) - порты.
        baudrate = ui.comboBox_2.currentText() # ComboBox_2 (baudrate) - скорость передачи данных.
        ser = serial.Serial(comboText, baudrate)
        if ser.is_open():
            prnt("Порт открыт.")
        else:
            prnt("Порт закрыт.")

        prnt("Подключаемся...")

        text = ui.lineEdit.text()
        prnt(text)
        ser.write(text.encode('utf-8'))  # поставить переменную (text), что-бы считывались команды введённые пользователем.
        response = ser.readline()
        prnt(response)

    except:
        prnt("Error...")

ui.pushButton.clicked.connect( on_click )

def prnt(s):
    ui.textEdit.insertPlainText(s)


#def request():
    #try:
    #    text = ui.lineEdit.text()
    #   print(text)
    #    ser.write(text.encode('utf-8'))  # поставить переменную (text), что-бы считывались команды введённые пользователем.
    #    response = ser.readline()
    #    print(response)
    #except:
    #    print("Press F to pay respect")

#ui.pushButton_2.clicked.connect( request )

app.exec()

import sys
import serial
import pdb
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from ConApi import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#Просиходит поиск портов и вывод их в comboBox.
def Search():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        prnt('Нашли порт '+ port.device + "\n")
        ui.comboBox.addItem(port.device)

ui.pushButton.clicked.connect( Search )

# Функция для занесения данных в textEdit
def prnt(s):
    ui.textEdit.insertPlainText(s)

def on_click():
    try:
        comboText = ui.comboBox.currentText() # ComboBox (comboText) - порты.
        baudrate = ui.comboBox_2.currentText() # ComboBox_2 (baudrate) - скорость передачи данных.
        global ser
        ser = serial.Serial(comboText, baudrate)
        if ser.isOpen():
            prnt("\nПодключаемся...\n")
    except:
        prnt("\nError \n")

ui.pushButton_2.clicked.connect( on_click )

# Отправка запроса преобразователю
def request():
    try:
        text = ui.lineEdit.text()
        ser.write("-> ".encode() + text.encode() + " \n".encode())  # Переменная (text), что-бы считывались команды введённые пользователем.
        response = ser.readline()
        prnt(str(response)+ "\n")
    except:
        prnt("Press F to pay respect")

ui.pushButton_3.clicked.connect( request )

app.exec()

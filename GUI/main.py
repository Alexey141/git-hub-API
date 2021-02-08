import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_Dialog

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

def on_click(self):
    try:
        comboText = ui.comboBox.currentText() # ComboBox (comboText) - порты.
        baudrate = ui.comboBox_2.currentText() # ComboBox_2 (baudrate) - скорость передачи данных.
        ser = serial.Serial(comboText, baudrate)
        if ser.isOpen():
            prnt("\nПодключаемся...\n")

        text = ui.lineEdit.text()
        prnt(text)
        ser.write("hello \n \r".encode('utf-8'))  # Переменная (text), что-бы считывались команды введённые пользователем.
        response = ser.readline()
        prnt(str(response))
    except:
        prnt("\nError \n")

ui.pushButton_2.clicked.connect( on_click )

# Функция для занесения данных в textEdit
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

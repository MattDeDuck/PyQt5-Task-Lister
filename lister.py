import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 400, 210)
        self.setWindowTitle("Simple Task Lister")
        self.initUI()

    # Items to be drawn to the window
    def initUI(self):
        # Entry field
        self.e1 = QtWidgets.QLineEdit(self)
        self.e1.setGeometry(220, 10, 170, 30)

        # Listbox
        self.l1 = QtWidgets.QListWidget(self)
        self.l1.setGeometry(10, 10, 200, 150)
        # Grab items from the list
        for i in items:
            self.l1.addItem(i)
        self.l1.clicked.connect(self.clicked)

        # Add task button
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(250, 50)
        self.b2.setText("Add Task")
        self.b2.clicked.connect(self.add)

        # Delete button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setEnabled(False)
        self.b1.move(250, 90)
        self.b1.setText("Delete Item")
        self.b1.clicked.connect(self.deletion)

        # Disabled text box
        self.e2 = QtWidgets.QLineEdit(self)
        self.e2.setDisabled(True)
        self.e2.setGeometry(10, 170, 380, 30)

    def clicked(self):
        # item = self.l1.currentItem()
        self.b1.setDisabled(False)
        # print(item.text())

    def deletion(self):
        item = self.l1.currentItem()
        items.remove(item.text())
        self.l1.takeItem(self.l1.currentRow())
        self.b1.setEnabled(False)
        print(items)

    def add(self):
        itext = self.e1.text().strip()
        if itext:
            print(itext)
            items.append(itext)
            self.l1.addItem(itext)
            self.e1.clear()
            self.b1.setEnabled(False)
        else:
            self.e2.setText("Please enter a task to add!")
            self.b1.setEnabled(False)

    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)

        with open('data.txt', 'w') as listf:
            sep = ","
            litems = sep.join(items)
            listf.write(litems)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


# Define the list of tasks
items = []

# Check if the data file exists
itemfile = os.path.isfile('data.txt')

if itemfile:
    # The file is there...proceed
    with open('data.txt', 'r') as g:
        # Grab the contents of the file
        contents = g.read()
        if contents:
            items = contents.split(",")
            # Debug
            print("On startup: " + str(contents))
else:
    # File isn't there
    with open('data.txt', 'w'):
        pass

# Run the window
window()

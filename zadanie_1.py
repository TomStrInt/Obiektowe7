import sys
import json
from PySide6 import QtCore, QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prosty Edytor Grafiki Wektorowej")

        # obszar roboczy
        self.scene = QtWidgets.QGraphicsScene(self)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # tworzenie akcji i paska narzędzi
        self._createActions()
        self._createToolbar()

    def _createActions(self):
        # dodawanie ksztaltow

        self.actionAddRect = QtGui.QAction("Dodaj Prostokąt", self)
        self.actionAddRect.triggered.connect(self.addRect)

        self.actionAddEllipse = QtGui.QAction("Dodaj Elipsę", self)
        self.actionAddEllipse.triggered.connect(self.addEllipse)

        self.actionAddTriangle = QtGui.QAction("Dodaj Trójkąt", self)
        self.actionAddTriangle.triggered.connect(self.addTriangle)

        # zmiana kolejności
        self.actionBringForward = QtGui.QAction("Do przodu", self)
        self.actionBringForward.triggered.connect(self.bringForward)


        self.actionSendBackward = QtGui.QAction("Do tyłu", self)
        self.actionSendBackward.triggered.connect(self.sendBackward)



        # usuwanie kształtu
        self.actionDelete = QtGui.QAction("Usuń", self)
        self.actionDelete.triggered.connect(self.deleteItem)


        # eksport do PNG i zapis wektorowy
        self.actionExportPNG = QtGui.QAction("Zapisz jako PNG", self)
        self.actionExportPNG.triggered.connect(self.exportPNG)
        self.actionSaveVector = QtGui.QAction("Zapisz wektorowo", self)
        self.actionSaveVector.triggered.connect(self.saveVector)

    def _createToolbar(self):
        toolbar = self.addToolBar("Narzędzia")
        toolbar.addAction(self.actionAddRect)
        toolbar.addAction(self.actionAddEllipse)
        toolbar.addAction(self.actionAddTriangle)
        toolbar.addSeparator()
        toolbar.addAction(self.actionBringForward)
        toolbar.addAction(self.actionSendBackward)
        toolbar.addAction(self.actionDelete)
        toolbar.addSeparator()
        toolbar.addAction(self.actionExportPNG)
        toolbar.addAction(self.actionSaveVector)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

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




    def addRect(self):     #dodaje prostokat
        rect = QtCore.QRectF(0, 0, 100, 50)
        item = QtWidgets.QGraphicsRectItem(rect)
        item.setBrush(QtGui.QBrush(QtGui.QColor("lightblue")))
        item.setPen(QtGui.QPen(QtGui.QColor("black"), 2))
        item.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable | QtWidgets.QGraphicsItem.ItemIsMovable)
        item.setPos(50, 50)
        self.scene.addItem(item)



    def addEllipse(self): #dodawanie elipsy
        rect = QtCore.QRectF(0, 0, 100, 50)
        item = QtWidgets.QGraphicsEllipseItem(rect)
        item.setBrush(QtGui.QBrush(QtGui.QColor("lightgreen")))
        item.setPen(QtGui.QPen(QtGui.QColor("black"), 2))
        item.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable | QtWidgets.QGraphicsItem.ItemIsMovable)
        item.setPos(150, 50)
        self.scene.addItem(item)

    def addTriangle(self):   #trójkąt 
        polygon = QtGui.QPolygonF([
            QtCore.QPointF(0, 0),
            QtCore.QPointF(100, 0),
            QtCore.QPointF(50, 80)
        ])
        item = QtWidgets.QGraphicsPolygonItem(polygon)
        item.setBrush(QtGui.QBrush(QtGui.QColor("lightyellow")))
        item.setPen(QtGui.QPen(QtGui.QColor("black"), 2))
        item.setFlags(QtWidgets.QGraphicsItem.ItemIsSelectable | QtWidgets.QGraphicsItem.ItemIsMovable)
        item.setPos(250, 50)
        self.scene.addItem(item)

    def bringForward(self):  #przesun na wierzch
        for item in self.scene.selectedItems():
            current_z = item.zValue()
            item.setZValue(current_z + 1)

    def sendBackward(self):  #przesun na spod
        for item in self.scene.selectedItems():
            current_z = item.zValue()
            item.setZValue(current_z - 1)

    def deleteItem(self):
        for item in self.scene.selectedItems():
            self.scene.removeItem(item)

    def exportPNG(self):
        rect = self.scene.itemsBoundingRect()
        if rect.isNull():
            return  


        # Tworzenie obrazu z przezroczystym tłem
        img = QtGui.QImage(rect.size().toSize(), QtGui.QImage.Format_ARGB32)
        img.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(img)
        self.scene.render(painter, QtCore.QRectF(img.rect()), rect)
        painter.end()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Zapisz jako PNG", "", "PNG Files (*.png)")
        if filename:
            img.save(filename)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

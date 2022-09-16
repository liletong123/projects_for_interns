from socket import if_nameindex
import sys
import os
from pathlib import Path
from os import path,walk
from PySide6.QtWidgets import QHBoxLayout,QApplication,QPushButton,QWidget,QSpacerItem,QSizePolicy,QVBoxLayout,QGraphicsScene, QGraphicsView,QMessageBox,QFileDialog, QMainWindow,  QGraphicsPixmapItem
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap,QImage
# from PySide6.QtCore import QPixmap

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        widget = QWidget()
        self.layout = QHBoxLayout()
        self.btn_select = QPushButton("打开文件")
        self.layout.addWidget(self.btn_select)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.btn_select.clicked.connect(self.on_file_select)
    
    def on_file_select(self):
        files,flietype = QFileDialog.getOpenFileNames(self.btn_select,'All Files(*);TeXt Files(*.jepg)')
        for pixpath in files:
            view = QGraphicsView()
            scene = QGraphicsScene()
            pixmap = QPixmap(str(pixpath))
            item = QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            view.setScene(scene)
            self.layout.addWidget(view)



if __name__ == "__main__":
    app = QApplication()
    window = MyMainWindow()
    window.show()
    app.exec()

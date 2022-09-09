import sys
import os
from pathlib import Path
from os import path,walk
from PySide6.QtWidgets import QFileDialog,QApplication,QGraphicsPixmapItem,QHBoxLayout,QLabel
from PyQt5.QtCore import QRect, QRectF, QSize, Qt
from PySide6.QtGui import QPainter, QPixmap, QWheelEvent
from vmd import ExtplotCheck
# from scene import ImageViewer
class Rename():
    def __init__(self):
        super().__init__()
        self.vmd = ExtplotCheck()
        self.vmd.btn1.clicked.connect(self.btn1click)
      
       

    def _set_local_image_dir(self, image_dir: Path) -> None:
        images = [
            path.join(root, name)
            for root, _, files in walk(image_dir)
            for name in files
        ]
        return images
    def btn1click(self):
        self.img_path: Path = QFileDialog.getExistingDirectory(self.vmd, "local image dir selection")
        
        self.img = self._set_local_image_dir(self.img_path)
    
    def con(self):
        path = path.replace(".xml",".jepg")
        # self.pixmap = QPixmap('/home/user/桌面/脚本/convert/h1/img_1/50.jpeg')
        # self.pixmapItem = QGraphicsPixmapItem(self.pixmap)
        # self.displayedImageSize = QSize(0, 0)
        # pixmap = QPixmap("/home/user/桌面/llt/h3/h2/img/50.jpeg").scaled(self.label.size(), aspectMode=Qt.KeepAspectRatio)
        # self.label.setPixmap(pixmap)
        # self.label.repaint()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    na = Rename()
    na.vmd.show()
    # sen = ImageViewer()
    # sen.show()
    app.exec()
    
# 读取xml文件，通过该文件的坐标切割原图，切割原图之后，把图片五成n列显示在界面上
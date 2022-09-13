from socket import if_nameindex
import sys
import os
from pathlib import Path
from os import path,walk

from PySide6.QtWidgets import QHBoxLayout,QApplication,QPushButton,QWidget,QSpacerItem,QSizePolicy,QVBoxLayout,QGraphicsScene, QGraphicsView,QMessageBox,QFileDialog, QMainWindow,  QGraphicsPixmapItem
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap



class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        widget = QWidget()
        layout = QHBoxLayout()
        self.btn_select = QPushButton("打开文件")
        self.view = QGraphicsView()
        layout.addWidget(self.view)
        layout.addWidget(self.btn_select)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.btn_select.clicked.connect(self.on_file_select)
        
    def on_file_select(self):
       
        files = QFileDialog.getOpenFileName(self.btn_select,'open file','./')
        file = files[0]
        pixmap = QPixmap.fromFile(file)
        item = QGraphicsPixmapItem(pixmap, scene)
        # read files and get images
        scene = QGraphicsScene

        self.view.setScene(scene)





class ExtplotCheck(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.wlayout = QtWidgets.QVBoxLayout()
        self.layout = QHBoxLayout()
        self.btn_widget = QWidget()
        self.qw_widget = QWidget()
        self.btn_widget.setLayout(self.layout)
        # self.zoomInTimes = 0
        # self.maxZoomInTimes = 22
        # self.graphicsScene = QGraphicsScene()
        # self.lable = QLabel()
        # pixmap = QPixmap("/home/user/桌面/llt/h3/h2/img/50.jpeg") 
        
        # self.wlayout.addWidget(self.lable)


        # self.wlayout.addWidget(self.lable)
        # self.setLayout(self.wlayout)

        self.topFiller = QWidget()
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
       
        # self.layout.addWidget(self.btn2)
        self.resize(1000,600)

        # self.wlayout.addWidget(self.view)
        # self.setLayout(self.wlayout)

        # self.topFiller.setMinimumSize(250,5000) # 滚动条尺寸
        # self.scroll = QScrollArea() # 创建滚动条
        # self.scroll.setWidget(self.topFiller)
 
        # self.wlayout = QVBoxLayout()
        # self.wlayout.addWidget(self.scroll)
        
        
    
        
        self.setLayout(self.wlayout)
        self.sence = QGraphicsScene()
        self.view = QGraphicsView()

        self.btn1 = QPushButton(self.btn_widget)
        self.btn1.setText("打开文件")
        
        self.btn2 = QPushButton(self.btn_widget)
        self.btn2.setText("保存")
        self.horizontalSpacer = QSpacerItem(
            100,50, QSizePolicy.Expanding, QSizePolicy.Maximum
        )
        self.layout.addItem(self.horizontalSpacer)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.setLayout(self.layout)

        self.wlayout.addWidget(self.btn_widget)
        self.wlayout.addWidget(self.qw_widget)
        self.setLayout(self.wlayout)


        self.view.setScene(self.sence)
        self.wlayout.addWidget(self.view)
        self.setLayout(self.wlayout)
    #     FileDialog = QFileDialog(self.btn1)
    #     FileDialog.setFileMode(QFileDialog.AnyFile)
    #     filter = "(*.jepg,*.xml)|*.jepg,*.xml|All files(*.*)|*.*"
    #     image_file,_ = FileDialog.getOpenFileName(self.btn1,'open file','./','Image file(*.jepg,*.xml)')
    #    # 判断是否打开文件
    #     if not image_file:
    #        QMessageBox.warning(self.btn1,"警告","文件错误或打开文件夹!",QMessageBox.Yes)
    #        return
    #     print("读入文件成功") 
    #     print(image_file)   
    #     self.label.setPixmap(image_file)
    #     self.label.setScaledContents(True)   
        # self.sence.addPixmap(pixmap)
      
        
       

       
if __name__ == "__main__":
    app = QApplication()
    window = MyMainWindow()
    window.show()

    app.exec()

       
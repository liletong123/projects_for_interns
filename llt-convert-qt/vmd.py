import sys
import os
from PySide6.QtWidgets import QHBoxLayout,QApplication,QPushButton,QWidget,QSpacerItem,QSizePolicy,QVBoxLayout,QGraphicsScene,QGraphicsView
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap


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
        pixmap = QPixmap("/home/user/桌面/llt/h3/h2/img/50.jpeg") 
        
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
        self.view.setScene(self.sence)
        self.wlayout.addWidget(self.view)
        self.setLayout(self.wlayout)
        self.sence.addPixmap(pixmap)
      
        
       

       


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

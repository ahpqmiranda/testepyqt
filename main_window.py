# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 798)
        self.background_frame = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_frame.sizePolicy().hasHeightForWidth())
        self.background_frame.setSizePolicy(sizePolicy)
        self.background_frame.setObjectName("background_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.background_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.background_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.Apreview = QtWidgets.QWidget()
        self.Apreview.setObjectName("Apreview")
        self.tabWidget.addTab(self.Apreview, "")
        self.Ainsert = QtWidgets.QWidget()
        self.Ainsert.setObjectName("Ainsert")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Ainsert)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.title_label = QtWidgets.QLabel(self.Ainsert)
        self.title_label.setObjectName("title_label")
        self.gridLayout_4.addWidget(self.title_label, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.Ainsert)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 202))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tag_label = QtWidgets.QLabel(self.frame_2)
        self.tag_label.setObjectName("tag_label")
        self.gridLayout_2.addWidget(self.tag_label, 0, 0, 1, 1)
        self.tag_box_edit = QtWidgets.QLineEdit(self.frame_2)
        self.tag_box_edit.setObjectName("tag_box_edit")
        self.gridLayout_2.addWidget(self.tag_box_edit, 0, 1, 1, 1)
        self.data_label = QtWidgets.QLabel(self.frame_2)
        self.data_label.setObjectName("data_label")
        self.gridLayout_2.addWidget(self.data_label, 0, 2, 1, 1)
        self.data_line_edit = QtWidgets.QLineEdit(self.frame_2)
        self.data_line_edit.setObjectName("data_line_edit")
        self.gridLayout_2.addWidget(self.data_line_edit, 0, 3, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 4, 1, 1)
        self.equip_label = QtWidgets.QLabel(self.frame_2)
        self.equip_label.setObjectName("equip_label")
        self.gridLayout_2.addWidget(self.equip_label, 1, 0, 1, 1)
        self.equip_line_edit = QtWidgets.QLineEdit(self.frame_2)
        self.equip_line_edit.setObjectName("equip_line_edit")
        self.gridLayout_2.addWidget(self.equip_line_edit, 1, 1, 1, 1)
        self.pessoal_label = QtWidgets.QLabel(self.frame_2)
        self.pessoal_label.setObjectName("pessoal_label")
        self.gridLayout_2.addWidget(self.pessoal_label, 1, 2, 1, 1)
        self.pessoal_line_edit = QtWidgets.QLineEdit(self.frame_2)
        self.pessoal_line_edit.setObjectName("pessoal_line_edit")
        self.gridLayout_2.addWidget(self.pessoal_line_edit, 1, 3, 1, 2)
        self.area_label = QtWidgets.QLabel(self.frame_2)
        self.area_label.setObjectName("area_label")
        self.gridLayout_2.addWidget(self.area_label, 2, 0, 1, 1)
        self.rev_label = QtWidgets.QLabel(self.frame_2)
        self.rev_label.setObjectName("rev_label")
        self.gridLayout_2.addWidget(self.rev_label, 3, 0, 1, 1)
        self.rev_line_edit = QtWidgets.QLineEdit(self.frame_2)
        self.rev_line_edit.setObjectName("rev_line_edit")
        self.gridLayout_2.addWidget(self.rev_line_edit, 3, 1, 1, 1)
        self.station_label = QtWidgets.QLabel(self.frame_2)
        self.station_label.setObjectName("station_label")
        self.gridLayout_2.addWidget(self.station_label, 3, 2, 1, 1)
        self.station_label_edit = QtWidgets.QLineEdit(self.frame_2)
        self.station_label_edit.setObjectName("station_label_edit")
        self.gridLayout_2.addWidget(self.station_label_edit, 3, 3, 1, 2)
        self.area_label_edit = QtWidgets.QLineEdit(self.frame_2)
        self.area_label_edit.setObjectName("area_label_edit")
        self.gridLayout_2.addWidget(self.area_label_edit, 2, 1, 1, 4)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.Ainsert)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_4.addWidget(self.verticalScrollBar, 1, 1, 4, 1)
        self.frame_3 = QtWidgets.QFrame(self.Ainsert)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.m6_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m6_checkBox.setObjectName("m6_checkBox")
        self.gridLayout_3.addWidget(self.m6_checkBox, 1, 1, 1, 1)
        self.m12_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m12_checkBox.setObjectName("m12_checkBox")
        self.gridLayout_3.addWidget(self.m12_checkBox, 3, 2, 1, 1)
        self.m3_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m3_checkBox.setObjectName("m3_checkBox")
        self.gridLayout_3.addWidget(self.m3_checkBox, 2, 0, 1, 1)
        self.m8_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m8_checkBox.setObjectName("m8_checkBox")
        self.gridLayout_3.addWidget(self.m8_checkBox, 3, 1, 1, 1)
        self.m13_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m13_checkBox.setObjectName("m13_checkBox")
        self.gridLayout_3.addWidget(self.m13_checkBox, 0, 3, 1, 1)
        self.m16_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m16_checkBox.setObjectName("m16_checkBox")
        self.gridLayout_3.addWidget(self.m16_checkBox, 3, 3, 1, 1)
        self.m15_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m15_checkBox.setObjectName("m15_checkBox")
        self.gridLayout_3.addWidget(self.m15_checkBox, 2, 3, 1, 1)
        self.m5_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m5_checkBox.setObjectName("m5_checkBox")
        self.gridLayout_3.addWidget(self.m5_checkBox, 0, 1, 1, 1)
        self.m11_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m11_checkBox.setObjectName("m11_checkBox")
        self.gridLayout_3.addWidget(self.m11_checkBox, 2, 2, 1, 1)
        self.m1_checkbox = QtWidgets.QCheckBox(self.frame_3)
        self.m1_checkbox.setObjectName("m1_checkbox")
        self.gridLayout_3.addWidget(self.m1_checkbox, 0, 0, 1, 1)
        self.m10_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m10_checkBox.setObjectName("m10_checkBox")
        self.gridLayout_3.addWidget(self.m10_checkBox, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 6, 0, 1, 4)
        self.m7_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m7_checkBox.setObjectName("m7_checkBox")
        self.gridLayout_3.addWidget(self.m7_checkBox, 2, 1, 1, 1)
        self.m2_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m2_checkBox.setObjectName("m2_checkBox")
        self.gridLayout_3.addWidget(self.m2_checkBox, 1, 0, 1, 1)
        self.m4_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m4_checkBox.setObjectName("m4_checkBox")
        self.gridLayout_3.addWidget(self.m4_checkBox, 3, 0, 1, 1)
        self.m9_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m9_checkBox.setObjectName("m9_checkBox")
        self.gridLayout_3.addWidget(self.m9_checkBox, 0, 2, 1, 1)
        self.m14_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.m14_checkBox.setObjectName("m14_checkBox")
        self.gridLayout_3.addWidget(self.m14_checkBox, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)
        self.image_label = QtWidgets.QLabel(self.Ainsert)
        self.image_label.setObjectName("image_label")
        self.gridLayout_4.addWidget(self.image_label, 3, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.Ainsert)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 4, 0, 1, 1)
        self.tabWidget.addTab(self.Ainsert, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.background_frame)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 19))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOp1 = QtGui.QAction(MainWindow)
        self.actionOp1.setObjectName("actionOp1")
        self.actionOp2 = QtGui.QAction(MainWindow)
        self.actionOp2.setObjectName("actionOp2")
        self.actionOp3 = QtGui.QAction(MainWindow)
        self.actionOp3.setObjectName("actionOp3")
        self.actionarq1 = QtGui.QAction(MainWindow)
        self.actionarq1.setObjectName("actionarq1")
        self.actionar2 = QtGui.QAction(MainWindow)
        self.actionar2.setObjectName("actionar2")
        self.actionar3 = QtGui.QAction(MainWindow)
        self.actionar3.setObjectName("actionar3")
        self.actionaj1 = QtGui.QAction(MainWindow)
        self.actionaj1.setObjectName("actionaj1")
        self.actionaj2 = QtGui.QAction(MainWindow)
        self.actionaj2.setObjectName("actionaj2")
        self.actionaj3 = QtGui.QAction(MainWindow)
        self.actionaj3.setObjectName("actionaj3")
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionarq1)
        self.menuArquivo.addAction(self.actionar2)
        self.menuArquivo.addAction(self.actionar3)
        self.menuOp_es.addAction(self.actionOp1)
        self.menuOp_es.addAction(self.actionOp2)
        self.menuOp_es.addAction(self.actionOp3)
        self.menuAjuda.addAction(self.actionaj1)
        self.menuAjuda.addAction(self.actionaj2)
        self.menuAjuda.addAction(self.actionaj3)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuOp_es.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Apreview), _translate("MainWindow", "Consultar Anexo A"))
        self.title_label.setText(_translate("MainWindow", "Cabeçalho"))
        self.tag_label.setText(_translate("MainWindow", "TAG: "))
        self.data_label.setText(_translate("MainWindow", "Data:"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.equip_label.setText(_translate("MainWindow", "Equipt:"))
        self.pessoal_label.setText(_translate("MainWindow", "Pessoa Autorizada:"))
        self.area_label.setText(_translate("MainWindow", "Area/Site: "))
        self.rev_label.setText(_translate("MainWindow", "Revisão:"))
        self.station_label.setText(_translate("MainWindow", "Estação de Energia:"))
        self.m6_checkBox.setText(_translate("MainWindow", "Pressão Pneumática"))
        self.m12_checkBox.setText(_translate("MainWindow", "Químico"))
        self.m3_checkBox.setText(_translate("MainWindow", "Alta Tensão"))
        self.m8_checkBox.setText(_translate("MainWindow", "Energia Mecânica"))
        self.m13_checkBox.setText(_translate("MainWindow", "Vapor"))
        self.m16_checkBox.setText(_translate("MainWindow", "OUTROS"))
        self.m15_checkBox.setText(_translate("MainWindow", "Gás"))
        self.m5_checkBox.setText(_translate("MainWindow", "Pressão Hidrodinâmica"))
        self.m11_checkBox.setText(_translate("MainWindow", "Pressão Hidráulica"))
        self.m1_checkbox.setText(_translate("MainWindow", "Energia Elétrica 220V"))
        self.m10_checkBox.setText(_translate("MainWindow", "Pressão Pneumática"))
        self.m7_checkBox.setText(_translate("MainWindow", "Sistema de Vácuo"))
        self.m2_checkBox.setText(_translate("MainWindow", "Energia Elétrica 440V"))
        self.m4_checkBox.setText(_translate("MainWindow", "Carga Acumulada"))
        self.m9_checkBox.setText(_translate("MainWindow", "Pressão Hidroestática"))
        self.m14_checkBox.setText(_translate("MainWindow", "Térmico"))
        self.image_label.setText(_translate("MainWindow", "Previsualização de imagem:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ainsert), _translate("MainWindow", "Criar Anexo A"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuOp_es.setTitle(_translate("MainWindow", "Opções"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionOp1.setText(_translate("MainWindow", "Op1"))
        self.actionOp2.setText(_translate("MainWindow", "Op2"))
        self.actionOp3.setText(_translate("MainWindow", "Op3"))
        self.actionarq1.setText(_translate("MainWindow", "arq1"))
        self.actionar2.setText(_translate("MainWindow", "ar2"))
        self.actionar3.setText(_translate("MainWindow", "ar3"))
        self.actionaj1.setText(_translate("MainWindow", "aj1"))
        self.actionaj2.setText(_translate("MainWindow", "aj2"))
        self.actionaj3.setText(_translate("MainWindow", "aj3"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jdlv.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1207, 852)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 15, -1)
        self.gridLayout.setObjectName("gridLayout")
        
        self.gb_grid = QtWidgets.QGroupBox(Form)
        self.gb_grid.setTitle("")
        self.gb_grid.setObjectName("gb_grid")
        
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gb_grid)
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.tablew_grid = QtWidgets.QTableWidget(self.gb_grid)
        
        font = QtGui.QFont()
        font.setPointSize(8)
        
        self.tablew_grid.setFont(font)
        self.tablew_grid.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tablew_grid.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tablew_grid.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tablew_grid.setObjectName("tablew_grid")
        self.tablew_grid.setColumnCount(0)
        self.tablew_grid.setRowCount(0)
        self.tablew_grid.horizontalHeader().setDefaultSectionSize(10)
        self.tablew_grid.horizontalHeader().setMinimumSectionSize(10)
        self.tablew_grid.verticalHeader().setDefaultSectionSize(10)
        self.tablew_grid.verticalHeader().setMinimumSectionSize(10)
        
        self.tablew_grid.setShowGrid(False)
        
        
        self.gridLayout_5.addWidget(self.tablew_grid, 2, 0, 1, 1)
        
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        self.cb_figures_de_base = QtWidgets.QComboBox(self.gb_grid)
        self.cb_figures_de_base.setMinimumSize(QtCore.QSize(180, 0))
        self.cb_figures_de_base.setObjectName("cb_figures_de_base")
        
        self.gridLayout_6.addWidget(self.cb_figures_de_base, 0, 2, 1, 1)
        
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.gridLayout_8.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 7, 1, 1)
        self.pb_add_examples = QtWidgets.QPushButton(self.gb_grid)
        self.pb_add_examples.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/signe_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_add_examples.setIcon(icon)
        self.pb_add_examples.setObjectName("pb_add_examples")
        self.gridLayout_6.addWidget(self.pb_add_examples, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 5, 1, 1)
        self.label_numero_generation = QtWidgets.QLabel(self.gb_grid)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numero_generation.setFont(font)
        self.label_numero_generation.setObjectName("label_numero_generation")
        self.gridLayout_6.addWidget(self.label_numero_generation, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pb_copier = QtWidgets.QPushButton(self.gb_grid)
        self.pb_copier.setObjectName("pb_copier")
        self.gridLayout_9.addWidget(self.pb_copier, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 1, 1, 1)
        self.pb_effacer = QtWidgets.QPushButton(self.gb_grid)
        self.pb_effacer.setObjectName("pb_effacer")
        self.gridLayout_9.addWidget(self.pb_effacer, 0, 4, 1, 1)
        self.pb_coller = QtWidgets.QPushButton(self.gb_grid)
        self.pb_coller.setObjectName("pb_coller")
        self.gridLayout_9.addWidget(self.pb_coller, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_9, 0, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.gb_grid, 0, 0, 1, 1)
        self.gb_push_buttons = QtWidgets.QGroupBox(Form)
        self.gb_push_buttons.setMaximumSize(QtCore.QSize(150, 16777215))
        self.gb_push_buttons.setTitle("")
        self.gb_push_buttons.setObjectName("gb_push_buttons")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gb_push_buttons)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pb_quit = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_quit.setObjectName("pb_quit")
        self.gridLayout_3.addWidget(self.pb_quit, 15, 0, 1, 1)
        self.pb_load = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_load.setObjectName("pb_load")
        self.gridLayout_3.addWidget(self.pb_load, 13, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 12, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 14, 0, 1, 1)
        self.pb_reset = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_reset.setObjectName("pb_reset")
        self.gridLayout_3.addWidget(self.pb_reset, 7, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 6, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 8, 0, 1, 1)
        self.pb_save = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_save.setObjectName("pb_save")
        self.gridLayout_3.addWidget(self.pb_save, 9, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pb_undo_play = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_undo_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_undo_play.setIcon(icon1)
        self.pb_undo_play.setObjectName("pb_undo_play")
        self.gridLayout_7.addWidget(self.pb_undo_play, 0, 0, 1, 1)
        self.pb_redo_play = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_redo_play.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_redo_play.setIcon(icon2)
        self.pb_redo_play.setObjectName("pb_redo_play")
        self.gridLayout_7.addWidget(self.pb_redo_play, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem11, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem12, 10, 0, 1, 1)
        self.pb_play_pause = QtWidgets.QPushButton(self.gb_push_buttons)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/play.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pb_play_pause.setIcon(icon3)
        self.pb_play_pause.setIconSize(QtCore.QSize(32, 32))
        self.pb_play_pause.setObjectName("pb_play_pause")
        self.gridLayout_3.addWidget(self.pb_play_pause, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 5, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem13, 2, 0, 1, 1)
        self.pb_save_as = QtWidgets.QPushButton(self.gb_push_buttons)
        self.pb_save_as.setObjectName("pb_save_as")
        self.gridLayout_3.addWidget(self.pb_save_as, 11, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem14, 4, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem15, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.gb_push_buttons, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_add_examples.setToolTip(_translate("Form", "<html><head/><body><p>Ajouter un répertoire contenant des exemples</p></body></html>"))
        self.label_numero_generation.setText(_translate("Form", "Votre liste d\'exemples"))
        self.pb_copier.setText(_translate("Form", "Copier"))
        self.pb_effacer.setText(_translate("Form", "Effacer"))
        self.pb_coller.setText(_translate("Form", "Coller"))
        self.pb_quit.setText(_translate("Form", "  Quitter"))
        self.pb_load.setText(_translate("Form", "  Load"))
        self.pb_reset.setText(_translate("Form", "   Reset"))
        self.pb_save.setText(_translate("Form", "  Save"))
        self.pb_undo_play.setToolTip(_translate("Form", "<html><head/><body><p>Parcours des états sauvegardés à chaque clique sur &quot;Play&quot;</p></body></html>"))
        self.pb_redo_play.setToolTip(_translate("Form", "<html><head/><body><p>Parcours des états sauvegardés à chaque clique sur &quot;Play&quot;</p></body></html>"))
        self.pb_play_pause.setText(_translate("Form", "  play / pause"))
        self.pushButton.setText(_translate("Form", "Play from scene"))
        self.pb_save_as.setText(_translate("Form", "Save As"))
import jdlv_rc

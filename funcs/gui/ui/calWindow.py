# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutVertMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutVertMain.setContentsMargins(0, 0, 0, 0)
        self.layoutVertMain.setObjectName("layoutVertMain")
        self.btnLoadHDF5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnLoadHDF5.setMinimumSize(QtCore.QSize(0, 25))
        self.btnLoadHDF5.setBaseSize(QtCore.QSize(0, 25))
        self.btnLoadHDF5.setObjectName("btnLoadHDF5")
        self.layoutVertMain.addWidget(self.btnLoadHDF5)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutVertMain.addWidget(self.line_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layoutFormSelectDate = QtWidgets.QFormLayout()
        self.layoutFormSelectDate.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.layoutFormSelectDate.setObjectName("layoutFormSelectDate")
        self.lblSelectDate = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblSelectDate.setEnabled(False)
        self.lblSelectDate.setObjectName("lblSelectDate")
        self.layoutFormSelectDate.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSelectDate)
        self.cboxSelectDate = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cboxSelectDate.setEnabled(False)
        self.cboxSelectDate.setMinimumSize(QtCore.QSize(240, 0))
        self.cboxSelectDate.setObjectName("cboxSelectDate")
        self.layoutFormSelectDate.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cboxSelectDate)
        self.verticalLayout_4.addLayout(self.layoutFormSelectDate)
        self.layoutHorizShotSelect = QtWidgets.QHBoxLayout()
        self.layoutHorizShotSelect.setObjectName("layoutHorizShotSelect")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutHorizShotSelect.addItem(spacerItem)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.inpStartShot = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inpStartShot.setEnabled(False)
        self.inpStartShot.setMinimumSize(QtCore.QSize(50, 25))
        self.inpStartShot.setMaximumSize(QtCore.QSize(50, 25))
        self.inpStartShot.setAlignment(QtCore.Qt.AlignCenter)
        self.inpStartShot.setObjectName("inpStartShot")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inpStartShot)
        self.lblStartShot = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblStartShot.setEnabled(False)
        self.lblStartShot.setObjectName("lblStartShot")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblStartShot)
        self.layoutHorizShotSelect.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lblEndShot = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblEndShot.setEnabled(False)
        self.lblEndShot.setObjectName("lblEndShot")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblEndShot)
        self.inpEndShot = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inpEndShot.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inpEndShot.sizePolicy().hasHeightForWidth())
        self.inpEndShot.setSizePolicy(sizePolicy)
        self.inpEndShot.setMinimumSize(QtCore.QSize(50, 25))
        self.inpEndShot.setMaximumSize(QtCore.QSize(50, 25))
        self.inpEndShot.setBaseSize(QtCore.QSize(0, 0))
        self.inpEndShot.setAlignment(QtCore.Qt.AlignCenter)
        self.inpEndShot.setObjectName("inpEndShot")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inpEndShot)
        self.layoutHorizShotSelect.addLayout(self.formLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutHorizShotSelect.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.layoutHorizShotSelect)
        self.layoutVertMain.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutVertMain.addWidget(self.line)
        self.layoutSecondDay = QtWidgets.QVBoxLayout()
        self.layoutSecondDay.setObjectName("layoutSecondDay")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.chkUseDate2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkUseDate2.setEnabled(False)
        self.chkUseDate2.setObjectName("chkUseDate2")
        self.horizontalLayout.addWidget(self.chkUseDate2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.layoutSecondDay.addLayout(self.horizontalLayout)
        self.layoutFormSelectDate2 = QtWidgets.QFormLayout()
        self.layoutFormSelectDate2.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.layoutFormSelectDate2.setObjectName("layoutFormSelectDate2")
        self.lblSelectDate2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblSelectDate2.setEnabled(False)
        self.lblSelectDate2.setObjectName("lblSelectDate2")
        self.layoutFormSelectDate2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSelectDate2)
        self.cboxSelectDate2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cboxSelectDate2.setEnabled(False)
        self.cboxSelectDate2.setMinimumSize(QtCore.QSize(240, 0))
        self.cboxSelectDate2.setObjectName("cboxSelectDate2")
        self.layoutFormSelectDate2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cboxSelectDate2)
        self.layoutSecondDay.addLayout(self.layoutFormSelectDate2)
        self.layoutHorizShotSelect_4 = QtWidgets.QHBoxLayout()
        self.layoutHorizShotSelect_4.setObjectName("layoutHorizShotSelect_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutHorizShotSelect_4.addItem(spacerItem4)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_8.setObjectName("formLayout_8")
        self.inpStartShot2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inpStartShot2.setEnabled(False)
        self.inpStartShot2.setMinimumSize(QtCore.QSize(50, 25))
        self.inpStartShot2.setMaximumSize(QtCore.QSize(50, 25))
        self.inpStartShot2.setAlignment(QtCore.Qt.AlignCenter)
        self.inpStartShot2.setObjectName("inpStartShot2")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inpStartShot2)
        self.lblStartShot2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblStartShot2.setEnabled(False)
        self.lblStartShot2.setObjectName("lblStartShot2")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblStartShot2)
        self.layoutHorizShotSelect_4.addLayout(self.formLayout_8)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_9.setObjectName("formLayout_9")
        self.lblEndShot2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblEndShot2.setEnabled(False)
        self.lblEndShot2.setObjectName("lblEndShot2")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblEndShot2)
        self.inpEndShot2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.inpEndShot2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inpEndShot2.sizePolicy().hasHeightForWidth())
        self.inpEndShot2.setSizePolicy(sizePolicy)
        self.inpEndShot2.setMinimumSize(QtCore.QSize(50, 25))
        self.inpEndShot2.setMaximumSize(QtCore.QSize(50, 25))
        self.inpEndShot2.setBaseSize(QtCore.QSize(0, 0))
        self.inpEndShot2.setAlignment(QtCore.Qt.AlignCenter)
        self.inpEndShot2.setObjectName("inpEndShot2")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inpEndShot2)
        self.layoutHorizShotSelect_4.addLayout(self.formLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutHorizShotSelect_4.addItem(spacerItem5)
        self.layoutSecondDay.addLayout(self.layoutHorizShotSelect_4)
        self.layoutVertMain.addLayout(self.layoutSecondDay)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutVertMain.addWidget(self.line_2)
        self.layoutHorizStoredSpatials = QtWidgets.QHBoxLayout()
        self.layoutHorizStoredSpatials.setObjectName("layoutHorizStoredSpatials")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutHorizStoredSpatials.addItem(spacerItem6)
        self.lblStoredCalibrations = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblStoredCalibrations.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStoredCalibrations.setObjectName("lblStoredCalibrations")
        self.layoutHorizStoredSpatials.addWidget(self.lblStoredCalibrations)
        self.chkStoredNear = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkStoredNear.setCheckable(True)
        self.chkStoredNear.setObjectName("chkStoredNear")
        self.layoutHorizStoredSpatials.addWidget(self.chkStoredNear)
        self.chkStoredFar = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkStoredFar.setCheckable(True)
        self.chkStoredFar.setObjectName("chkStoredFar")
        self.layoutHorizStoredSpatials.addWidget(self.chkStoredFar)
        self.chkStoredCenterline = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkStoredCenterline.setCheckable(True)
        self.chkStoredCenterline.setObjectName("chkStoredCenterline")
        self.layoutHorizStoredSpatials.addWidget(self.chkStoredCenterline)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutHorizStoredSpatials.addItem(spacerItem7)
        self.layoutVertMain.addLayout(self.layoutHorizStoredSpatials)
        self.layoutFormSelectSpatialLocation = QtWidgets.QFormLayout()
        self.layoutFormSelectSpatialLocation.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.layoutFormSelectSpatialLocation.setObjectName("layoutFormSelectSpatialLocation")
        self.lblSelectSpatialLocation = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblSelectSpatialLocation.setObjectName("lblSelectSpatialLocation")
        self.layoutFormSelectSpatialLocation.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSelectSpatialLocation)
        self.cboxSelectLocation = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cboxSelectLocation.setMinimumSize(QtCore.QSize(240, 0))
        self.cboxSelectLocation.setObjectName("cboxSelectLocation")
        self.cboxSelectLocation.addItem("")
        self.cboxSelectLocation.addItem("")
        self.layoutFormSelectSpatialLocation.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cboxSelectLocation)
        self.layoutVertMain.addLayout(self.layoutFormSelectSpatialLocation)
        self.btnLoadAndCalibrate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnLoadAndCalibrate.setEnabled(False)
        self.btnLoadAndCalibrate.setMinimumSize(QtCore.QSize(0, 25))
        self.btnLoadAndCalibrate.setBaseSize(QtCore.QSize(0, 25))
        self.btnLoadAndCalibrate.setObjectName("btnLoadAndCalibrate")
        self.layoutVertMain.addWidget(self.btnLoadAndCalibrate)
        self.btnStoreCalibration = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnStoreCalibration.setEnabled(False)
        self.btnStoreCalibration.setMinimumSize(QtCore.QSize(0, 25))
        self.btnStoreCalibration.setBaseSize(QtCore.QSize(0, 25))
        self.btnStoreCalibration.setObjectName("btnStoreCalibration")
        self.layoutVertMain.addWidget(self.btnStoreCalibration)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layoutVertMain.addWidget(self.line_3)
        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setMinimumSize(QtCore.QSize(0, 100))
        self.btnExit.setBaseSize(QtCore.QSize(0, 50))
        self.btnExit.setObjectName("btnExit")
        self.layoutVertMain.addWidget(self.btnExit)
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Schlieren Spatial Calibration"))
        self.btnLoadHDF5.setText(_translate("MainWindow", "Load Schlieren HDF5"))
        self.lblSelectDate.setText(_translate("MainWindow", "Select Date"))
        self.lblStartShot.setText(_translate("MainWindow", "Start Shot"))
        self.lblEndShot.setText(_translate("MainWindow", "End Shot"))
        self.chkUseDate2.setText(_translate("MainWindow", "Use a second day"))
        self.lblSelectDate2.setText(_translate("MainWindow", "Select Date"))
        self.lblStartShot2.setText(_translate("MainWindow", "Start Shot"))
        self.lblEndShot2.setText(_translate("MainWindow", "End Shot"))
        self.lblStoredCalibrations.setText(_translate("MainWindow", "Stored Spatial Calibrations:"))
        self.chkStoredNear.setText(_translate("MainWindow", "Near"))
        self.chkStoredFar.setText(_translate("MainWindow", "Far"))
        self.chkStoredCenterline.setText(_translate("MainWindow", "Centerline"))
        self.lblSelectSpatialLocation.setText(_translate("MainWindow", "Select Spatial Location"))
        self.cboxSelectLocation.setItemText(0, _translate("MainWindow", "Near"))
        self.cboxSelectLocation.setItemText(1, _translate("MainWindow", "Far"))
        self.btnLoadAndCalibrate.setText(_translate("MainWindow", "Load Spatial and Perform Calibration"))
        self.btnStoreCalibration.setText(_translate("MainWindow", "Store Calibration"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))

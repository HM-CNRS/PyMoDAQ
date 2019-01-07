# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer2D_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(819, 487)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Show_histogram = QtWidgets.QPushButton(Form)
        self.Show_histogram.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/Histogram.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Show_histogram.setIcon(icon)
        self.Show_histogram.setCheckable(True)
        self.Show_histogram.setObjectName("Show_histogram")
        self.horizontalLayout_2.addWidget(self.Show_histogram)
        self.roiBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.roiBtn.sizePolicy().hasHeightForWidth())
        self.roiBtn.setSizePolicy(sizePolicy)
        self.roiBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.roiBtn.setBaseSize(QtCore.QSize(50, 0))
        self.roiBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/Region.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.roiBtn.setIcon(icon1)
        self.roiBtn.setCheckable(True)
        self.roiBtn.setObjectName("roiBtn")
        self.horizontalLayout_2.addWidget(self.roiBtn)
        self.isocurve_pb = QtWidgets.QPushButton(Form)
        self.isocurve_pb.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/meshPlot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.isocurve_pb.setIcon(icon2)
        self.isocurve_pb.setCheckable(True)
        self.isocurve_pb.setObjectName("isocurve_pb")
        self.horizontalLayout_2.addWidget(self.isocurve_pb)
        self.Ini_plot_pb = QtWidgets.QPushButton(Form)
        self.Ini_plot_pb.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.Ini_plot_pb.setIcon(icon3)
        self.Ini_plot_pb.setObjectName("Ini_plot_pb")
        self.horizontalLayout_2.addWidget(self.Ini_plot_pb)
        self.aspect_ratio_pb = QtWidgets.QPushButton(Form)
        self.aspect_ratio_pb.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/Zoom_1_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.aspect_ratio_pb.setIcon(icon4)
        self.aspect_ratio_pb.setCheckable(True)
        self.aspect_ratio_pb.setObjectName("aspect_ratio_pb")
        self.horizontalLayout_2.addWidget(self.aspect_ratio_pb)
        self.auto_levels_pb = QtWidgets.QPushButton(Form)
        self.auto_levels_pb.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/autoscale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.auto_levels_pb.setIcon(icon5)
        self.auto_levels_pb.setCheckable(True)
        self.auto_levels_pb.setObjectName("auto_levels_pb")
        self.horizontalLayout_2.addWidget(self.auto_levels_pb)
        self.crosshair_pb = QtWidgets.QPushButton(Form)
        self.crosshair_pb.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.crosshair_pb.setIcon(icon6)
        self.crosshair_pb.setCheckable(True)
        self.crosshair_pb.setObjectName("crosshair_pb")
        self.horizontalLayout_2.addWidget(self.crosshair_pb)
        self.ROIselect_pb = QtWidgets.QPushButton(Form)
        self.ROIselect_pb.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/Select_24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ROIselect_pb.setIcon(icon7)
        self.ROIselect_pb.setCheckable(True)
        self.ROIselect_pb.setObjectName("ROIselect_pb")
        self.horizontalLayout_2.addWidget(self.ROIselect_pb)
        self.FlipUD_pb = QtWidgets.QPushButton(Form)
        self.FlipUD_pb.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/scale_vertically.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FlipUD_pb.setIcon(icon8)
        self.FlipUD_pb.setCheckable(True)
        self.FlipUD_pb.setObjectName("FlipUD_pb")
        self.horizontalLayout_2.addWidget(self.FlipUD_pb)
        self.FlipLR_pb = QtWidgets.QPushButton(Form)
        self.FlipLR_pb.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/scale_horizontally.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FlipLR_pb.setIcon(icon9)
        self.FlipLR_pb.setCheckable(True)
        self.FlipLR_pb.setObjectName("FlipLR_pb")
        self.horizontalLayout_2.addWidget(self.FlipLR_pb)
        self.rotate_pb = QtWidgets.QPushButton(Form)
        self.rotate_pb.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/rotation2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_pb.setIcon(icon10)
        self.rotate_pb.setCheckable(True)
        self.rotate_pb.setObjectName("rotate_pb")
        self.horizontalLayout_2.addWidget(self.rotate_pb)
        self.x_label = QtWidgets.QLabel(Form)
        self.x_label.setObjectName("x_label")
        self.horizontalLayout_2.addWidget(self.x_label)
        self.y_label = QtWidgets.QLabel(Form)
        self.y_label.setObjectName("y_label")
        self.horizontalLayout_2.addWidget(self.y_label)
        self.z_label_red = QtWidgets.QPushButton(Form)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/r_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_label_red.setIcon(icon11)
        self.z_label_red.setFlat(True)
        self.z_label_red.setObjectName("z_label_red")
        self.horizontalLayout_2.addWidget(self.z_label_red)
        self.z_label_green = QtWidgets.QPushButton(Form)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/g_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_label_green.setIcon(icon12)
        self.z_label_green.setFlat(True)
        self.z_label_green.setObjectName("z_label_green")
        self.horizontalLayout_2.addWidget(self.z_label_green)
        self.z_label_blue = QtWidgets.QPushButton(Form)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Labview_icons/Icon_Library/b_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_label_blue.setIcon(icon13)
        self.z_label_blue.setFlat(True)
        self.z_label_blue.setObjectName("z_label_blue")
        self.horizontalLayout_2.addWidget(self.z_label_blue)
        self.red_cb = QtWidgets.QCheckBox(Form)
        self.red_cb.setObjectName("red_cb")
        self.horizontalLayout_2.addWidget(self.red_cb)
        self.green_cb = QtWidgets.QCheckBox(Form)
        self.green_cb.setObjectName("green_cb")
        self.horizontalLayout_2.addWidget(self.green_cb)
        self.blue_cb = QtWidgets.QCheckBox(Form)
        self.blue_cb.setObjectName("blue_cb")
        self.horizontalLayout_2.addWidget(self.blue_cb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_VLeft = QtWidgets.QSplitter(self.splitter)
        self.splitter_VLeft.setOrientation(QtCore.Qt.Vertical)
        self.splitter_VLeft.setObjectName("splitter_VLeft")
        self.graphicsView = GraphicsLayoutWidget(self.splitter_VLeft)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(50, 50))
        self.graphicsView.setObjectName("graphicsView")
        self.Lineout_H = PlotWidget(self.splitter_VLeft)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lineout_H.sizePolicy().hasHeightForWidth())
        self.Lineout_H.setSizePolicy(sizePolicy)
        self.Lineout_H.setMinimumSize(QtCore.QSize(0, 50))
        self.Lineout_H.setObjectName("Lineout_H")
        self.splitter_VRight = QtWidgets.QSplitter(self.splitter)
        self.splitter_VRight.setEnabled(True)
        self.splitter_VRight.setOrientation(QtCore.Qt.Vertical)
        self.splitter_VRight.setHandleWidth(5)
        self.splitter_VRight.setObjectName("splitter_VRight")
        self.Lineout_V = PlotWidget(self.splitter_VRight)
        self.Lineout_V.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lineout_V.sizePolicy().hasHeightForWidth())
        self.Lineout_V.setSizePolicy(sizePolicy)
        self.Lineout_V.setMinimumSize(QtCore.QSize(50, 0))
        self.Lineout_V.setObjectName("Lineout_V")
        self.Lineout_integrated = PlotWidget(self.splitter_VRight)
        self.Lineout_integrated.setObjectName("Lineout_integrated")
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Show_histogram.setToolTip(_translate("Form", "Histogram"))
        self.roiBtn.setToolTip(_translate("Form", "ROI"))
        self.isocurve_pb.setToolTip(_translate("Form", "Show iso-curve"))
        self.Ini_plot_pb.setToolTip(_translate("Form", "Ini Plot"))
        self.aspect_ratio_pb.setToolTip(_translate("Form", "set aspect ratio to 1"))
        self.auto_levels_pb.setToolTip(_translate("Form", "Turn on/off the intensity autolevel"))
        self.crosshair_pb.setToolTip(_translate("Form", "Show/hide crosshair"))
        self.ROIselect_pb.setToolTip(_translate("Form", "Show/hide ROI scan area selection"))
        self.FlipUD_pb.setToolTip(_translate("Form", "Flip image up->down"))
        self.FlipLR_pb.setToolTip(_translate("Form", "Flip image left->right"))
        self.rotate_pb.setToolTip(_translate("Form", "Rotate image by 90°"))
        self.x_label.setText(_translate("Form", "x:"))
        self.y_label.setText(_translate("Form", "y:"))
        self.z_label_red.setText(_translate("Form", "z_red"))
        self.z_label_green.setText(_translate("Form", "z_green"))
        self.z_label_blue.setText(_translate("Form", "z_blue"))
        self.red_cb.setText(_translate("Form", "Red"))
        self.green_cb.setText(_translate("Form", "Green"))
        self.blue_cb.setText(_translate("Form", "Blue"))

from pyqtgraph import GraphicsLayoutWidget, PlotWidget
from pymodaq.QtDesigner_Ressources import QtDesigner_ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


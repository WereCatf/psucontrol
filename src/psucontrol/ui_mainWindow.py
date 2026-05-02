# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from indicatorlabel import IndicatorLabel
from lcdlabel import LcdLabel
import psucontrol.rc_gui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(623, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/graphics/psucontrol.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionM_buttons = QAction(MainWindow)
        self.actionM_buttons.setObjectName(u"actionM_buttons")
        self.actionM_buttons.setCheckable(True)
        self.actionM_buttons.setChecked(True)
        font1 = QFont()
        self.actionM_buttons.setFont(font1)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(9, -1, 9, -1)
        self.serialPortSettingsLayout = QHBoxLayout()
        self.serialPortSettingsLayout.setObjectName(u"serialPortSettingsLayout")
        self.serialPortSettingsLayout.setContentsMargins(9, 9, 9, 9)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.serialPortSettingsLayout.addWidget(self.label_2)

        self.serialPortBox = QComboBox(self.centralwidget)
        self.serialPortBox.setObjectName(u"serialPortBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.serialPortBox.sizePolicy().hasHeightForWidth())
        self.serialPortBox.setSizePolicy(sizePolicy1)
        self.serialPortBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.serialPortSettingsLayout.addWidget(self.serialPortBox)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")

        self.serialPortSettingsLayout.addWidget(self.connectButton)


        self.mainLayout.addLayout(self.serialPortSettingsLayout)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.frame_5.setPalette(palette)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_2 = QFrame(self.frame_5)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        palette1 = QPalette()
        brush1 = QBrush(QColor(166, 169, 159, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.verticalFrame_2.setPalette(palette1)
        self.verticalFrame_2.setAutoFillBackground(False)
        self.verticalFrame_2.setStyleSheet(u"QFrame#verticalFrame_2 {\n"
"     border-left: 1px solid black;\n"
"	 border-top: 2px solid black;\n"
"	 border-right: 0px;\n"
"	 border-bottom: 0px;\n"
"background-color: #a6a99f;\n"
"}")
        self.verticalFrame_2.setFrameShape(QFrame.Shape.Box)
        self.verticalFrame_2.setLineWidth(1)
        self.verticalLayout_12 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.voltageOutputLabel = LcdLabel(self.verticalFrame_2)
        self.voltageOutputLabel.setObjectName(u"voltageOutputLabel")
        font2 = QFont()
        font2.setFamilies([u"DSEG7 Classic Mini"])
        font2.setPointSize(32)
        font2.setBold(True)
        self.voltageOutputLabel.setFont(font2)
        self.voltageOutputLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.voltageOutputLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.voltageOutputLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.verticalLayout_12.addWidget(self.voltageOutputLabel)

        self.currentOutputLabel = LcdLabel(self.verticalFrame_2)
        self.currentOutputLabel.setObjectName(u"currentOutputLabel")
        self.currentOutputLabel.setFont(font2)
        self.currentOutputLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.currentOutputLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.currentOutputLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.verticalLayout_12.addWidget(self.currentOutputLabel)

        self.powerOutputLabel = LcdLabel(self.verticalFrame_2)
        self.powerOutputLabel.setObjectName(u"powerOutputLabel")
        self.powerOutputLabel.setFont(font2)
        self.powerOutputLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.powerOutputLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.powerOutputLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.verticalLayout_12.addWidget(self.powerOutputLabel)


        self.gridLayout_2.addWidget(self.verticalFrame_2, 1, 2, 1, 1)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame_3.setPalette(palette2)
        self.frame_3.setFont(font)
        self.frame_3.setAutoFillBackground(True)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 9)
        self.modelLabel = QLabel(self.frame_3)
        self.modelLabel.setObjectName(u"modelLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.modelLabel.sizePolicy().hasHeightForWidth())
        self.modelLabel.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.modelLabel.setFont(font3)
        self.modelLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.modelLabel.setScaledContents(False)
        self.modelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.modelLabel)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)


        self.gridLayout_2.addWidget(self.frame_3, 0, 2, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_14.setContentsMargins(12, -1, 12, -1)
        self.indicatorOvp = IndicatorLabel(self.frame_5)
        self.indicatorOvp.setObjectName(u"indicatorOvp")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.indicatorOvp.sizePolicy().hasHeightForWidth())
        self.indicatorOvp.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 228))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.indicatorOvp.setPalette(palette3)
        self.indicatorOvp.setFont(font3)
        self.indicatorOvp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.indicatorOvp.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.indicatorOvp.setProperty(u"checked", False)
        self.indicatorOvp.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorOvp.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorOvp.setProperty(u"spacing", 6)

        self.verticalLayout_14.addWidget(self.indicatorOvp)

        self.indicatorOcp = IndicatorLabel(self.frame_5)
        self.indicatorOcp.setObjectName(u"indicatorOcp")
        sizePolicy2.setHeightForWidth(self.indicatorOcp.sizePolicy().hasHeightForWidth())
        self.indicatorOcp.setSizePolicy(sizePolicy2)
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.indicatorOcp.setPalette(palette4)
        self.indicatorOcp.setFont(font3)
        self.indicatorOcp.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorOcp.setProperty(u"checked", False)
        self.indicatorOcp.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorOcp.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorOcp.setProperty(u"spacing", 6)

        self.verticalLayout_14.addWidget(self.indicatorOcp)

        self.indicatorCc = IndicatorLabel(self.frame_5)
        self.indicatorCc.setObjectName(u"indicatorCc")
        sizePolicy2.setHeightForWidth(self.indicatorCc.sizePolicy().hasHeightForWidth())
        self.indicatorCc.setSizePolicy(sizePolicy2)
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.indicatorCc.setPalette(palette5)
        self.indicatorCc.setFont(font3)
        self.indicatorCc.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorCc.setProperty(u"checked", False)
        self.indicatorCc.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorCc.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorCc.setProperty(u"spacing", 6)

        self.verticalLayout_14.addWidget(self.indicatorCc)

        self.indicatorCv = IndicatorLabel(self.frame_5)
        self.indicatorCv.setObjectName(u"indicatorCv")
        sizePolicy2.setHeightForWidth(self.indicatorCv.sizePolicy().hasHeightForWidth())
        self.indicatorCv.setSizePolicy(sizePolicy2)
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.indicatorCv.setPalette(palette6)
        self.indicatorCv.setFont(font3)
        self.indicatorCv.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorCv.setProperty(u"checked", False)
        self.indicatorCv.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorCv.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorCv.setProperty(u"spacing", 6)

        self.verticalLayout_14.addWidget(self.indicatorCv)

        self.indicatorLabel = IndicatorLabel(self.frame_5)
        self.indicatorLabel.setObjectName(u"indicatorLabel")
        sizePolicy2.setHeightForWidth(self.indicatorLabel.sizePolicy().hasHeightForWidth())
        self.indicatorLabel.setSizePolicy(sizePolicy2)
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.indicatorLabel.setPalette(palette7)
        self.indicatorLabel.setFont(font3)
        self.indicatorLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorLabel.setProperty(u"checked", False)
        self.indicatorLabel.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorLabel.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorLabel.setProperty(u"spacing", 6)

        self.verticalLayout_14.addWidget(self.indicatorLabel)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 1, 3, 1, 1)

        self.memoryButtonWidget = QWidget(self.frame_5)
        self.memoryButtonWidget.setObjectName(u"memoryButtonWidget")
        self.memoryButtonWidget.setMinimumSize(QSize(0, 50))
        self.memoryButtonWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.memoryButtonWidget)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.m1Button = QPushButton(self.memoryButtonWidget)
        self.m1Button.setObjectName(u"m1Button")
        self.m1Button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.m1Button.sizePolicy().hasHeightForWidth())
        self.m1Button.setSizePolicy(sizePolicy)
        self.m1Button.setFont(font3)
        self.m1Button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 70, 70);\n"
"padding: 9px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: red;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:checked {\n"
"background-color: rgb(127, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed:checked {\n"
"color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.m1Button)

        self.m2Button = QPushButton(self.memoryButtonWidget)
        self.m2Button.setObjectName(u"m2Button")
        self.m2Button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.m2Button.sizePolicy().hasHeightForWidth())
        self.m2Button.setSizePolicy(sizePolicy)
        self.m2Button.setFont(font3)
        self.m2Button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 70, 70);\n"
"padding: 9px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: red;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:checked {\n"
"background-color: rgb(127, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed:checked {\n"
"color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.m2Button)

        self.m3Button = QPushButton(self.memoryButtonWidget)
        self.m3Button.setObjectName(u"m3Button")
        self.m3Button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.m3Button.sizePolicy().hasHeightForWidth())
        self.m3Button.setSizePolicy(sizePolicy)
        self.m3Button.setFont(font3)
        self.m3Button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 70, 70);\n"
"padding: 9px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: red;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:checked {\n"
"background-color: rgb(127, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed:checked {\n"
"color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.m3Button)

        self.m4Button = QPushButton(self.memoryButtonWidget)
        self.m4Button.setObjectName(u"m4Button")
        self.m4Button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.m4Button.sizePolicy().hasHeightForWidth())
        self.m4Button.setSizePolicy(sizePolicy)
        self.m4Button.setFont(font3)
        self.m4Button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 70, 70);\n"
"padding: 9px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: red;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:checked {\n"
"background-color: rgb(127, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed:checked {\n"
"color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.m4Button)

        self.m5Button = QPushButton(self.memoryButtonWidget)
        self.m5Button.setObjectName(u"m5Button")
        self.m5Button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.m5Button.sizePolicy().hasHeightForWidth())
        self.m5Button.setSizePolicy(sizePolicy)
        self.m5Button.setFont(font3)
        self.m5Button.setAutoFillBackground(False)
        self.m5Button.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 70, 70);\n"
"padding: 9px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: red;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:checked {\n"
"background-color: rgb(127, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed:checked {\n"
"color: black;\n"
"}")
        self.m5Button.setIconSize(QSize(0, 0))
        self.m5Button.setCheckable(False)
        self.m5Button.setFlat(False)

        self.horizontalLayout.addWidget(self.m5Button)

        self.saveButton = QPushButton(self.memoryButtonWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setFont(font3)
        self.saveButton.setAutoFillBackground(False)
        self.saveButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 70, 70);\n"
"padding: 9px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: red;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:checked {\n"
"background-color: rgb(127, 0, 0);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:pressed:checked {\n"
"color: black;\n"
"}")
        self.saveButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.memoryButtonWidget, 2, 1, 1, 2)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.frame.setPalette(palette8)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 9)
        self.manufacturerLabel = QLabel(self.frame)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        sizePolicy2.setHeightForWidth(self.manufacturerLabel.sizePolicy().hasHeightForWidth())
        self.manufacturerLabel.setSizePolicy(sizePolicy2)
        self.manufacturerLabel.setFont(font3)
        self.manufacturerLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.manufacturerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.manufacturerLabel)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)

        self.verticalFrame = QFrame(self.frame_5)
        self.verticalFrame.setObjectName(u"verticalFrame")
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.verticalFrame.setPalette(palette9)
        self.verticalFrame.setAutoFillBackground(False)
        self.verticalFrame.setStyleSheet(u"QFrame#verticalFrame {\n"
"     border-right: 1px solid black;\n"
"	 border-top: 2px solid black;\n"
"	 border-left: 0px;\n"
"	 border-bottom: 0px;\n"
"background-color: #a6a99f;\n"
"}")
        self.verticalFrame.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.voltageLimitLabel = LcdLabel(self.verticalFrame)
        self.voltageLimitLabel.setObjectName(u"voltageLimitLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.voltageLimitLabel.sizePolicy().hasHeightForWidth())
        self.voltageLimitLabel.setSizePolicy(sizePolicy4)
        self.voltageLimitLabel.setFont(font2)
        self.voltageLimitLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.voltageLimitLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.voltageLimitLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.verticalLayout_11.addWidget(self.voltageLimitLabel)

        self.currentLimitLabel = LcdLabel(self.verticalFrame)
        self.currentLimitLabel.setObjectName(u"currentLimitLabel")
        self.currentLimitLabel.setFont(font2)
        self.currentLimitLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.currentLimitLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.currentLimitLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.verticalLayout_11.addWidget(self.currentLimitLabel)

        self.powerLimitLabel = LcdLabel(self.verticalFrame)
        self.powerLimitLabel.setObjectName(u"powerLimitLabel")
        self.powerLimitLabel.setFont(font2)
        self.powerLimitLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.powerLimitLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.powerLimitLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.verticalLayout_11.addWidget(self.powerLimitLabel)


        self.gridLayout_2.addWidget(self.verticalFrame, 1, 1, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_13.setContentsMargins(12, -1, 12, -1)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.label_4.setPalette(palette10)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(32)
        font4.setBold(True)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.label_3.setPalette(palette11)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush2)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush2)
        self.label_6.setPalette(palette12)
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_6)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 1, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 100)
        self.gridLayout_2.setColumnStretch(2, 100)
        self.gridLayout_2.setColumnStretch(3, 1)

        self.mainLayout.addWidget(self.frame_5)

        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setSpacing(10)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.controlsLayout.setContentsMargins(9, 9, 9, 9)
        self.voltageLimitButton = QPushButton(self.centralwidget)
        self.voltageLimitButton.setObjectName(u"voltageLimitButton")
        self.voltageLimitButton.setEnabled(False)

        self.controlsLayout.addWidget(self.voltageLimitButton)

        self.currentLimitButton = QPushButton(self.centralwidget)
        self.currentLimitButton.setObjectName(u"currentLimitButton")
        self.currentLimitButton.setEnabled(False)

        self.controlsLayout.addWidget(self.currentLimitButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.controlsLayout.addItem(self.horizontalSpacer_2)

        self.ovpButton = QPushButton(self.centralwidget)
        self.ovpButton.setObjectName(u"ovpButton")
        self.ovpButton.setEnabled(False)
        icon1 = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.ovpButton.setIcon(icon1)
        self.ovpButton.setCheckable(True)

        self.controlsLayout.addWidget(self.ovpButton)

        self.ocpButton = QPushButton(self.centralwidget)
        self.ocpButton.setObjectName(u"ocpButton")
        self.ocpButton.setEnabled(False)
        self.ocpButton.setIcon(icon1)
        self.ocpButton.setCheckable(True)

        self.controlsLayout.addWidget(self.ocpButton)

        self.powerButton = QPushButton(self.centralwidget)
        self.powerButton.setObjectName(u"powerButton")
        self.powerButton.setEnabled(False)
        icon2 = QIcon(QIcon.fromTheme(u"system-shutdown"))
        self.powerButton.setIcon(icon2)
        self.powerButton.setCheckable(True)
        self.powerButton.setChecked(False)

        self.controlsLayout.addWidget(self.powerButton)


        self.mainLayout.addLayout(self.controlsLayout)


        self.verticalLayout_4.addLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 623, 33))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuView.addAction(self.actionM_buttons)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionM_buttons.toggled.connect(self.memoryButtonWidget.setVisible)
        self.actionQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PSUcontrol", None))
        self.actionM_buttons.setText(QCoreApplication.translate("MainWindow", u"Show PSU memory slot controls", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.voltageOutputLabel.setProperty(u"text", "")
        self.voltageOutputLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"88.88", None))
        self.currentOutputLabel.setProperty(u"text", "")
        self.currentOutputLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"8.888", None))
        self.powerOutputLabel.setProperty(u"text", "")
        self.powerOutputLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"888.8", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"NOT CONNECTED", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.indicatorOvp.setProperty(u"text", QCoreApplication.translate("MainWindow", u"OVP", None))
        self.indicatorOcp.setProperty(u"text", QCoreApplication.translate("MainWindow", u"OCP", None))
        self.indicatorCc.setProperty(u"text", QCoreApplication.translate("MainWindow", u"C.C", None))
        self.indicatorCv.setProperty(u"text", QCoreApplication.translate("MainWindow", u"C.V", None))
        self.indicatorLabel.setProperty(u"text", QCoreApplication.translate("MainWindow", u"OUT", None))
        self.m1Button.setText(QCoreApplication.translate("MainWindow", u"M1", None))
        self.m2Button.setText(QCoreApplication.translate("MainWindow", u"M2", None))
        self.m3Button.setText(QCoreApplication.translate("MainWindow", u"M3", None))
        self.m4Button.setText(QCoreApplication.translate("MainWindow", u"M4", None))
        self.m5Button.setText(QCoreApplication.translate("MainWindow", u"M5", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"SAV", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("MainWindow", u"NO DEVICE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SET LIMIT", None))
        self.voltageLimitLabel.setProperty(u"text", "")
        self.voltageLimitLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"88.88", None))
        self.currentLimitLabel.setProperty(u"text", "")
        self.currentLimitLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"8.888", None))
        self.powerLimitLabel.setProperty(u"text", "")
        self.powerLimitLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"888.8", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.voltageLimitButton.setText(QCoreApplication.translate("MainWindow", u"Voltage limit", None))
        self.currentLimitButton.setText(QCoreApplication.translate("MainWindow", u"Current limit", None))
        self.ovpButton.setText(QCoreApplication.translate("MainWindow", u"OVP", None))
        self.ocpButton.setText(QCoreApplication.translate("MainWindow", u"OCP", None))
        self.powerButton.setText(QCoreApplication.translate("MainWindow", u"POWER", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


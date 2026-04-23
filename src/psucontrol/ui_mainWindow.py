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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from indicatorlabel import IndicatorLabel
from lcdlabel import LcdLabel
import psucontrol.rc_gui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 364)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.serialPortSettingsLayout = QHBoxLayout()
        self.serialPortSettingsLayout.setObjectName(u"serialPortSettingsLayout")
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

        self.preferencesButton = QPushButton(self.centralwidget)
        self.preferencesButton.setObjectName(u"preferencesButton")
        sizePolicy.setHeightForWidth(self.preferencesButton.sizePolicy().hasHeightForWidth())
        self.preferencesButton.setSizePolicy(sizePolicy)
        icon1 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.preferencesButton.setIcon(icon1)

        self.serialPortSettingsLayout.addWidget(self.preferencesButton)

        self.aboutButton = QPushButton(self.centralwidget)
        self.aboutButton.setObjectName(u"aboutButton")
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(u"dialog-information"))
        self.aboutButton.setIcon(icon2)

        self.serialPortSettingsLayout.addWidget(self.aboutButton)


        self.mainLayout.addLayout(self.serialPortSettingsLayout)

        self.lcdLayout = QHBoxLayout()
        self.lcdLayout.setSpacing(0)
        self.lcdLayout.setObjectName(u"lcdLayout")
        self.memoryButtonsFrame = QFrame(self.centralwidget)
        self.memoryButtonsFrame.setObjectName(u"memoryButtonsFrame")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.memoryButtonsFrame.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.memoryButtonsFrame.setFont(font1)
        self.memoryButtonsFrame.setAutoFillBackground(True)
        self.memoryButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.memoryButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.memoryButtonsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 54, 6, -1)
        self.label_4 = QLabel(self.memoryButtonsFrame)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(32)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_3 = QLabel(self.memoryButtonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_6 = QLabel(self.memoryButtonsFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.verticalLayout_7)


        self.lcdLayout.addWidget(self.memoryButtonsFrame)

        self.lcdFrame = QFrame(self.centralwidget)
        self.lcdFrame.setObjectName(u"lcdFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lcdFrame.sizePolicy().hasHeightForWidth())
        self.lcdFrame.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        brush1 = QBrush(QColor(166, 169, 159, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.lcdFrame.setPalette(palette1)
        self.lcdFrame.setAutoFillBackground(True)
        self.lcdFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.lcdFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.connectionStatusLayout = QHBoxLayout()
        self.connectionStatusLayout.setObjectName(u"connectionStatusLayout")
        self.connectionStatusLayout.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.manufacturerLabel = QLabel(self.lcdFrame)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.manufacturerLabel.sizePolicy().hasHeightForWidth())
        self.manufacturerLabel.setSizePolicy(sizePolicy3)
        self.manufacturerLabel.setFont(font1)
        self.manufacturerLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.manufacturerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.manufacturerLabel)

        self.label_5 = QLabel(self.lcdFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)


        self.connectionStatusLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.modelLabel = QLabel(self.lcdFrame)
        self.modelLabel.setObjectName(u"modelLabel")
        sizePolicy3.setHeightForWidth(self.modelLabel.sizePolicy().hasHeightForWidth())
        self.modelLabel.setSizePolicy(sizePolicy3)
        self.modelLabel.setFont(font1)
        self.modelLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.modelLabel.setScaledContents(False)
        self.modelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.modelLabel)

        self.label = QLabel(self.lcdFrame)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)


        self.connectionStatusLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.connectionStatusLayout)

        self.connectionAndNumbersSeparator = QFrame(self.lcdFrame)
        self.connectionAndNumbersSeparator.setObjectName(u"connectionAndNumbersSeparator")
        self.connectionAndNumbersSeparator.setFrameShape(QFrame.Shape.HLine)
        self.connectionAndNumbersSeparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.connectionAndNumbersSeparator)

        self.numbersLayout = QHBoxLayout()
        self.numbersLayout.setSpacing(6)
        self.numbersLayout.setObjectName(u"numbersLayout")
        self.numbersLayout.setContentsMargins(6, 0, 6, 0)
        self.setLimitLayout = QVBoxLayout()
        self.setLimitLayout.setSpacing(0)
        self.setLimitLayout.setObjectName(u"setLimitLayout")
        self.voltageLimitLabel = LcdLabel(self.lcdFrame)
        self.voltageLimitLabel.setObjectName(u"voltageLimitLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.voltageLimitLabel.sizePolicy().hasHeightForWidth())
        self.voltageLimitLabel.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamilies([u"DSEG7 Classic Mini"])
        font3.setPointSize(32)
        font3.setBold(True)
        self.voltageLimitLabel.setFont(font3)
        self.voltageLimitLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.voltageLimitLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.voltageLimitLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.setLimitLayout.addWidget(self.voltageLimitLabel)

        self.currentLimitLabel = LcdLabel(self.lcdFrame)
        self.currentLimitLabel.setObjectName(u"currentLimitLabel")
        self.currentLimitLabel.setFont(font3)
        self.currentLimitLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.currentLimitLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.currentLimitLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.setLimitLayout.addWidget(self.currentLimitLabel)

        self.powerLimitLabel = LcdLabel(self.lcdFrame)
        self.powerLimitLabel.setObjectName(u"powerLimitLabel")
        self.powerLimitLabel.setFont(font3)
        self.powerLimitLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.powerLimitLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.powerLimitLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.setLimitLayout.addWidget(self.powerLimitLabel)


        self.numbersLayout.addLayout(self.setLimitLayout)

        self.line = QFrame(self.lcdFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.numbersLayout.addWidget(self.line)

        self.outputLayout = QVBoxLayout()
        self.outputLayout.setSpacing(0)
        self.outputLayout.setObjectName(u"outputLayout")
        self.voltageOutputLabel = LcdLabel(self.lcdFrame)
        self.voltageOutputLabel.setObjectName(u"voltageOutputLabel")
        self.voltageOutputLabel.setFont(font3)
        self.voltageOutputLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.voltageOutputLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.voltageOutputLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.outputLayout.addWidget(self.voltageOutputLabel)

        self.currentOutputLabel = LcdLabel(self.lcdFrame)
        self.currentOutputLabel.setObjectName(u"currentOutputLabel")
        self.currentOutputLabel.setFont(font3)
        self.currentOutputLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.currentOutputLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.currentOutputLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.outputLayout.addWidget(self.currentOutputLabel)

        self.powerOutputLabel = LcdLabel(self.lcdFrame)
        self.powerOutputLabel.setObjectName(u"powerOutputLabel")
        self.powerOutputLabel.setFont(font3)
        self.powerOutputLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignCenter)
        self.powerOutputLabel.setProperty(u"foregroundColor", QColor(0, 0, 0))
        self.powerOutputLabel.setProperty(u"backgroundColor", QColor(156, 159, 159))

        self.outputLayout.addWidget(self.powerOutputLabel)


        self.numbersLayout.addLayout(self.outputLayout)

        self.numbersLayout.setStretch(0, 1)
        self.numbersLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.numbersLayout)

        self.verticalLayout.setStretch(2, 1)

        self.lcdLayout.addWidget(self.lcdFrame)

        self.statusIndicatorsFrame = QFrame(self.centralwidget)
        self.statusIndicatorsFrame.setObjectName(u"statusIndicatorsFrame")
        sizePolicy4.setHeightForWidth(self.statusIndicatorsFrame.sizePolicy().hasHeightForWidth())
        self.statusIndicatorsFrame.setSizePolicy(sizePolicy4)
        palette2 = QPalette()
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.statusIndicatorsFrame.setPalette(palette2)
        self.statusIndicatorsFrame.setFont(font1)
        self.statusIndicatorsFrame.setAutoFillBackground(True)
        self.statusIndicatorsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusIndicatorsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.statusIndicatorsFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.indicatorOvp = IndicatorLabel(self.statusIndicatorsFrame)
        self.indicatorOvp.setObjectName(u"indicatorOvp")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.indicatorOvp.sizePolicy().hasHeightForWidth())
        self.indicatorOvp.setSizePolicy(sizePolicy5)
        self.indicatorOvp.setFont(font1)
        self.indicatorOvp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.indicatorOvp.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.indicatorOvp.setProperty(u"checked", False)
        self.indicatorOvp.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorOvp.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorOvp.setProperty(u"spacing", 6)

        self.verticalLayout_5.addWidget(self.indicatorOvp)

        self.indicatorOcp = IndicatorLabel(self.statusIndicatorsFrame)
        self.indicatorOcp.setObjectName(u"indicatorOcp")
        sizePolicy3.setHeightForWidth(self.indicatorOcp.sizePolicy().hasHeightForWidth())
        self.indicatorOcp.setSizePolicy(sizePolicy3)
        self.indicatorOcp.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorOcp.setProperty(u"checked", False)
        self.indicatorOcp.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorOcp.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorOcp.setProperty(u"spacing", 6)

        self.verticalLayout_5.addWidget(self.indicatorOcp)

        self.indicatorCc = IndicatorLabel(self.statusIndicatorsFrame)
        self.indicatorCc.setObjectName(u"indicatorCc")
        sizePolicy3.setHeightForWidth(self.indicatorCc.sizePolicy().hasHeightForWidth())
        self.indicatorCc.setSizePolicy(sizePolicy3)
        self.indicatorCc.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorCc.setProperty(u"checked", False)
        self.indicatorCc.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorCc.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorCc.setProperty(u"spacing", 6)

        self.verticalLayout_5.addWidget(self.indicatorCc)

        self.indicatorCv = IndicatorLabel(self.statusIndicatorsFrame)
        self.indicatorCv.setObjectName(u"indicatorCv")
        sizePolicy3.setHeightForWidth(self.indicatorCv.sizePolicy().hasHeightForWidth())
        self.indicatorCv.setSizePolicy(sizePolicy3)
        self.indicatorCv.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorCv.setProperty(u"checked", False)
        self.indicatorCv.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorCv.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorCv.setProperty(u"spacing", 6)

        self.verticalLayout_5.addWidget(self.indicatorCv)

        self.indicatorLabel = IndicatorLabel(self.statusIndicatorsFrame)
        self.indicatorLabel.setObjectName(u"indicatorLabel")
        sizePolicy3.setHeightForWidth(self.indicatorLabel.sizePolicy().hasHeightForWidth())
        self.indicatorLabel.setSizePolicy(sizePolicy3)
        self.indicatorLabel.setProperty(u"alignment", Qt.AlignmentFlag.AlignLeading)
        self.indicatorLabel.setProperty(u"checked", False)
        self.indicatorLabel.setProperty(u"on_color", QColor(255, 0, 0))
        self.indicatorLabel.setProperty(u"off_color", QColor(50, 0, 0))
        self.indicatorLabel.setProperty(u"spacing", 6)

        self.verticalLayout_5.addWidget(self.indicatorLabel)


        self.lcdLayout.addWidget(self.statusIndicatorsFrame)

        self.lcdLayout.setStretch(1, 1)

        self.mainLayout.addLayout(self.lcdLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.voltageLimitButton = QPushButton(self.centralwidget)
        self.voltageLimitButton.setObjectName(u"voltageLimitButton")
        self.voltageLimitButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.voltageLimitButton)

        self.currentLimitButton = QPushButton(self.centralwidget)
        self.currentLimitButton.setObjectName(u"currentLimitButton")
        self.currentLimitButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.currentLimitButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.ovpButton = QPushButton(self.centralwidget)
        self.ovpButton.setObjectName(u"ovpButton")
        self.ovpButton.setEnabled(False)
        icon3 = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.ovpButton.setIcon(icon3)
        self.ovpButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.ovpButton)

        self.ocpButton = QPushButton(self.centralwidget)
        self.ocpButton.setObjectName(u"ocpButton")
        self.ocpButton.setEnabled(False)
        self.ocpButton.setIcon(icon3)
        self.ocpButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.ocpButton)

        self.powerButton = QPushButton(self.centralwidget)
        self.powerButton.setObjectName(u"powerButton")
        self.powerButton.setEnabled(False)
        icon4 = QIcon(QIcon.fromTheme(u"system-shutdown"))
        self.powerButton.setIcon(icon4)
        self.powerButton.setCheckable(True)
        self.powerButton.setChecked(False)

        self.horizontalLayout.addWidget(self.powerButton)


        self.mainLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PSUcontrol", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.preferencesButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Preferences</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preferencesButton.setText("")
#if QT_CONFIG(tooltip)
        self.aboutButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>About</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.aboutButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("MainWindow", u"NO DEVICE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SET LIMIT", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"NOT CONNECTED", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.voltageLimitLabel.setProperty(u"text", "")
        self.voltageLimitLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"88.88", None))
        self.currentLimitLabel.setProperty(u"text", "")
        self.currentLimitLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"8.888", None))
        self.powerLimitLabel.setProperty(u"text", "")
        self.powerLimitLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"888.8", None))
        self.voltageOutputLabel.setProperty(u"text", "")
        self.voltageOutputLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"88.88", None))
        self.currentOutputLabel.setProperty(u"text", "")
        self.currentOutputLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"8.888", None))
        self.powerOutputLabel.setProperty(u"text", "")
        self.powerOutputLabel.setProperty(u"backgroundText", QCoreApplication.translate("MainWindow", u"888.8", None))
        self.indicatorOvp.setProperty(u"text", QCoreApplication.translate("MainWindow", u"OVP", None))
        self.indicatorOcp.setProperty(u"text", QCoreApplication.translate("MainWindow", u"OCP", None))
        self.indicatorCc.setProperty(u"text", QCoreApplication.translate("MainWindow", u"C.C", None))
        self.indicatorCv.setProperty(u"text", QCoreApplication.translate("MainWindow", u"C.V", None))
        self.indicatorLabel.setProperty(u"text", QCoreApplication.translate("MainWindow", u"OUT", None))
        self.voltageLimitButton.setText(QCoreApplication.translate("MainWindow", u"Voltage limit", None))
        self.currentLimitButton.setText(QCoreApplication.translate("MainWindow", u"Current limit", None))
        self.ovpButton.setText(QCoreApplication.translate("MainWindow", u"OVP", None))
        self.ocpButton.setText(QCoreApplication.translate("MainWindow", u"OCP", None))
        self.powerButton.setText(QCoreApplication.translate("MainWindow", u"POWER", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferencesDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.resize(563, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreferencesDialog.sizePolicy().hasHeightForWidth())
        PreferencesDialog.setSizePolicy(sizePolicy)
        PreferencesDialog.setMinimumSize(QSize(560, 540))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        PreferencesDialog.setWindowIcon(icon)
        PreferencesDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 18, -1, -1)
        self.label_2 = QLabel(PreferencesDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(PreferencesDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.CustomPortsList = QListWidget(PreferencesDialog)
        self.CustomPortsList.setObjectName(u"CustomPortsList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CustomPortsList.sizePolicy().hasHeightForWidth())
        self.CustomPortsList.setSizePolicy(sizePolicy2)
        self.CustomPortsList.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.CustomPortsList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(PreferencesDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.AddButton = QPushButton(PreferencesDialog)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.AddButton)

        self.RemoveButton = QPushButton(PreferencesDialog)
        self.RemoveButton.setObjectName(u"RemoveButton")
        self.RemoveButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.RemoveButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept)
        self.buttonBox.rejected.connect(PreferencesDialog.reject)

        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Preferences", None))
        self.label_2.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Here you can enter custom serial-port entries, like e.g. if the port you want to use just isn't currently available or it's not found automatically by the application.</p><p>Another option is the more varied options offered by the PySerial-library that this application uses underneath, like e.g. an RFC2217-compliant serial-port over the network:</p><p><span style=\" font-style:italic;\">rfc2217://yourserialdeviceiphere:2013</span></p><p>Or a plain TCP-socket:</p><p><span style=\" font-style:italic;\">socket://serialdevice.lan:2012</span></p><p>See <a href=\"https://pyserial.readthedocs.io/en/latest/url_handlers.html\"><span style=\" text-decoration: underline; color:#ff95ca;\">https://pyserial.readthedocs.io/en/latest/url_handlers.html</span></a> for more details.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("PreferencesDialog", u"Custom serial ports and connections:", None))
#if QT_CONFIG(tooltip)
        self.CustomPortsList.setToolTip(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Here you can enter custom serial-port entries, like e.g. if the port you want to use just isn't currently available or it's not found automatically by the application.</p><p>Another option is the more varied options offered by the PySerial-library that this application uses underneath, like e.g. an RFC2217-compliant serial-port over the network:</p><p><span style=\" font-style:italic;\">rfc2217://yourserialdeviceiphere:2013</span></p><p>Or a plain TCP-socket:</p><p><span style=\" font-style:italic;\">socket://serialdevice.lan:2012</span></p><p>See <a href=\"https://pyserial.readthedocs.io/en/latest/url_handlers.html\"><span style=\" text-decoration: underline; color:#ff95ca;\">https://pyserial.readthedocs.io/en/latest/url_handlers.html</span></a> for more details.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Here you can enter custom serial-port entries, like e.g. if the port you want to use just isn't currently available or it's not found automatically by the application.</p><p>Another option is the more varied options offered by the PySerial-library that this application uses underneath, like e.g. an RFC2217-compliant serial-port over the network:</p><p><span style=\" font-style:italic;\">rfc2217://yourserialdeviceiphere:2013</span></p><p>Or a plain TCP-socket:</p><p><span style=\" font-style:italic;\">socket://serialdevice.lan:2012</span></p><p>See <a href=\"https://pyserial.readthedocs.io/en/latest/url_handlers.html\"><span style=\" text-decoration: underline; color:#ff95ca;\">https://pyserial.readthedocs.io/en/latest/url_handlers.html</span></a> for more details.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.AddButton.setText(QCoreApplication.translate("PreferencesDialog", u"Add to list", None))
        self.RemoveButton.setText(QCoreApplication.translate("PreferencesDialog", u"Remove from list", None))
    # retranslateUi


from .__init__ import __version__
import random
import sys
import time
from PySide6 import QtWidgets, QtSerialPort, QtGui
import serial
import psucontrol.rc_gui  # noqa: F401
from psucontrol.ui_mainWindow import Ui_MainWindow
from psucontrol.ui_limitDialog import Ui_LimitDialog
from psucontrol.ui_errorDialog import Ui_ErrorDialog
from psucontrol.ui_preferencesDialog import Ui_PreferencesDialog
from psucontrol.ui_aboutDialog import Ui_AboutDialog
from PySide6.QtCore import QObject, QThread, QTimer, Signal, Slot, Qt
from .protocol import PsuDevice
from .protocol import CcCvMode
from xdg_base_dirs import xdg_config_home
import json
from indicatorlabel import IndicatorLabel  # noqa: F401
from lcdlabel import LcdLabel  # noqa: F401


def readConfig():
    configPath = xdg_config_home() / "psucontrol"
    configPath.mkdir(parents=True, exist_ok=True)
    config = {"customSerialPorts": [], "selectedSerialPort": ""}
    if (configPath / "config.json").exists():
        with open(configPath / "config.json", "r") as f:
            config.update(json.load(f))
            config["customSerialPorts"] = [
                port for port in config["customSerialPorts"] if port.strip()
            ]
    return config


def saveConfig(configData: dict):
    if readConfig() != configData:
        configPath = xdg_config_home() / "psucontrol"
        with open(configPath / "config.json", "w") as f:
            json.dump(configData, f)


class MainWindow(QtWidgets.QMainWindow):
    settingsChange: Signal = Signal(str, object)
    connectDevice: Signal = Signal(str)
    disconnectDevice: Signal = Signal()

    def __init__(self, configData: dict, simulate: bool = False):
        super(MainWindow, self).__init__()
        self._previousData = None
        self._configData = configData
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtGui.QFontDatabase.addApplicationFont(":/fonts/7seg.ttf")
        QtGui.QFontDatabase.addApplicationFont(":/fonts/14seg.ttf")
        serial_port_info = QtSerialPort.QSerialPortInfo()
        available_ports = configData["customSerialPorts"] + [
            port.portName() for port in serial_port_info.availablePorts()
        ]
        available_ports = list(dict.fromkeys(available_ports))
        self.ui.serialPortBox.addItems(available_ports)
        if configData["selectedSerialPort"] in available_ports:
            self.ui.serialPortBox.setCurrentText(configData["selectedSerialPort"])
        self.ui.connectButton.clicked.connect(self.connectButtonHandler)

        self.psuThread = QThread()
        self.psuWorker = DeviceWorker(simulate)
        self.psuWorker.moveToThread(self.psuThread)
        self.psuWorker.connectionStatusChanged.connect(self.updateStatus)
        self.psuWorker.updatedData.connect(self.updateData)

        self.ui.powerButton.clicked.connect(self.powerButtonHandler)
        self.ui.voltageLimitButton.clicked.connect(self.voltageLimitButtonHandler)
        self.ui.currentLimitButton.clicked.connect(self.currentLimitButtonHandler)

        self.psuWorker.busy.connect(self.busySignalHandler)
        self.settingsChange.connect(self.psuWorker.settingsChangeHandler)
        self.connectDevice.connect(self.psuWorker.connect_device)
        self.disconnectDevice.connect(self.psuWorker.disconnect_device)
        self.ui.ocpButton.clicked.connect(self.ocpButtonHandler)
        self.ui.ovpButton.clicked.connect(self.ovpButtonHandler)

        self.ui.serialPortBox.currentTextChanged.connect(self.serialPortBoxChanged)
        self.ui.preferencesButton.clicked.connect(self.preferencesDialogButtonHandler)
        self.ui.aboutButton.clicked.connect(self.aboutDialogHandler)

        self.psuWorker.psuError.connect(self.errorDialogHandler)
        """
        PreferencesDialog
        """
        self._preferencesDialog = QtWidgets.QDialog()
        self._preferencesDialogUi = Ui_PreferencesDialog()
        self._preferencesDialogUi.setupUi(self._preferencesDialog)
        self._preferencesDialogUi.AddButton.clicked.connect(
            self.preferencesDialogAddButtonHandler
        )
        self._preferencesDialogUi.RemoveButton.clicked.connect(
            self.preferencesDialogRemoveButtonHandler
        )
        self._preferencesDialogUi.lineEdit.textChanged.connect(
            self.preferencesDialoglineEditHandler
        )
        self._preferencesDialogUi.CustomPortsList.itemSelectionChanged.connect(
            self.preferencesDialogCustomPortsListHandler
        )

        if "windowPosition" in configData:
            self.move(*configData["windowPosition"])
        self.psuThread.start()

    def aboutDialogHandler(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_AboutDialog()
        ui.setupUi(dialog)
        dialog.exec_()

    def preferencesDialogCustomPortsListHandler(self):
        self._preferencesDialogUi.lineEdit.setText(
            self._preferencesDialogUi.CustomPortsList.currentItem().text()
        )

    def preferencesDialogButtonHandler(self):
        self._preferencesDialogUi.CustomPortsList.clear()
        self._preferencesDialogUi.CustomPortsList.addItems(
            self._configData["customSerialPorts"]
        )
        if self._preferencesDialog.exec_():
            items = [
                self._preferencesDialogUi.CustomPortsList.item(x).text().strip()
                for x in range(self._preferencesDialogUi.CustomPortsList.count())
            ]
            self._configData["customSerialPorts"] = items.copy()
            serial_port_info = QtSerialPort.QSerialPortInfo()
            items += [port.portName() for port in serial_port_info.availablePorts()]
            items = list(dict.fromkeys(items))
            currentPort = self._configData["selectedSerialPort"]
            self.ui.serialPortBox.clear()
            if currentPort and currentPort not in items:
                items.append(currentPort)
            self.ui.serialPortBox.addItems(items)
            if currentPort in items:
                self.ui.serialPortBox.setCurrentText(currentPort)

    def preferencesDialogAddButtonHandler(self):
        if (
            self._preferencesDialogUi.lineEdit.text().strip()
            and self._preferencesDialogUi.lineEdit.text().strip()
            not in self._configData["customSerialPorts"]
        ):
            self._preferencesDialogUi.CustomPortsList.addItem(
                self._preferencesDialogUi.lineEdit.text().strip()
            )

    def preferencesDialogRemoveButtonHandler(self):
        self._preferencesDialogUi.CustomPortsList.takeItem(
            self._preferencesDialogUi.CustomPortsList.row(
                self._preferencesDialogUi.CustomPortsList.findItems(
                    self._preferencesDialogUi.lineEdit.text().strip(),
                    Qt.MatchFlag.MatchExactly,
                )[0]
            )
        )
        self._preferencesDialogUi.lineEdit.setText("")

    def preferencesDialoglineEditHandler(self, text):
        if text.strip():
            self._preferencesDialogUi.AddButton.setEnabled(True)
            if (
                self._preferencesDialogUi.CustomPortsList.findItems(
                    text.strip(),
                    Qt.MatchFlag.MatchExactly,
                )
                and self._preferencesDialogUi.CustomPortsList.findItems(
                    text.strip(),
                    Qt.MatchFlag.MatchExactly,
                )[0]
            ):
                self._preferencesDialogUi.RemoveButton.setEnabled(True)
            else:
                self._preferencesDialogUi.RemoveButton.setEnabled(False)
        else:
            self._preferencesDialogUi.AddButton.setEnabled(False)
            self._preferencesDialogUi.RemoveButton.setEnabled(False)

    def errorDialogHandler(self, message: str):
        dialog = QtWidgets.QDialog()
        ui = Ui_ErrorDialog()
        ui.setupUi(dialog)
        ui.label.setText(message)
        dialog.exec_()

    def serialPortBoxChanged(self, text):
        self._configData["selectedSerialPort"] = text

    def closeEvent(self, event):
        if self.psuThread.isRunning():
            self.psuWorker.exitPollEarly = True
            self.disconnectDevice.emit()
            while self.psuWorker.connected:
                time.sleep(0.01)
            while self.psuWorker.timerActive:
                time.sleep(0.01)
            self.psuThread.quit()
            if not self.psuThread.wait(2000):
                self.psuThread.terminate()
        self._configData["windowPosition"] = (self.x(), self.y())
        saveConfig(self._configData)
        event.accept()

    def resetUi(self):
        self.ui.powerButton.setChecked(False)
        self.ui.powerButton.setEnabled(False)
        self.ui.voltageLimitButton.setEnabled(False)
        self.ui.currentLimitButton.setEnabled(False)
        self.ui.ocpButton.setEnabled(False)
        self.ui.ovpButton.setEnabled(False)
        self.ui.indicatorCc.setChecked(False)
        self.ui.indicatorCv.setChecked(False)
        self.ui.indicatorLabel.setChecked(False)
        self.ui.indicatorOcp.setChecked(False)
        self.ui.indicatorOvp.setChecked(False)
        self.ui.voltageLimitLabel.setText("")
        self.ui.currentLimitLabel.setText("")
        self.ui.powerLimitLabel.setText("")
        self.ui.voltageOutputLabel.setText("")
        self.ui.currentOutputLabel.setText("")
        self.ui.powerOutputLabel.setText("")
        self.ui.manufacturerLabel.setText("NO DEVICE")
        self.ui.modelLabel.setText("NOT CONNECTED")
        self.ui.connectButton.setText("Connect")
        self.ui.connectButton.setEnabled(True)
        self.ui.serialPortBox.setEnabled(True)

    @Slot()
    def busySignalHandler(self, busy: bool):
        if busy:
            self.ui.powerButton.setEnabled(False)
            self.ui.voltageLimitButton.setEnabled(False)
            self.ui.currentLimitButton.setEnabled(False)
            self.ui.ovpButton.setEnabled(False)
            self.ui.ocpButton.setEnabled(False)
        else:
            self.ui.powerButton.setEnabled(True)
            self.ui.voltageLimitButton.setEnabled(True)
            self.ui.currentLimitButton.setEnabled(True)
            self.ui.ovpButton.setEnabled(True)
            self.ui.ocpButton.setEnabled(True)

    def voltageLimitButtonHandler(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_LimitDialog()
        ui.setupUi(dialog)
        ui.doubleSpinBox.setMaximum(self._maximumVoltage)
        ui.doubleSpinBox.setDecimals(2)
        ui.doubleSpinBox.setSingleStep(0.01)
        if self._previousData:
            ui.doubleSpinBox.setValue(self._previousData["voltage"])
        if dialog.exec_():
            self.busySignalHandler(True)
            self.psuWorker.exitPollEarly = True
            self.settingsChange.emit("setVoltage", ui.doubleSpinBox.value())

    def currentLimitButtonHandler(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_LimitDialog()
        ui.setupUi(dialog)
        ui.doubleSpinBox.setMaximum(self._maximumCurrent)
        ui.doubleSpinBox.setDecimals(3)
        ui.doubleSpinBox.setSingleStep(0.001)
        if self._previousData:
            ui.doubleSpinBox.setValue(self._previousData["current"])
        if dialog.exec_():
            self.busySignalHandler(True)
            self.psuWorker.exitPollEarly = True
            self.settingsChange.emit("setCurrent", ui.doubleSpinBox.value())

    def connectButtonHandler(self):
        if self.ui.connectButton.text() == "Disconnect":
            self.psuWorker.exitPollEarly = True
            self.disconnectDevice.emit()
        else:
            port = self.ui.serialPortBox.currentText()
            self.connectDevice.emit(port)

    def powerButtonHandler(self, checked: bool):
        self.busySignalHandler(True)
        self.psuWorker.exitPollEarly = True
        self.settingsChange.emit("setOutput", checked)

    def ovpButtonHandler(self, checked: bool):
        self.busySignalHandler(True)
        self.psuWorker.exitPollEarly = True
        self.settingsChange.emit("setOVP", checked)
        self.ui.indicatorOvp.setChecked(checked)

    def ocpButtonHandler(self, checked: bool):
        self.busySignalHandler(True)
        self.psuWorker.exitPollEarly = True
        self.settingsChange.emit("setOCP", checked)
        self.ui.indicatorOcp.setChecked(checked)

    def updateStatus(self, status: str, data: tuple):
        if status == "Connecting...":
            self.ui.connectButton.setText("Connecting...")
            self.ui.connectButton.setEnabled(False)
            self.ui.serialPortBox.setEnabled(False)
        elif status == "Connected":
            self.ui.connectButton.setText("Disconnect")
            self.ui.connectButton.setEnabled(True)
            self.ui.serialPortBox.setEnabled(False)
            self.ui.powerButton.setEnabled(True)
            self.ui.powerButton.setChecked(False)
            if data:
                self.ui.manufacturerLabel.setText(data[0])
                self.ui.modelLabel.setText(data[1])
                self._manufacturer = data[0]
                self._model = data[1]
                self._version = data[2]
                self._maximumVoltage = data[3]
                self._maximumCurrent = data[4]
            self.ui.voltageLimitButton.setEnabled(True)
            self.ui.currentLimitButton.setEnabled(True)
            self.ui.ocpButton.setEnabled(True)
            self.ui.ovpButton.setEnabled(True)
        elif status == "Disconnected":
            self.resetUi()
            self._previousData = None

    def updateData(self, data: dict):
        powerLimitLabelNeedsUpdate = False
        powerOutputLabelNeedsUpdate = False
        if not self._previousData or self._previousData["voltage"] != data["voltage"]:
            text = f"{data['voltage']:.2f}"
            self.ui.voltageLimitLabel.setText(f"{text:{'!'}>5}")
            powerLimitLabelNeedsUpdate = True
        if not self._previousData or self._previousData["current"] != data["current"]:
            text = f"{data['current']:.3f}"
            self.ui.currentLimitLabel.setText(f"{text:{'!'}>5}")
            powerLimitLabelNeedsUpdate = True
        if (
            not self._previousData
            or self._previousData["voltageOutput"] != data["voltageOutput"]
        ):
            text = f"{data['voltageOutput']:.2f}"
            self.ui.voltageOutputLabel.setText(f"{text:{'!'}>5}")
            powerOutputLabelNeedsUpdate = True
        if (
            not self._previousData
            or self._previousData["currentOutput"] != data["currentOutput"]
        ):
            text = f"{data['currentOutput']:.3f}"
            self.ui.currentOutputLabel.setText(f"{text:{'!'}>5}")
            powerOutputLabelNeedsUpdate = True
        if (
            not self._previousData
            or self._previousData["status"]["output"] != data["status"]["output"]
        ):
            self.ui.powerButton.setChecked(data["status"]["output"])
            self.ui.indicatorLabel.setChecked(data["status"]["output"])
        if (
            not self._previousData
            or self._previousData["status"]["mode"] != data["status"]["mode"]
        ):
            if data["status"]["mode"] == CcCvMode.CC:
                self.ui.indicatorCc.setChecked(True)
                self.ui.indicatorCv.setChecked(False)
            else:
                self.ui.indicatorCc.setChecked(False)
                self.ui.indicatorCv.setChecked(True)
        if powerLimitLabelNeedsUpdate:
            text = f"{data['voltage'] * data['current']:.1f}"
            self.ui.powerLimitLabel.setText(f"{text:{'!'}>5}")
        if powerOutputLabelNeedsUpdate:
            text = f"{data['voltageOutput'] * data['currentOutput']:.1f}"
            self.ui.powerOutputLabel.setText(f"{text:{'!'}>5}")
        self._previousData = data


class DeviceWorker(QObject):
    updatedData = Signal(dict)
    connectionStatusChanged = Signal(str, tuple)
    psuError = Signal(str)
    _psu: PsuDevice
    busy = Signal(bool)
    exitPollEarly: bool
    _busyPolling: bool
    _simulatePsu: bool
    _simulatedPsuConnected: bool
    _simulatedPsuOutput: bool
    _simulatedVoltageLimit: float
    _simulatedCurrentLimit: float

    def __init__(self, simulate: bool = False):
        super().__init__()
        self._psu = PsuDevice(None)
        self._pollingTimer = QTimer(self)
        self._pollingTimer.setInterval(60)
        self._pollingTimer.timeout.connect(self._pollingTimerHandler)
        self.exitPollEarly = False
        self._busyPolling = False
        self._simulatePsu = simulate
        self._updateStatus = False
        self._simulatedPsuConnected = False
        self._simulatedPsuOutput = False
        self._simulatedVoltageLimit = 12.0
        self._simulatedCurrentLimit = 5.0

    def _statusTimerHandler(self):
        self._updateStatus = True

    @property
    def connected(self) -> bool:
        return (
            self._psu.isConnected()
            if not self._simulatePsu
            else self._simulatedPsuConnected
        )

    @property
    def timerActive(self) -> bool:
        return self._pollingTimer.isActive()

    @Slot()
    def connect_device(self, port: str):
        if self.connected:
            return
        self._psu.port = port
        self.connectionStatusChanged.emit("Connecting...", ())
        try:
            if self._simulatePsu:
                self._simulatedPsuConnected = True
                time.sleep(2)
            else:
                self._psu.connect()
        except serial.SerialException as e:
            self.connectionStatusChanged.emit("Disconnected", ())
            self.psuError.emit(str(e))
            return
        except RuntimeError as e:
            self.connectionStatusChanged.emit("Disconnected", ())
            self.psuError.emit(str(e))
            return
        if self._simulatePsu:
            self.connectionStatusChanged.emit(
                "Connected",
                (
                    "FAKEMANUFACTURER",
                    "BENCHPSU",
                    "V3.13",
                    30.0,
                    5.0,
                ),
            )
        else:
            self.connectionStatusChanged.emit(
                "Connected",
                (
                    self._psu.manufacturer,
                    self._psu.model,
                    self._psu.version,
                    self._psu.maximumVoltage,
                    self._psu.maximumCurrent,
                ),
            )

        self.exitPollEarly = False
        self._busyPolling = False
        self._pollingTimer.start()

    @Slot()
    def disconnect_device(self):
        self._pollingTimer.stop()
        self.exitPollEarly = True
        while self._busyPolling:
            time.sleep(0.01)
        if self._simulatePsu:
            self._simulatedPsuConnected = False
        else:
            self._psu.close()
        self.connectionStatusChanged.emit("Disconnected", ())

    @Slot()
    def _pollingTimerHandler(self):
        if not self.connected:
            self.disconnect_device()
            return
        if self.exitPollEarly:
            return
        self._busyPolling = True
        if self._simulatePsu:
            for x in range(5):
                if self.exitPollEarly:
                    self._busyPolling = False
                    return
                time.sleep(0.1)
            psuData = {
                "voltage": self._simulatedVoltageLimit,
                "current": self._simulatedCurrentLimit,
                "voltageOutput": self._simulatedVoltageLimit
                if self._simulatedPsuOutput
                else 0.00,
                "currentOutput": (random.random() * 0.2 + 0.8)
                * self._simulatedCurrentLimit
                if self._simulatedPsuOutput
                else 0.00,
                "status": {
                    "mode": CcCvMode.CV,
                    "tracking": 0,
                    "beep": False,
                    "lock": False,
                    "output": self._simulatedPsuOutput,
                },
            }
            self.updatedData.emit(psuData)
            self._busyPolling = False
            return
        else:
            try:
                psuData = {}
                properties = [
                    "voltage",
                    "current",
                    "voltageOutput",
                    "currentOutput",
                    "status",
                ]
                for property in properties:
                    if self.exitPollEarly:
                        return
                    value = getattr(self._psu, property)
                    psuData[property] = value
                self.updatedData.emit(psuData)
            except ConnectionError:
                self.disconnect_device()
            except TimeoutError:
                self.disconnect_device()
                self.psuError.emit("Timeout communicating with the PSU, disconnecting.")
            finally:
                self._busyPolling = False

    @Slot()
    def settingsChangeHandler(self, functionName: str, value):
        if self._simulatePsu:
            if functionName == "setOutput":
                self._simulatedPsuOutput = value
            elif functionName == "setVoltage":
                self._simulatedVoltageLimit = value
            elif functionName == "setCurrent":
                self._simulatedCurrentLimit = value
            time.sleep(0.3)
        else:
            try:
                psuFunction = getattr(self._psu, functionName)
                psuFunction(value)
            except ConnectionError:
                self.disconnect_device()
            except TimeoutError:
                self.disconnect_device()
                self.psuError.emit("Timeout communicating with the PSU, disconnecting.")
            finally:
                pass
        self.busy.emit(False)
        self.exitPollEarly = False


def main(argv: list[str] | None = None):
    if not argv:
        argv = sys.argv
    simulate = False
    if "--simulate" in argv:
        argv.remove("--simulate")
        simulate = True
    if any(arg in argv for arg in ["--version", "-v"]):
        print(f"psucontrol_gui version {__version__}")
        sys.exit(0)
    configData = readConfig()

    app = QtWidgets.QApplication(argv)

    window = MainWindow(configData, simulate)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)

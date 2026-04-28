import time
import serial
from enum import Enum
import re


class TrackingMode(Enum):
    INDEPENDENT = 0
    SERIES = 1
    PARALLEL = 2


class CcCvMode(Enum):
    CC = 0
    CV = 1


class PsuDevice:
    """Class for controlling a programmable power supply unit (PSU) over a serial connection. This class provides methods for connecting to the PSU, reading and setting voltage and current, and controlling various settings such as output enable, beep, and lock. The class also includes error handling for connection issues and timeouts when communicating with the PSU."""

    def __init__(self, port):
        self._port = port
        self._connection = serial.serial_for_url(
            url=port,
            baudrate=9600,
            timeout=0.5,
            exclusive=True,
            do_not_open=True,
        )
        self._manufacturer = "Unknown"
        self._model = "Unknown"
        self._version = "Unknown"
        self._idn = ""
        self._maximumVoltage = 30.0
        self._maximumCurrent = 5.0

    def connect(self):
        self._connection.open()
        self._identify()

    def _identify(self):
        self._idn = self.identification
        idnRegex = r"^(VELLEMAN|KORAD|RND|STAMOS|TENMA)(.*?)(V\d*\.\d*)?$"
        results = re.findall(idnRegex, self._idn)
        if len(results):
            results = results[0]
            self._manufacturer = results[0]
            self._model = results[1]
            if len(results) > 2:
                self._version = results[2]
        else:
            self.close()
            raise RuntimeError(
                "Reply from PSU did not match expected format, not a supported device!"
            )

    def isConnected(self):
        return self._connection.is_open

    @property
    def port(self) -> str:
        """The serial port that the PSU is connected to. Changing the port while already connected will automatically disconnect from the current port and the application will need to call connect() again to reconnect."""
        return self._port

    @port.setter
    def port(self, port: str):
        self._port = port
        if self.isConnected():
            self.close()
        self._connection = serial.serial_for_url(
            url=port,
            baudrate=9600,
            timeout=1.3,
            exclusive=True,
            do_not_open=True,
        )

    def setPort(self, port: str):
        self.port = port

    @property
    def maximumVoltage(self) -> float:
        """The maximum voltage that the PSU can output in volts."""
        return self._maximumVoltage

    @property
    def maximumCurrent(self) -> float:
        """The maximum current that the PSU can output in amps."""
        return self._maximumCurrent

    @property
    def current(self) -> float:
        """The current limit setting of the PSU in amps. Note that this is not the actual current output, which can be read from the currentOutput property."""
        response = self._sendCommand("ISET1?", replyLength=6)
        # There is a bug in the PSU firmware where it sometimes appends a random garbage character to the end of the response, so we need to strip that out if it's there
        if response[-1:] not in ["01234567890"]:
            response = response[:-1]
        return float(response)

    @current.setter
    def current(self, current: float):
        if current < 0.0:
            current = 0.0
        if current > self._maximumCurrent:
            current = self._maximumCurrent
        retries = 0
        while retries < 5:
            self._sendCommand(f"ISET1:{current:.3f}", singleShot=True)
            if self.current == current:
                return
            retries += 1
        raise ValueError(f"Failed to set current to {current:.3f}A after 5 attempts")

    def setCurrent(self, current: float):
        """Set the current limit setting of the PSU in amps."""
        self.current = current

    @property
    def voltage(self) -> float:
        """The voltage limit setting of the PSU in volts. Note that this is not the actual voltage output, which can be read from the voltageOutput property."""
        return round(float(self._sendCommand("VSET1?", replyLength=5)), 2)

    @voltage.setter
    def voltage(self, voltage: float):
        if voltage < 0:
            voltage = 0
        if voltage > self._maximumVoltage:
            voltage = self._maximumVoltage
        retries = 0
        while retries < 5:
            self._sendCommand(f"VSET1:{voltage:.2f}", singleShot=True)
            if self.voltage == voltage:
                return
            retries += 1
        raise ValueError(f"Failed to set voltage to {voltage:.2f}V after 5 attempts")

    def setVoltage(self, voltage: float):
        """Set the voltage limit setting of the PSU in volts."""
        self.voltage = voltage

    @property
    def currentOutput(self) -> float:
        """The current output of the PSU in amps."""
        return float(self._sendCommand("IOUT1?", replyLength=5))

    @property
    def voltageOutput(self) -> float:
        """The voltage output of the PSU in volts."""
        return float(self._sendCommand("VOUT1?", replyLength=5))

    @property
    def status(self) -> dict:
        """A dictionary containing the current status of the PSU, including mode (CV or CC), tracking mode (independent, series, or parallel), beep status, lock status, and output status."""
        statusBits = ord(self._sendCommand("STATUS?", replyLength=1, waitTime=0.045))
        return {
            "mode": CcCvMode.CV if statusBits & 0x01 else CcCvMode.CC,
            "tracking": TrackingMode.INDEPENDENT
            if statusBits & (0x03 << 2) == 0
            else TrackingMode.SERIES
            if statusBits & (0x03 << 2) == 1
            else TrackingMode.PARALLEL,
            "beep": bool(statusBits & (0x01 << 4)),
            "lock": not bool(statusBits & (0x01 << 5)),
            "output": bool(statusBits & (0x01 << 6)),
        }

    @property
    def identification(self) -> str:
        """The unmodified identification string returned by the PSU."""
        return self._sendCommand("*IDN?").upper()

    @property
    def manufacturer(self) -> str:
        """The manufacturer of the PSU."""
        return self._manufacturer

    @property
    def model(self) -> str:
        """The model of the PSU."""
        return self._model

    @property
    def version(self) -> str:
        """The version of the PSU."""
        return self._version

    def recall(self, memorySlot: int):
        """Recall a saved setting from the specified memory slot."""
        if memorySlot < 1 or memorySlot > 5:
            raise ValueError("Memory slot must be between 1 and 5")
        self._sendCommand(f"RCL{memorySlot}", singleShot=True)

    def save(self, memorySlot: int):
        """Save the current settings to the specified memory slot."""
        if memorySlot < 1 or memorySlot > 5:
            raise ValueError("Memory slot must be between 1 and 5")
        self._sendCommand(f"SAV{memorySlot}", singleShot=True)

    @property
    def cc(self) -> bool:
        """Check if the PSU is in constant current mode."""
        if self.status["mode"] == CcCvMode.CC:
            return True
        return False

    @property
    def cv(self) -> bool:
        """Check if the PSU is in constant voltage mode."""
        if self.status["mode"] == CcCvMode.CV:
            return True
        return False

    @property
    def tracking(self) -> TrackingMode:
        """Get the tracking mode of the PSU."""
        return self.status["tracking"]

    @property
    def beep(self) -> bool:
        """Check if the PSU's beeper is enabled."""
        return self.status["beep"]

    @beep.setter
    def beep(self, enable: bool):
        """Enable or disable the PSU's beeper. Note that this doesn't appear to actually work on the Velleman LABPS3005D."""
        self._sendCommand(f"BEEP{'1' if enable else '0'}", singleShot=True)

    def setBeep(self, enable: bool):
        """Enable or disable the PSU's beeper. Note that this doesn't appear to actually work on the Velleman LABPS3005D."""
        self.beep = enable

    @property
    def lock(self) -> bool:
        """Check if the PSU's physical controls are locked."""
        return self.status["lock"]

    @lock.setter
    def lock(self, enable: bool):
        """Lock or unlock the PSU's physical controls. Note that this doesn't appear to actually work on the Velleman LABPS3005D."""
        self._sendCommand(f"LOCK{'1' if enable else '0'}", singleShot=True)

    def setLock(self, enable: bool):
        """Lock or unlock the PSU's physical controls. Note that this doesn't appear to actually work on the Velleman LABPS3005D."""
        self.lock = enable

    @property
    def output(self) -> bool:
        """Check if the PSU's output is enabled."""
        return self.status["output"]

    @output.setter
    def output(self, enable: bool):
        """Enable or disable the PSU's output."""
        retries = 0
        while retries < 5:
            self._sendCommand(f"OUT{'1' if enable else '0'}", singleShot=True)
            if self.output == enable:
                return
            retries += 1
        errorString = f"OutputSetter: Failed to set output to {enable} after 5 attempts"
        raise ValueError(errorString)

    def setOutput(self, enable: bool):
        """Enable or disable the PSU's output."""
        self.output = enable

    def setOCP(self, enable: bool):
        """Enable or disable overcurrent protection."""
        retries = 0
        while retries < 5:
            self._sendCommand(f"OCP{'1' if enable else '0'}", singleShot=True)
            if self.output == enable:
                return
            retries += 1
        raise ValueError(f"Failed to set OCP to {enable} after 5 attempts")

    def setOVP(self, enable: bool):
        """Enable or disable overvoltage protection."""
        retries = 0
        while retries < 5:
            self._sendCommand(f"OVP{'1' if enable else '0'}", singleShot=True)
            if self.output == enable:
                return
            retries += 1
        raise ValueError(f"Failed to set OVP to {enable} after 5 attempts")

    def _sendCommand(
        self,
        command: str,
        replyLength: int | None = None,
        singleShot: bool = False,
        waitTime: float = 0.0,
    ) -> str:
        if not self.isConnected():
            raise ConnectionError("Not connected to PSU")
        retries = 0
        while retries < 5:
            self._connection.write(command.encode())
            if waitTime:
                time.sleep(waitTime)
            if singleShot:
                if not waitTime:
                    time.sleep(0.045)
                return ""
            response = self._connection.read_until(size=replyLength).decode()
            if len(response) and (not replyLength or len(response) == replyLength):
                return response
            retries += 1
        raise TimeoutError("No response from PSU")

    def close(self):
        """Close the connection to the PSU."""
        if self.isConnected():
            self._connection.close()
        self._manufacturer = "Unknown"
        self._model = "Unknown"
        self._version = "Unknown"
        self._idn = ""

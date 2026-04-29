# PSUcontrol

This is an application for controlling a Velleman LABPS3005D bench PSU and any compatible ones.

The project is still a work-in-progress and has only been tested with the aforementioned Velleman. That said, the basics do work fine for me.

![PSUcontrol Example](extra/psucontrol_gui.gif)

## CAVEATS

These PSUs tend to be buggy in multiple different ways and I have seen some mentions online about some of them just randomly having far longer delays in responding to commands than usual. The Velleman I have is missing e.g. the ability to control the audible beeps and the ability to lock/unlock the physical controls despite the protocol documentation saying otherwise. Without the ability to upgrade their firmwares this project is entirely YMMV and no guarantees are given.

## INSTALLATION

The recommended approach:

```bash
pipx install psucontrol
```

([If you are not familiar with pipx, take a look here](https://pipx.pypa.io/stable/))

You can also grab one of the binary releases from the Releases-section but they are rather large because they bundle an entire Python-environment inside. Do also note that the Windows Defender is practically guaranteed to falsely flag the .exe-files as containing viruses -- this is a false positive but there is really not much I can do about it.

## DEVELOPMENT

Install `poetry`. I, again, recommend `pipx` for this.

To modify the GUI:

```bash
git clone --recurse-submodules https://github.com/WereCatf/psucontrol
cd psucontrol
export PYSIDE_DESIGNER_PLUGINS="external/indicatorlabel;external/lcdlabel"
poetry install
poetry run pyside6-designer
```

If you have made any GUI or resource-file changes, you can rebuild the relevant files with:

```bash
cd psucontrol # If not already in there
poetry run pyside6-project build
# There is seemingly no way of making either pyside6-project or pyside6-uic to correctly generate the imports
# so we have to always fix the imports, or at least I have not found a way to do this automatically.
sed -i 's/^import rc_/import psucontrol.rc_/g' src/psucontrol/*.py
```

If you don't plan to touch the GUI-stuff, you can just do:

```bash
git clone --recurse-submodules https://github.com/WereCatf/psucontrol
cd psucontrol
poetry install
```

## TODO

- Fill out this README more
- Implement the memory-buttons functionality
- Add toggleable graphing
- CLI-interface
- TUI-interface
- Maybe see about dumping the firmware (with Chipwhisperer?)
- Add support for more PSUs?
- Add support for multiple channels?

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

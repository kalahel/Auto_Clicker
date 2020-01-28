from cx_Freeze import setup, Executable

# Run : python setup.py build
# In Terminal

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "time", "fileinput", "cv2", "pyautogui", "fileinput"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="<any name>",
    options=options,
    version="<any number>",
    description='<any description>',
    executables=executables, requires=['pyautogui']
)

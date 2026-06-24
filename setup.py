from cx_Freeze import setup, Executable

setup(name="Bytes substitution coder", executables=[Executable("Bytes substitution coder script.py")], options={"build_exe": {"excludes": ["tkinter"]}})

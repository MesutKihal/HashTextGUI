import cx_Freeze

executables = [cx_Freeze.Executable("hash.py",base='win32gui',icon='icon.ico')]

cx_Freeze.setup(
    name="Hash Text",
    options={"build_exe": {"include_files":["icon.ico"]}},
    
    executables = executables

    )

__author__ = 'Kaiming'

from cx_Freeze import setup, Executable

setup(name="os_homwork",
      version="1.0_beta",
      description="File Search System",
      executables=[Executable("os_homework.py")]
      )

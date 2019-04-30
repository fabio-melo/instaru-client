from gui import start_gui
from cli import start_cli
from sys import argv
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':
  if not is_admin():
    if len(argv) > 1 and '-cli' in argv:
      print(argv)
      start_cli(argv[2])

    else:
      start_gui()
  else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
  
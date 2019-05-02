from gui import start_gui
from cli import start_cli
from sys import argv
from licensing import LicenseFactory
import ctypes, sys, logging

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  if LicenseFactory().check_if_license():

    if not is_admin():
      if len(argv) > 1:
        start_cli(argv[1])

      else:
        start_gui()
        pass
    else:
      # Re-run the program with admin rights
      ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
  else:
    print("programa não licenciado, você pode ser vítima de pirataria")
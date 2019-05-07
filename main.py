from gui import start_gui
from cli import start_cli
from sys import argv
from licensing import LicenseFactory
import ctypes, sys, logging
from time import time
from pathlib import Path
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':
  # LOGS
  logdir = Path(os.getcwd())
  logdir = logdir / 'logs'

  if not logdir.exists(): logdir.mkdir()
  logpath = logdir / f"instaru_{int(time())}.log"

  logging.basicConfig(level=logging.INFO, filename=logpath)
  
  #LICENÇA
  if LicenseFactory().check_if_license():

    if len(argv) > 1:
      start_cli(argv[1])

    else:
      start_gui()
    
    
    
    # Re-run the program with admin rights
    #ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
  else:
    print("programa não licenciado, você pode ser vítima de pirataria")
from gui import start_gui
from profile import start_cli
from sys import argv

if len(argv) > 1 and '-cli' in argv:
  print(argv)
  start_cli(argv[2])

else:
  start_gui()
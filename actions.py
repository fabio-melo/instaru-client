
import requests
import re
from clint.textui import progress
from subprocess import check_output

class Action:

  def __init__(self, action_type, action_body):
    self.action_type = action_type
    self.action_body = action_body

  def execute(self):
    if self.action_type == 'cmd':
      self.system_command()
    elif self.action_type == 'dwn':
      self.download_file()

  def __repr__(self):
    return f'{self.action_type}: {self.action_body}'
    
  def system_command(self):
    print(f'COMANDO {self.action_body}')
    print(check_output(self.action_body, shell=True).decode())

  def download_file(self):
    print(f'LOCAL DO ARQUIVO: {self.action_body}')
    with requests.get(self.action_body, stream=True) as r:
      fname = ''
      if "Content-Disposition" in r.headers.keys():
        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
      else:
        fname = self.action_body.split("/")[-1]

      print(fname)

      
      with open(fname, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
          if chunk:
              f.write(chunk)
              f.flush()


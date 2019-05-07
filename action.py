import requests
import re
import time
import subprocess
import logging as log
from clint.textui import progress
from utils import check_sha256

class ActionFactory():
  def build_action(self, action_type, action_body):
    if action_type == 'dwn':
      return DownloadAction(action_body)
    elif action_type == 'cmd':
      return CommandAction(action_body)


class DownloadAction():

  def __init__(self, download_body):
    self.download_url = download_body['url']
    self.check_integrity = download_body['check_integrity']
    self.sha256 = download_body['sha256']
    self.run_file = download_body['run_file']
    self.run_arguments = download_body['run_arguments']


  def execute(self):
    log.info(f'Download: {self.download_url}')

    with requests.get(self.download_url, stream=True) as r:
      # extrair nome do arquivo
      fname = ''
      if "Content-Disposition" in r.headers.keys():
        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
      else:
        fname = self.download_url.split("/")[-1]

      log.info(f'File: {fname}')

      # baixar arquivo 
      with open(fname, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
          if chunk:
              f.write(chunk)
              f.flush()

      # verificar integridade
      if self.check_integrity:
        checksum = check_sha256(fname)
        if checksum == self.sha256:
          log.info(f'FILE OK, SHA256 {checksum}')
        else:
          log.warning('CHECKSUM DOESNT MATCH')

      #executar
      if self.run_file:
        try:
          build_command = f"START /WAIT {fname} {self.run_arguments}"
          log.info(build_command)
          output = subprocess.call(build_command, shell=True)
          log.info(output)
          log.info("Procedimento Concluido")
        except:
          log.error('erro na execução do comando / malformado?')

class CommandAction():
  def __init__(self, command_body):
    #self.need_admin = command_body['need_admin']
    self.command_to_run = command_body['command_to_run']
  def execute(self):
    log.info(f'Executando comando {self.command_to_run}')
    output = subprocess.call(self.command_to_run, shell=True)
    log.info(output)
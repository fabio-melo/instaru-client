from abc import abstractclassmethod
from profile import Profile, ProfileCollection
from action import DownloadAction, CommandAction
import requests

FIRESTORE_URL = 'https://firestore.googleapis.com/v1/projects/autoupd-6c999/databases/(default)/documents/profiles'

class FirestoreFactory:

  def fetch_profiles(self, profile_data):
    """retorna nome e ações"""
    return [Profile(
      x['fields']['name']['stringValue'], \
      x['fields'], self.build_func) \
      for x in profile_data['documents']]
  
  def build_collection(self):
    stored_json = requests.get(FIRESTORE_URL).json()
    return ProfileCollection(self.fetch_profiles(stored_json))

  def build_func(self, fields):
    action_queue = []

    # downloads
    if 'download' in fields:
      for x in fields['download']['arrayValue']['values']:
        download_body = {}
        download_body['url'] = x['mapValue']['fields']['url']['stringValue']

        try:
          download_body['check_integrity'] = x['mapValue']['fields']['check_integrity']['booleanValue']
          download_body['sha256'] = x['mapValue']['fields']['sha256']['stringValue']
        except:
          download_body['check_integrity'] = False
          download_body['sha256'] = False
        
        try:
          download_body['run_file'] =x['mapValue']['fields']['run_file']['booleanValue']
        except:
          download_body['run_file'] = False
        try:
          download_body['run_arguments'] = x['mapValue']['fields']['run_arguments']['stringValue']
        except:
          download_body['run_arguments'] = False

        print(download_body, end="\n\n")
        action_queue.append(DownloadAction(download_body))
      
      #commands
    if 'commands' in fields: 
      for x in fields['commands']['arrayValue']['values']:
        command_body = {}
        print("AAAAA")
        command_body['command_to_run'] = x['mapValue']['fields']['command_to_run']['stringValue']
        action_queue.append(CommandAction(command_body))

    return action_queue

from abc import abstractclassmethod
from profiles import Profile, ProfileCollection
from actions import Action
import requests

FIRESTORE_URL = 'https://firestore.googleapis.com/v1/projects/autoupd-6c999/databases/(default)/documents/profiles'


class FirestoreFactory:

  def fetch_profiles(self, profile_data):
    """retorna nome e ações"""
    return [Profile(
      x['fields']['name']['stringValue'], \
      self.build_action_queue(x['fields']['commands']['arrayValue']['values'])) \
      for x in profile_data['documents']]

  def build_action_queue(self, action_data):
    """retorna uma lista de ações (tipo/ação)"""
    return [Action(x['mapValue']['fields']['type']['stringValue'], \
                   x['mapValue']['fields']['action']['stringValue']) \
                   for x in action_data]
  
  def build_collection(self, firestore):
    stored_json = requests.get(firestore).json()
    return ProfileCollection(self.fetch_profiles(stored_json))
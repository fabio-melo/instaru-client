from actions import Action
from collections import namedtuple
import requests

firestore = ''

class Profile():
  def __init__(self, name, actions):
    self.name = name
    self.action_queue = self.build_action_queue(actions)

  def __repr__(self):
    return f'{self.name}'

  def build_action_queue(self, actions):
    return [Action(x['mapValue']['fields']['type']['stringValue'], \
                 x['mapValue']['fields']['action']['stringValue']) \
          for x in actions]

  def run_all(self):
    for x in self.action_queue: x.execute()


def fetch_data(firestore):
  profile_data = requests.get(firestore).json()
  
  return [Profile(x['fields']['name']['stringValue'], \
                      x['fields']['commands']['arrayValue']['values']) 
                      for x in profile_data['documents']]
  

mydatastructs = fetch_data(firestore)

print(mydatastructs)

mydatastructs[0].run_all()

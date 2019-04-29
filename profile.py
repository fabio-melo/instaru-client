from actions import Action
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

class ProfileCollection:
  def __init__(self, firestore):
    self.stored_json = requests.get(firestore).json()
    self.profile_list = self.fetch_data(self.stored_json)

  def fetch_data(self, profile_data):
    return [Profile(x['fields']['name']['stringValue'], \
                        x['fields']['commands']['arrayValue']['values']) 
                        for x in profile_data['documents']]
  
  def find_by_name(self, name):
    for prof in self.profile_list:
      if prof.name == name:
        return prof
      else:
        return False


def start_cli(profile_selected):
  profile_list = ProfileCollection(firestore)
  p = profile_list.find_by_name(profile_selected)
  if p:
    print(f"PROFILE ACHADO, RODANDO {profile_selected}")
    p.run_all()
  else:
    print(f"ERRO: perfil não encontrado")

# mydatastructs = fetch_data(firestore)


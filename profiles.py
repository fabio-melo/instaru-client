class Profile():
  def __init__(self, name, actions):
    self.name = name
    self.action_queue = actions
    print(f"{self.name} {self.action_queue}")

  def __repr__(self):
    return f'{self.name}'

  def run_all(self):
    for x in self.action_queue: x.execute()

class ProfileCollection:
  def __init__(self, profile_list):
    self.profile_list = profile_list

  def find_by_name(self, name):
    print(name)
    for prof in self.profile_list:
      if prof.name == name:
        return prof
    else:
      raise Exception("not found")


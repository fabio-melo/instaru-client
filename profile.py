import logging as log

class Profile():
  def __init__(self, name, fields, builder_func):
    self.name = name
    self.fields = fields
    self.action_queue = []
    self.builder_func = builder_func

  def __repr__(self):
    return f'{self.name}'

  def build(self):
    self.action_queue = self.builder_func(self.fields)

  def run_all(self):
    for x in self.action_queue: x.execute()

class ProfileCollection:
  def __init__(self, profile_list):
    self.profile_list = profile_list

  def find_profile(self, name):   
    for prof in self.profile_list:
      if prof.name == name: return prof
    else: 
      log.error("Profile not found")
      raise Exception("not found")


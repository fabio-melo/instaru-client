import requests
import os
import easygui

LICENSE_SERVER = "https://firestore.googleapis.com/v1/projects/instaru-license/databases/(default)/documents/profiles"


class LicenseFactory:

  def verify_license(self, license_key):
    licenses = requests.get(LICENSE_SERVER).json()
    for x in licenses['documents']:
      if license_key == x['fields']['serial']['stringValue']:
        print(f"LICENSE OK - {x['fields']['name']['stringValue']}")
        return True
    else:
      print(f'LICENSE CHECK FAILED')
      return False


  def check_if_license(self):
    license_file = 'license.key'
    if os.path.isfile(license_file):
      with open(license_file,'r') as lf:
        license_key = lf.read()
        if self.verify_license(license_key): return True
        else: return False
    else:
      l = easygui.enterbox("INSTARU - Chave de Licença")
      if self.verify_license(l):
        with open(license_file,'w') as license_write:
          easygui.msgbox("Licença Validada")
          license_write.write(l)
          return True
      else:
        easygui.msgbox("Licença Invalida")
        print("INVALID LICENSE")
        return False


LicenseFactory().check_if_license()
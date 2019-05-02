import requests


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





  
      
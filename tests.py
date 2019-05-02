from licensing import LicenseFactory
from firebase import FirestoreFactory

def licensing_tests():
  lf = LicenseFactory()

  #LICENÇA CORRETA
  lf.verify_license('1234-5678-910F')
  #Licença errada
  lf.verify_license('323222232')

  #ARQUIVO DE LICENÇA
  LicenseFactory().check_if_license()


def profile_building_tests():
  ff = FirestoreFactory()

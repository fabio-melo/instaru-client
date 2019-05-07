from firebase import FirestoreFactory
import logging as log

def start_cli(profile_selected, *args):
  profile_list = FirestoreFactory().build_collection()
  p = profile_list.find_profile(profile_selected)
  if p:
    log.info(f"Perfil Encontrado, Executando {profile_selected}")
    p.build()
    p.run_all()
  else:
    log.error(f"ERRO: perfil não encontrado")

# mydatastructs = fetch_data(firestore)

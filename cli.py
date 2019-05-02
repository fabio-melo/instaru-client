from firebase import FirestoreFactory, FIRESTORE_URL

def start_cli(profile_selected, *args):
  profile_list = FirestoreFactory().build_collection(FIRESTORE_URL)
  p = profile_list.find_profile(profile_selected)
  if p:
    print(f"PROFILE ACHADO, RODANDO {profile_selected}")
    p.build()
    p.run_all()
  else:
    print(f"ERRO: perfil não encontrado")

# mydatastructs = fetch_data(firestore)

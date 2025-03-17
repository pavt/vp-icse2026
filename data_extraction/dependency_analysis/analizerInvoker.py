import sys
import os

import pandas as pd

import singleAnalizer
from git import Repo

def run_with_args(args_list):
    # Salviamo l'originale sys.argv
    original_sys_argv = sys.argv
    try:
        # Impostiamo sys.argv con i nuovi argomenti
        sys.argv = [original_sys_argv[0]] + args_list
        singleAnalizer.main()
    finally:
        # Ripristiniamo sys.argv al valore originale
        sys.argv = original_sys_argv

def clone_repo(github_url, base_local_dir,repo_name):
    """
    Clona una repository Git da un URL in una directory locale.
    """
    try:
        # Estrai il nome del progetto dall'URL
        local_dir = os.path.join(base_local_dir, repo_name).replace("\\", "/")
        
        print(f"Clonazione della repository da {github_url} in {local_dir}...")
        Repo.clone_from(github_url, local_dir)
        print(f"Repository clonata con successo in {local_dir}.")
    except Exception as e:
        print(f"Errore durante la clonazione della repository: {e}")
        return None
    return local_dir

if __name__ == "__main__":
    '''
        base_local_dir = "Repositories"

    # Creare la directory base se non esiste
    os.makedirs(base_local_dir, exist_ok=True)
    data = pd.read_csv("sampled_repos.csv")
    for full_name in data['full_name']:
        github_url = f"https://token/{full_name}.git"

        # Clona la repository in una cartella specifica
        cloned_repo_path = clone_repo(github_url, base_local_dir,full_name.replace("/","-"))

        if cloned_repo_path:
            # Passa la directory clonata a singleAnalizer usando -r
            run_with_args(['-r', cloned_repo_path])
    
    '''

    base_local_dir = "Repositories"

    # Verifica che la directory base esista
    if not os.path.exists(base_local_dir):
        raise FileNotFoundError(f"La directory {base_local_dir} non esiste.")

    data = pd.read_csv("sampled_repos.csv")
    for full_name in data['full_name']:
        # Determina il percorso della repository locale
        local_repo_path = os.path.join(base_local_dir, full_name.replace("/", "-"))

        if os.path.exists(local_repo_path):
            # Passa la directory esistente a singleAnalizer usando -r
            run_with_args(['-r', local_repo_path])
        else:
            print(f"Attenzione: la repository {local_repo_path} non esiste e verrà saltata.")
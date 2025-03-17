import os
import json
import pandas as pd

# Percorsi delle cartelle
sbom_folder = "SBOM_Source_Analisys"
vuln_folder = "Vulnerabilities_with_CWE"
report_path = "report.csv"
sampled_repos_path = "sampled_repos.csv"

# Funzione per leggere tutti i file JSON da una cartella
def read_json_files_from_folder(folder_path):
    files_data = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, 'r') as f:
                    files_data[file_name] = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print(f"Errore nel leggere il file: {file_path}")
    return files_data

# Funzione per trovare la categoria dal file report.csv
def find_category(filename, report_df):
    try:
        row = report_df[report_df['File Name'].str.contains(filename, na=False)]
        if not row.empty:
            return row.iloc[0]['Category']
    except KeyError:
        print("Colonna 'File Name' o 'Category' mancante nel CSV")
    return "Unknown"

# Caricare il file report.csv
try:
    report_df = pd.read_csv(report_path)
except (pd.errors.EmptyDataError, FileNotFoundError):
    print("Errore nel leggere il file CSV o file vuoto.")
    report_df = pd.DataFrame(columns=['File Name', 'Category'])

# Caricare il file sampled_repos.csv
try:
    sampled_repos = pd.read_csv(sampled_repos_path)
    sampled_repos['File Name'] = sampled_repos['repo_owner'] + '-' + sampled_repos['repo_name']
    file_name_to_repo = sampled_repos.set_index('File Name')[['repo_owner', 'repo_name']]
except (pd.errors.EmptyDataError, FileNotFoundError):
    print("Errore nel leggere il file sampled_repos.csv o file vuoto.")
    file_name_to_repo = pd.DataFrame()

# Leggere tutti i file JSON dalle cartelle
sbom_files = read_json_files_from_folder(sbom_folder)
vuln_files = read_json_files_from_folder(vuln_folder)

# Generare il JSON di sintesi per tutti i file
sintesi = []

for sbom_file_name, sbom_data in sbom_files.items():
    # Estrarre il prefisso del file
    prefix = sbom_file_name.split('_SBOM')[0]

    # Cercare il file vulnerabilità corrispondente
    vuln_file_name = f"{prefix}_Vuln.json"
    if vuln_file_name in vuln_files:
        vuln_data = vuln_files[vuln_file_name]

        # Componenti dal SBOM (identificate dal purl)
        components = [comp.get('purl') for comp in sbom_data.get('components', []) if comp.get('purl')]

        # Vulnerabilità dalla coppia GHSA e CWE
        vulnerabilities = []
        for key, vuln_info in vuln_data.items():
            for vuln in vuln_info.get('vulnerabilities', []):
                if isinstance(vuln, dict):
                    vulnerabilities.append({
                        'GHSA': vuln.get('id', 'Unknown'),
                        'CWE': vuln.get('CWE_ID', 'Unknown'),
                        'description': vuln.get('description', 'No description provided'),
                        'severity': vuln.get('severity', 'Unknown')
                    })

        # Recuperare repo_owner e repo_name
        repo_owner = file_name_to_repo.loc[prefix, 'repo_owner'] if prefix in file_name_to_repo.index else "Unknown"
        repo_name = file_name_to_repo.loc[prefix, 'repo_name'] if prefix in file_name_to_repo.index else "Unknown"

        # Aggiungere i dati all'output finale
        sintesi.append({
            "repo_owner": repo_owner,
            "repo_name": repo_name,
            "components": components,
            "vulnerabilities": vulnerabilities,
            "category": find_category(prefix, report_df)
        })

# Salvare il risultato in un file JSON
output_path = "FinalSummary.json"
with open(output_path, 'w') as f:
    json.dump(sintesi, f, indent=4)

print(f"File JSON di sintesi salvato in: {output_path}")

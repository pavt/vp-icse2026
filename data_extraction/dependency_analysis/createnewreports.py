import pandas as pd

# Carica i file report.csv e sampled_repos.csv
report = pd.read_csv('report.csv')
sampled_repos = pd.read_csv('sampled_repos.csv')

# Crea il campo 'File Name' in sampled_repos per il confronto
sampled_repos['File Name'] = sampled_repos['repo_owner'] + '-' + sampled_repos['repo_name']

# Seleziona solo le colonne utili da sampled_repos
file_name_to_repo = sampled_repos.set_index('File Name')[['repo_owner', 'repo_name']]

# Aggiunge le colonne 'repo_owner' e 'repo_name' al file report.csv
report = report.join(file_name_to_repo, on='File Name')

# Rimuove la colonna 'File Name' e ordina le colonne con 'repo_owner' e 'repo_name' al primo posto
report = report[['repo_owner', 'repo_name'] + [col for col in report.columns if col not in ['repo_owner', 'repo_name', 'File Name']]]

# Salva il nuovo file Final_report.csv
report.to_csv('Final_report.csv', index=False)

print("Il file Final_report.csv è stato creato correttamente!")

# Carica i file high_critical_report.csv e sampled_repos.csv
high_critical_report = pd.read_csv('high_critical_report.csv')
sampled_repos = pd.read_csv('sampled_repos.csv')

# Crea il campo 'File Name' in sampled_repos per il confronto
sampled_repos['File Name'] = sampled_repos['repo_owner'] + '-' + sampled_repos['repo_name']

# Seleziona solo le colonne utili da sampled_repos
file_name_to_repo = sampled_repos.set_index('File Name')[['repo_owner', 'repo_name']]

# Aggiunge le colonne 'repo_owner' e 'repo_name' al file high_critical_report.csv
high_critical_report = high_critical_report.join(file_name_to_repo, on='File Name')

# Rimuove la colonna 'File Name' e ordina le colonne con 'repo_owner' e 'repo_name' al primo posto
high_critical_report = high_critical_report[['repo_owner', 'repo_name'] + [col for col in high_critical_report.columns if col not in ['repo_owner', 'repo_name', 'File Name']]]

# Salva il nuovo file Final_high_critical_report.csv
high_critical_report.to_csv('Final_high_critical_report.csv', index=False)

print("Il file Final_high_critical_report.csv è stato creato correttamente!")

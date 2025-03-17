import ast
import math

import pandas as pd
import matplotlib.pyplot as plt
import os
# Carica il file CSV
data = pd.read_csv('report.csv')

# 1) Boxplot della distribuzione della colonna Number of Components
plt.figure(figsize=(8, 6))
plt.boxplot(data['Number of Components'].dropna(),tick_labels=["Dataset"])
plt.title('Distribution of Number of Components')
plt.ylabel('Number of Components')
plt.savefig('figures/number_of_components_boxplot.jpeg')
plt.close()

# 2) Boxplot della distribuzione della colonna Total Vulnerabilities
plt.figure(figsize=(8, 6))
plt.boxplot(data['Total Vulnerabilities'].dropna(),tick_labels=["Dataset"])
plt.title('Distribution of Total Vulnerabilities')
plt.ylabel('Total Vulnerabilities')
plt.savefig('figures/total_vulnerabilities_boxplot.jpeg')
plt.close()

# 3) Boxplot per ogni livello di severità
severity_levels = ['Low', 'Medium', 'High', 'Critical']
severity_data = [data[level].dropna() for level in severity_levels]

plt.figure(figsize=(10, 6))
plt.boxplot(severity_data, tick_labels=severity_levels)
plt.title('Distribution of Vulnerabilities by Severity')
plt.ylabel('Number of Vulnerabilities')
plt.xlabel('Severity Level')
plt.savefig('figures/vulnerabilities_by_severity_boxplot.jpeg')
plt.close()

# 4) Boxplot del numero di vulnerabilità totali divisi per categoria
# Carica il file CSV
# Carica il file CSV

# Converti i valori di 'Category' da stringhe a liste utilizzando `ast.literal_eval`

'''
data['Category'] = data['Category'].apply(ast.literal_eval)

# Splitta le categorie multiple in righe separate
data_exploded = data.explode('Category')
data_exploded['Category'] = data_exploded['Category'].str.strip()  # Rimuove spazi bianchi dai nomi delle categorie

# Ottiene la lista delle categorie uniche
unique_categories = data_exploded['Category'].unique()
'''

unique_categories = data['Category'].unique()
# Crea una cartella per i grafici, se non esiste già
output_dir = "figures"
os.makedirs(output_dir, exist_ok=True)

# Suddivide le categorie in gruppi di massimo 10
num_plots = math.ceil(len(unique_categories) / 10)

for i in range(num_plots):
    # Estrae le categorie per il grafico corrente
    category_subset = unique_categories[i * 10:(i + 1) * 10]

    # Prepara i dati per il boxplot per le categorie selezionate
    boxplot_data = [data_exploded[data_exploded['Category'] == category]['Total Vulnerabilities'].dropna() for category
                    in category_subset]

    # Genera il boxplot per il gruppo di categorie
    plt.figure(figsize=(12, 8))
    plt.boxplot(boxplot_data, tick_labels=category_subset)
    plt.title(
        f'Distribution of Total Vulnerabilities (Categories {i * 10 + 1}-{min((i + 1) * 10, len(unique_categories))})')
    plt.ylabel('Total Vulnerabilities')
    plt.xlabel('Software Category')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salva il grafico in un file JPEG
    output_path = f'{output_dir}/total_vulnerabilities_boxplot_group_{i + 1}.jpeg'
    plt.savefig(output_path)
    plt.close()

    print(f"Grafico generato: {output_path}")
print("Grafici generati con successo:")
print("- number_of_components_boxplot.jpeg")
print("- total_vulnerabilities_boxplot.jpeg")
print("- vulnerabilities_by_severity_boxplot.jpeg")
print("- total_vulnerabilities_by_category_boxplot.jpeg")

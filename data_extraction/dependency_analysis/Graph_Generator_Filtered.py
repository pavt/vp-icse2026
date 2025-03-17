import math
import pandas as pd
import matplotlib.pyplot as plt
import os

# Carica il file CSV
data = pd.read_csv('high_critical_report.csv')

# Crea una cartella per i grafici, se non esiste già
output_dir = "Sorted_figures_Filtered"
os.makedirs(output_dir, exist_ok=True)

# 2) Boxplot della distribuzione della colonna Total Vulnerabilities (ordinato per mediana decrescente)
total_vulnerabilities_data = data['Total Vulnerabilities (High or Critical)'].dropna()
if len(total_vulnerabilities_data) > 1:
    plt.figure(figsize=(8, 6))
    plt.boxplot([total_vulnerabilities_data], tick_labels=["Dataset"])
    plt.title('Distribution of Total Vulnerabilities')
    plt.ylabel('Total Vulnerabilities')
    plt.savefig(f'{output_dir}/total_vulnerabilities_boxplot.jpeg')
    plt.close()

# 4) Boxplot del numero di vulnerabilità totali divisi per categoria (ordinato decrescente e filtrato)
# Assumi che il campo 'Category' contenga una singola stringa (non più una lista)

# Ottiene la lista delle categorie uniche e filtra per almeno 2 elementi
filtered_categories = [
    category for category in data['Category'].unique()
    if len(data[data['Category'] == category]['Total Vulnerabilities (High or Critical)'].dropna()) > 1
]

# Ordina le categorie in base alla mediana in ordine decrescente
category_medians = {
    category: data[data['Category'] == category]['Total Vulnerabilities (High or Critical)'].median()
    for category in filtered_categories
}
sorted_categories = sorted(category_medians, key=category_medians.get, reverse=True)

# Suddivide le categorie in gruppi di massimo 7
num_plots = math.ceil(len(sorted_categories) / 13)

for i in range(num_plots):
    # Estrae le categorie per il grafico corrente
    category_subset = sorted_categories[i * 13:(i + 1) * 13]

    # Prepara i dati per il boxplot per le categorie selezionate
    boxplot_data = [
        data[data['Category'] == category]['Total Vulnerabilities (High or Critical)'].dropna()
        for category in category_subset
    ]

    # Genera il boxplot per il gruppo di categorie
    plt.figure(figsize=(12, 8))
    plt.boxplot(boxplot_data, tick_labels=category_subset)
    plt.title(
        f'Distribution of Total Vulnerabilities (Categories {i * 13 + 1}-{min((i + 1) * 13, len(sorted_categories))})'
    )
    plt.ylabel('Total Vulnerabilities (High or Critical)')
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

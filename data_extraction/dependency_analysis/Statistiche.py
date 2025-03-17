from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests
import itertools
import pandas as pd
from scipy.stats import kruskal
import pandas as pd

# Carica il file CSV
file_path = 'high_critical_report.csv'  # Modifica il percorso al tuo file
data = pd.read_csv(file_path)

# Raggruppa i dati per categoria e conta le occorrenze
category_counts = data['Category'].value_counts()

# Filtra le categorie che hanno più di un campione
valid_categories = category_counts[category_counts > 1].index

# Filtra i dati per le categorie valide
filtered_data = data[data['Category'].isin(valid_categories)]

# Crea le distribuzioni delle vulnerabilità per categoria
category_distributions = {
    category: filtered_data[filtered_data['Category'] == category]['Total Vulnerabilities (High or Critical)'].tolist()
    for category in valid_categories
}
#0.571135
#0.579937
# Esegui il test di Kruskal-Wallis sulle distribuzioni delle categorie
values = list(category_distributions.values())

# Calcola il valore statistico e il p-value
stat, p_value = kruskal(*values)

# Crea una tabella con il risultato
kruskal_results_df = pd.DataFrame({
    'Categoria': ['Tutte le categorie'],
    'P-value': [p_value]
})

# Visualizza la tabella
print(kruskal_results_df)
############################################################################################
# Ottieni le categorie e le loro distribuzioni
categories = list(category_distributions.keys())
distributions = list(category_distributions.values())

# Esegui confronti pairwise con il test di Mann-Whitney
pairwise_results = []
for (cat1, dist1), (cat2, dist2) in itertools.combinations(zip(categories, distributions), 2):
    stat, p_value = mannwhitneyu(dist1, dist2, alternative='two-sided')
    pairwise_results.append({'Categoria 1': cat1, 'Categoria 2': cat2, 'P-value': p_value})

# Crea un DataFrame con i risultati raw
pairwise_df = pd.DataFrame(pairwise_results)
print(pairwise_df)

# Applica la correzione di Holm
corrected_p = multipletests(pairwise_df['P-value'], method='holm')[1]
pairwise_df['P-value corretto (Holm)'] = corrected_p

# Filtra le coppie con p-value corretto < 0.05
significant_pairs_df = pairwise_df[pairwise_df['P-value corretto (Holm)'] < 0.5]

# Ordina i risultati per p-value corretto
significant_pairs_df = significant_pairs_df.sort_values(by='P-value corretto (Holm)')

# Visualizza la tabella dei risultati significativi
print(significant_pairs_df)

'''
# Stampa le distribuzioni per verificare
for category, distribution in category_distributions.items():
    print(f"Categoria: {category}, Distribuzione: {distribution}")
'''


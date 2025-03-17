import json
import csv
import os

# Percorsi delle cartelle SBOM e Vulnerabilità
sbom_dir = r"SBOM_Source_Analisys"
vuln_dir = r"Vulnerabilities"
tentative_sample_path = r"sampled_repos.csv"

def load_category_map(file_path):
    """Carica una mappa full_name -> Category dal file CSV specificato."""
    category_map = {}
    with open(file_path, mode="r", encoding="utf-8", errors="replace") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            full_name = row.get("full_name")
            category = row.get("Category")
            if full_name and category:
                category_map[full_name.replace("/", "-")] = category
    return category_map

def analyze_high_critical_vulnerabilities(vuln_data):
    """Conta solo le vulnerabilità con severità High o Critical."""
    vuln_count = {"High": 0, "Critical": 0}
    total_vulnerabilities = 0

    for component in vuln_data.values():
        vuln_set = set()
        for vuln in component.get("vulnerabilities", []):
            if vuln.get("id", "unknown") not in vuln_set:
                vuln_set.add(vuln.get("id", "unknown"))
                severity = vuln.get("severity", "unknown")
                if severity in ["High", "Critical"]:
                    vuln_count[severity] += 1
                    total_vulnerabilities += 1

    return total_vulnerabilities, vuln_count["High"], vuln_count["Critical"]

def process_high_critical_files(sbom_dir, vuln_dir, output_csv="high_critical_report.csv"):
    # Carica la mappa fullname -> category dal file CSV di esempio
    category_map = load_category_map(tentative_sample_path)

    # Ottieni i file SBOM e Vulnerabilità usando solo la parte comune dei nomi
    sbom_files = {os.path.splitext(f)[0].replace("_SBOM", ""): f for f in os.listdir(sbom_dir) if
                  f.endswith("_SBOM.json")}
    vuln_files = {os.path.splitext(f)[0].replace("_Vuln", ""): f for f in os.listdir(vuln_dir) if
                  f.endswith("_Vuln.json")}

    # Trova i file con nome base comune
    common_files = sbom_files.keys() & vuln_files.keys()

    with open(output_csv, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File Name", "Total Vulnerabilities (High or Critical)", "Category"])

        for base_name in common_files:
            vuln_file_path = os.path.join(vuln_dir, vuln_files[base_name])

            with open(vuln_file_path, 'r') as f:
                vuln_data = json.load(f)

            # Conta le vulnerabilità High e Critical
            total_high_critical, high, critical = analyze_high_critical_vulnerabilities(vuln_data)

            # Ottieni la categoria corrispondente dal file di esempio
            category = category_map.get(base_name, "Unknown")

            # Scrive una riga per il file attuale nel CSV
            writer.writerow([base_name, total_high_critical, category])

    print("Report High e Critical generato con successo.")

# Esegue il processo
process_high_critical_files(sbom_dir, vuln_dir, output_csv="high_critical_report.csv")
print("Processo completato.")

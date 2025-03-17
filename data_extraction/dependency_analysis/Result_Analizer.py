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



def analyze_vulnerabilities(vuln_data):
    vuln_count = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
    total_vulnerabilities = 0
    vuln_ids = []

    for component in vuln_data.values():
        vuln_set = set()
        for vuln in component.get("vulnerabilities", []):
            if vuln.get("id", "unknown") not in vuln_set:
                vuln_set.add(vuln.get("id", "unknown"))
                severity = vuln.get("severity", "unknown")
                if severity in vuln_count:
                    vuln_count[severity] += 1
                vuln_ids.append(vuln.get("id", "unknown"))
                total_vulnerabilities += 1

    return total_vulnerabilities, vuln_count["Low"], vuln_count["Medium"], vuln_count["High"], vuln_count["Critical"], vuln_ids


def get_component_ids(sbom_data):
    component_ids = []
    for component in sbom_data.get("components", []):
        component_ids.append(component.get("bom-ref", "unknown"))
    return component_ids


def process_files(sbom_dir, vuln_dir, output_csv="report.csv", output_json="summary.json"):
    summary_data = []

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
        writer.writerow(
            ["File Name", "Number of Components", "Total Vulnerabilities", "Low", "Medium", "High", "Critical", "Category"])

        for base_name in common_files:
            sbom_file_path = os.path.join(sbom_dir, sbom_files[base_name])
            vuln_file_path = os.path.join(vuln_dir, vuln_files[base_name])

            with open(sbom_file_path, 'r') as f:
                sbom_data = json.load(f)
            with open(vuln_file_path, 'r') as f:
                vuln_data = json.load(f)

            # Conta i componenti e ottieni i loro ID
            component_ids = get_component_ids(sbom_data)
            num_components = len(component_ids)

            # Conta le vulnerabilità, per severità, e ottieni gli ID
            total_vuln, low, moderate, high, critical, vuln_ids = analyze_vulnerabilities(vuln_data)

            # Ottieni la categoria corrispondente dal file di esempio
            category = category_map.get(base_name, "Unknown")

            # Scrive una riga per il file attuale nel CSV
            writer.writerow([base_name, num_components, total_vuln, low, moderate, high, critical, category])

            # Crea l'entry per il file JSON di riepilogo
            summary_entry = {
                "file_name": base_name,
                "components": component_ids,
                "vulnerabilities": vuln_ids,
                "category": category
            }
            summary_data.append(summary_entry)

    # Scrive il file JSON di riepilogo
    with open(output_json, mode="w") as json_file:
        json.dump(summary_data, json_file, indent=4)

    print("Report CSV e riepilogo JSON generati con successo.")


# Esegue il processo
process_files(sbom_dir, vuln_dir, output_csv="report.csv", output_json="summary.json")
print("Processo completato.")

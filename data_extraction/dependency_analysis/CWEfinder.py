import requests
import json
import os

# Inserisci qui il tuo token di accesso personale di GitHub (PAT)
GITHUB_TOKEN = "ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
API_URL = "https://api.github.com/graphql"

# Funzione per ottenere il CWE dato un codice GHSA
def get_cwe_from_ghsa(ghsa_code):
    query = """
    query($ghsa: String!) {
      securityAdvisory(ghsaId: $ghsa) {
        cwes(first: 10) {
          nodes {
            cweId
            name
          }
        }
      }
    }
    """

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json",
    }

    variables = {"ghsa": ghsa_code}

    response = requests.post(
        API_URL, headers=headers, json={"query": query, "variables": variables}
    )

    if response.status_code == 200:
        data = response.json()
        cwe_list = data.get("data", {}).get("securityAdvisory", {}).get("cwes", {}).get("nodes", [])
        if cwe_list:
            return [(cwe["cweId"], cwe["name"]) for cwe in cwe_list]
        else:
            return []
    else:
        print("ERRORE")
        exit(2)


# Funzione per elaborare i file nella cartella Vulnerabilities
def process_vulnerabilities_files():
    input_dir = "Vulnerabilities"
    output_dir = "Vulnerabilities_with_CWE"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)

        if not file_name.endswith(".json"):
            continue

        with open(input_file_path, "r") as file:
            data = json.load(file)

        print(f"Analize: {file_name}")
        for package, details in data.items():
            for vulnerability in details.get("vulnerabilities", []):
                ghsa_id = vulnerability.get("id")
                cwes = get_cwe_from_ghsa(ghsa_id)

                if cwes:
                    # Aggiungi il primo CWE trovato
                    vulnerability["CWE_ID"] = cwes[0][0]
                    vulnerability["CWE_DESCRIPTION"] = cwes[0][1]
                else:
                    print(ghsa_id +" NON HA CWE")
                    vulnerability["CWE_ID"] = "N/A"
                    vulnerability["CWE_DESCRIPTION"] = "N/A"

        with open(output_file_path, "w") as file:
            json.dump(data, file, indent=4)

# Esegui il processo
def main():
    process_vulnerabilities_files()

if __name__ == "__main__":
    main()

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Gestisce le opzioni -f e -r.")
    parser.add_argument('-f', metavar='file', type=str, help='Esegui la scansione su file.')
    parser.add_argument('-r', metavar='cartella', type=str, help='Esegui la scansione su repository.')

    args = parser.parse_args()

    command = ["anchore_syft"]

    if args.f:
        print("Hai selezionato l'opzione -f. Esecuzione dell'azione F.")
        PathRepo = "SBOM_Exe_Analisys"
        file_path = args.f

        if not os.path.isfile(file_path):
            print(f"Errore: Il file '{file_path}' non esiste.")
            return

        # Estrai il nome del file senza estensione
        file_name = os.path.splitext(os.path.basename(file_path))[0].replace("\\", "/")
        output_file = os.path.join(PathRepo, f"{file_name}_SBOM.json").replace("\\", "/")

        # Costruisci il comando completo
        command.extend(["scan",file_path, "-o", f"cyclonedx-json"])

    elif args.r:
        print("Hai selezionato l'opzione -r. Esecuzione dell'azione R.")
        PathRepo = "SBOM_Source_Analisys"
        repo_path = args.r

        if not os.path.isdir(repo_path):
            print(f"Errore: La cartella '{repo_path}' non esiste.")
            return

        # Estrai il nome della cartella
        folder_name = os.path.basename(os.path.normpath(repo_path))
        output_file = os.path.join(PathRepo, f"{folder_name}_SBOM.json").replace("\\", "/")

        # Costruisci il comando completo
        command.extend(["scan",repo_path, "-o", f"cyclonedx-json"])

    else:
        print("Nessuna opzione selezionata. Utilizza -f <file> o -r <cartella>.")
        return

    # Esegui il comando
    try:
        print(f"Esecuzione del comando: {' '.join(command)}")
        with open(output_file, 'w') as file:
            subprocess.run(command, stdout=file, stderr=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")

if __name__ == "__main__":
    main()

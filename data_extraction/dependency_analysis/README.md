# 🔍 Software Dependency Vulnerability Analysis

This repository provides automated tools to **extract** and **analyze** vulnerabilities in software dependencies. It leverages **Syft** to generate **SBOMs (Software Bill of Materials)** and **Grype** to scan them for known vulnerabilities (CVEs). Additionally, it integrates **CWE classification** and produces comprehensive security reports.

## 📌 Features

✅ **Dependency extraction**: Uses **Syft** to generate SBOM files and identify software dependencies.  
✅ **Vulnerability scanning**: Uses **Grype** to analyze SBOMs and detect security vulnerabilities (CVEs).  
✅ **Vulnerability classification**: Associates CWE codes with detected vulnerabilities.  
✅ **Report generation**: Produces detailed reports in CSV and JSON formats.  
✅ **Statistical analysis**: Evaluates vulnerability severity and generates visual insights.  

## 📁 Project Structure

```
📦 SOURCEBASEMATERIALS
 ┣ 📂 SBOM_Source_Analisys        # Generated SBOM files using Syft
 ┣ 📂 Vulnerabilities             # Vulnerability reports generated with Grype
 ┣ 📂 Vulnerabilities_with_CWE    # Vulnerabilities enriched with CWE classification
 ┣ 📜 analizerInvoker.py          # Orchestrates analysis execution for multiple repositories
 ┣ 📜 CWEfinder.py                # Maps GHSA vulnerabilities to CWE codes
 ┣ 📜 vulnerability_checker.py     # Performs vulnerability detection and analysis
 ┣ 📜 sbom_extractor.py           # Uses Syft to extract SBOMs from repositories
 ┣ 📜 GraphGenerator.py            # Generates statistical visualizations for security insights
 ┣ 📜 Result_Analyzer.py           # Analyzes results and consolidates reports
 ┣ 📜 Generate_Report.py           # Creates CSV and JSON reports from security findings
 ┣ 📜 statistiche.py               # Statistical insights on detected vulnerabilities
 ┣ 📜 singleAnalyzer.py            # Runs analysis on a single repository
 ┣ 📜 high_critical_report.csv     # Report on high and critical severity vulnerabilities
 ┣ 📜 Final_report.csv             # Comprehensive report of all detected vulnerabilities
 ┣ 📜 FinalSummary.json            # JSON summary with security findings and categorization
```

---

## 🚀 Installation

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Install **Syft** and **Grype** (if not already installed)

```bash
# Install Syft
pip install syft

# Install Grype (if required)
curl -s https://raw.githubusercontent.com/anchore/grype/main/install.sh | sudo bash
```

---

## 🛠️ Usage

### 1️⃣ Generate an SBOM using Syft

Extract an **SBOM** from a **file**:

```bash
python sbom_extractor.py -f path/to/file
```

or from a **repository**:

```bash
python sbom_extractor.py -r path/to/repository
```

📌 **Output:** A SBOM file will be generated in `SBOM_Source_Analisys/`, listing all software dependencies.

---

### 2️⃣ Scan the SBOM for vulnerabilities using Grype

```bash
python analyze_sbom.py SBOM_Source_Analisys/my_project_SBOM.json
```

📌 **Output:** A vulnerability report will be created in `Vulnerabilities/my_project_Vuln.json`.

---

### 3️⃣ Enrich vulnerability data with CWE classification

```bash
python CWEfinder.py
```

📌 **Output:** Updated reports with CWE classification in `Vulnerabilities_with_CWE/`.

---

### 4️⃣ Generate final security reports

```bash
python Generate_Report.py
```

📌 **Output:** The files `Final_report.csv` and `FinalSummary.json` will be created.

---

### 5️⃣ Visualize security trends

```bash
python GraphGenerator.py
```

📌 **Output:** Various graphs will be generated to illustrate vulnerability distributions.

---

## 📊 Data Visualization

The script `GraphGenerator.py` produces visual insights on:

- **Vulnerability distribution by severity level** (Low, Medium, High, Critical).
- **Number of vulnerabilities by software category**.
- **Comparison of vulnerabilities in source code vs. dependencies**.

Graphs are saved in the `figures/` directory.

---
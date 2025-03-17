# 🔍 Shadows on the Spotless Workflow: The Vulnerability Proneness of GitHub Actions

This project performs a comprehensive vulnerability analysis in GitHub Actions, focusing on RQ1 and RQ2. It processes vulnerability data from predefined files and generates structured results for interpretation and visualization.

## 📌 Analysis Overview

The analysis addresses the following research questions:

- **RQ1. Vulnerability-Proneness and Popularity.**  
  *How does vulnerability-proneness relate to the adoption and popularity of third-party Actions?*  

- **RQ2. Vulnerability-Proneness Across Categories.**  
  *How does vulnerability-proneness relate to different GitHub Marketplace categories?*  

### 📂 Input Data

The data is sourced from the following files:

- `data/1_dependencies_sorted.csv` → Contains information about vulnerabilities in dependencies used in GitHub Actions.
- `data/1_source_code_sorted.csv` → Contains vulnerabilities detected in the source code of GitHub Actions.

### 📁 Output Results

The analysis results are stored in the following directory:

- `results/` → Contains the generated charts, tables, and reports based on the analysis.

## 🚀 Installation and Execution

### 1️⃣ Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Analysis

```bash
python main.py
```

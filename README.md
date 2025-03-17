# Shadows on the Spotless Workflow: The Vulnerability Proneness of GitHub Actions - Replication Package

This repository contains the replication package associated with the study _Shadows on the Spotless Workflow: The Vulnerability Proneness of GitHub Actions_. It provides the data, scripts, and methodologies used for data collection, vulnerability extraction, and analysis.

## Repository Structure

The repository is structured into two main sections:

### 1. Data Collection and Vulnerability Extraction
This section includes scripts and tools used to collect repository metadata and extract vulnerabilities from both source code and dependencies.

#### 1.1. Vulnerability Extraction from Source Code with CodeQL
- Uses **CodeQL** to analyze JavaScript and TypeScript-based GitHub Actions and detect security vulnerabilities.
- Extracts Common Weakness Enumerations (CWEs) and categorizes security flaws.

📂 **`data_extraction/source_code_analysis/`**  
- Scripts for cloning repositories and performing CodeQL analysis.  
- Results from vulnerability detection in source code.

#### 1.2. Vulnerability Extraction from Dependencies with Syft and Grype
- Uses **Syft** to generate a Software Bill of Materials (SBOM) for each Action.  
- Uses **Grype** to detect vulnerabilities in dependencies based on SBOM analysis.  

📂 **`data_extraction/dependency_analysis/`**  
- Scripts for SBOM generation and dependency vulnerability scanning.  
- Extracted vulnerability data from dependencies.

### 2. Data Analysis
This section contains scripts and data used to analyze the relationship between vulnerabilities and adoption trends, categorize risk levels across GitHub Marketplace, and predict vulnerability-proneness based on repository metadata.

#### 2.1. RQ1 & RQ2: Vulnerability Trends and Category-Based Analysis
- Examines how vulnerability-proneness correlates with the popularity and adoption of GitHub Actions.  
- Identifies high-risk categories in the GitHub Marketplace.  

📂 **`analysis/rq1_rq2/`**  
- Scripts for computing vulnerability metrics and performing statistical analysis.  
- Aggregated vulnerability scores and category-based risk assessments.

#### 2.2. RQ3: Predicting Vulnerability-Proneness with Contextual Information
- Investigates whether metadata from GitHub repositories can predict the vulnerability-proneness of Actions.  
- Uses machine learning models to assess security risks without direct code inspection.  

📂 **`analysis/rq3/`**  
- Feature extraction scripts from repository metadata (**Meta-Data Collection** section).  
- Models and evaluation metrics for vulnerability prediction.

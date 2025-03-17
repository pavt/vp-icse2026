# CodeQL Analysis for GitHub Repositories

## Description

This repository provides a framework for analyzing vulnerabilities in cloned GitHub repositories using **CodeQL**. It supports multiple programming languages and allows security assessments based on predefined CodeQL queries.

You can run the analysis using:
- A **standalone Python script** (`codeql_analysis.py`).
- An **interactive Jupyter Notebook** (`static_analysis_multilanguage.ipynb`).

## Requirements

### Dependencies

Before running the scripts, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Installing CodeQL

CodeQL must be installed and available in your system's `PATH`. If not installed, follow these steps:

1. Download CodeQL from the [GitHub repository](https://github.com/github/codeql).
2. Extract the contents and place them in an accessible directory, e.g., `~/codeql`.
3. Add CodeQL to your `PATH`:

   ```bash
   export PATH="$HOME/codeql:$PATH"
   ```

4. Verify the installation:

   ```bash
   codeql --version
   ```

## Usage

### Running the Analysis

#### Using the Python Script

To analyze vulnerabilities in cloned repositories using the standalone script, run:

```bash
python codeql_analysis.py --csv repos.csv --base-dir /path/to/repos --results-dir /path/to/results --num-repos 5
```

Where:
- `--csv repos.csv`: Path to the CSV file with repository details.
- `--base-dir /path/to/repos`: Directory containing cloned repositories.
- `--results-dir /path/to/results`: Directory to store analysis results.
- `--num-repos 5`: Number of repositories to analyze (optional, default is all).

#### Using the Jupyter Notebook

For an **interactive analysis**, use the `static_analysis_multilanguage.ipynb` notebook.

1. Install Jupyter if not already installed:

   ```bash
   pip install jupyter
   ```

2. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open `static_analysis_multilanguage.ipynb`, adjust parameters as needed, and run the following code:

   ```python
   import codeql_analysis as cqa

   # Define paths
   csv_file_path = '/path/to/sampled_repos.csv'  # CSV file with repository information
   base_dir = '/path/to/repos_cloned'  # Directory where repositories are cloned
   results_dir = '/path/to/multi_language_results'  # Directory to store CodeQL results

   # Run the analysis
   cqa.run_analysis(csv_file_path, base_dir, results_dir, num_repos=304)


Replace `/path/to/...` with the actual paths in your environment.

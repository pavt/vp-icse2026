import pandas as pd
import os
from VulnerabilityDataLoader import VulnerabilityDataLoader
from VulnerabilityAggregator import VulnerabilityAggregator
from VulnerabilityAnalysis import VulnerabilityAnalysis
from VulnerabilityVisualization import VulnerabilityVisualization
from ResultHandler import ResultHandler

# Define input file paths (starting files)
data_folder = "data/"
results_folder = "results/"
os.makedirs(data_folder, exist_ok=True)
os.makedirs(results_folder, exist_ok=True)

source_file = os.path.join(data_folder, "1_source_code_sorted.csv")
dependencies_file = os.path.join(data_folder, "1_dependencies_sorted.csv")

# Step 1: Load Data
print("Step 1: Loading and merging data...")
loader = VulnerabilityDataLoader(source_file, dependencies_file, results_folder)
merged_df = loader.load_data()

# Step 2: Aggregate Vulnerabilities
print("Step 2: Aggregating vulnerabilities...")
aggregator = VulnerabilityAggregator(results_folder)
aggregated_df = aggregator.aggregate(merged_df)

# Step 3: Perform Analysis
print("Step 3: Performing statistical analysis...")
analysis = VulnerabilityAnalysis(results_folder)
stats_df = analysis.compute_statistics(aggregated_df)

# Perform Kruskal-Wallis test
kruskal_stat, kruskal_p_value = analysis.perform_kruskal_wallis_test(stats_df)
print(f"Step 3.1: Kruskal-Wallis Test - Statistic: {kruskal_stat}, p-value: {kruskal_p_value}")

# Step 4: Generate Visualizations
print("Step 4: Generating visualizations...")
results_handler = ResultHandler(results_folder)  # Use ResultHandler instance
vis = VulnerabilityVisualization(results_handler)

# Generate plots and save them as PDFs
vis.plot_boxplot(stats_df)
vis.plot_histogram(stats_df)
vis.plot_category_histograms(stats_df)
vis.plot_scatter_vulnerability_vs_components(aggregated_df)
vis.plot_cwe_distribution(aggregated_df)
vis.plot_cwe_distribution_by_category(aggregated_df)   
vis.plot_cwe_distribution_by_frequency(aggregated_df)
vis.plot_cwe_distribution_violinplot(aggregated_df)
vis.plot_vulnerability_distribution(aggregated_df)
vis.plot_vulnerability_bubble_scatter(aggregated_df)
vis.plot_cwe_category_heatmap(aggregated_df)
vis.plot_cwe_category_treemap(aggregated_df)
vis.plot_cwe_category_sunburst(aggregated_df)
vis.plot_cwe_cooccurrence_matrix(aggregated_df)


print("Process completed successfully!")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class AdvancedVisualization:
    def __init__(self, results_path="results/"):
        self.results_path = results_path
        os.makedirs(self.results_path, exist_ok=True)

    def plot_sorted_boxplot(self, df):
        """
        Generates a sorted boxplot comparing vulnerability-proneness.
        """
        category_medians = df.groupby('Category')['Vulnerability-Proneness'].median().sort_values()
        ordered_categories = category_medians.index

        df['Category'] = pd.Categorical(df['Category'], categories=ordered_categories, ordered=True)

        plt.figure(figsize=(15, 8), dpi=300)
        sns.boxplot(
            x="Category",
            y="Vulnerability-Proneness",
            hue="Data Source",
            data=df,
            palette=["#2E86C1", "#E74C3C"]
        )

        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Category")
        plt.ylabel("Vulnerability-Proneness")
        plt.title("Sorted Vulnerability-Proneness by Category")
        plt.legend(title="Data Source")

        output_file = os.path.join(self.results_path, "sorted_vulnerability_boxplot.png")
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Plot saved: {output_file}")

import os
import pandas as pd
import matplotlib.pyplot as plt

class ResultHandler:
    def __init__(self, results_path="results/"):
        self.results_path = results_path
        os.makedirs(self.results_path, exist_ok=True)

    def save_plot(self, fig, filename):
        output_path = os.path.join(self.results_path, filename)
        fig.savefig(output_path, format='pdf')
        plt.close(fig)
        print(f"Plot saved: {output_path}")

    def save_data(self, df, filename):
        df.to_csv(os.path.join(self.results_path, filename), index=False)

    def save_text(self, text, filename):
        with open(os.path.join(self.results_path, filename), "w", encoding="utf-8") as f:
            f.write(text)

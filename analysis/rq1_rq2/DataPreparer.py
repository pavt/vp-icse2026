import pandas as pd

class DataPreparer:
    def __init__(self, df):
        self.df = df

    def prepare_vulnerabilities_list(self):
        # Validación: asegúrate de que la columna existe antes de continuar
        if 'vulnerabilities_list' not in self.df.columns:
            raise ValueError("La columna 'vulnerabilities_list' no existe en el DataFrame.")

        # Procesa la columna si está presente
        self.df['vulnerabilities_list'] = self.df['vulnerabilities_list'].apply(
            lambda x: eval(x) if isinstance(x, str) and x.startswith('[') else x
        )
        return self.df

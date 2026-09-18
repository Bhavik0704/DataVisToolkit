import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        if df.empty:
            raise ValueError("CSV file is empty.")
        return df
    except Exception as e:
        raise RuntimeError("Failed to load CSV: " + str(e))

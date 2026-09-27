import pandas as pd

def load(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def infer_types(df: pd.DataFrame) -> dict:
    types = {}
    for col in df.columns:
        s = df[col]
        if pd.api.types.is_numeric_dtype(s):
            types[col] = "numeric"
        else:
            nunique = s.nunique(dropna=True)
            types[col] = "categorical" if nunique <= 50 else "text"
    return types
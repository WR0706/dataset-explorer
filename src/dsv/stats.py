import pandas as pd

def numeric_stats(s: pd.Series) -> dict:
    return {
        "count": int(s.count()),
        "mean": round(float(s.mean()), 2),
        "std": round(float(s.std()), 2),
        "min": float(s.min()),
        "median": float(s.median()),
        "max": float(s.max()),
        "缺失率": f"{s.isna().mean():.1%}",
    }

def categorical_stats(s: pd.Series) -> dict:
    vc = s.value_counts(dropna=True)
    return {
        "unique": int(s.nunique(dropna=True)),
        "mode": vc.index[0] if len(vc) else None,
        "top_values": ", ".join(f"{k}({v})" for k, v in vc.head(3).items()),
        "缺失率": f"{s.isna().mean():.1%}",
    }

def describe_all(df: pd.DataFrame, types: dict) -> dict:
    result = {}
    for col, t in types.items():
        if t == "numeric":
            result[col] = numeric_stats(df[col])
        elif t == "categorical":
            result[col] = categorical_stats(df[col])
    return result
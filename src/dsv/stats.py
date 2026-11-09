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

def categorical_stats(s: pd.Series, top_n: int = 10) -> dict:
    vc = s.value_counts(dropna=True)
    return {
        "unique": int(s.nunique(dropna=True)),
        "mode": vc.index[0] if len(vc) else None,
        "top_values": ", ".join(f"{k}({v})" for k, v in vc.head(top_n).items()),
        "缺失率": f"{s.isna().mean():.1%}",
    }

def describe_all(df: pd.DataFrame, types: dict) -> dict:
    result = {}
    for col, t in types.items():
        if t == "numeric":
            result[col] = numeric_stats(df[col])
        elif t == "categorical":
            result[col] = categorical_stats(df[col])
        elif t == "datetime":  # 新增对日期的统计
            result[col] = {
                "count": int(df[col].count()),
                "min": str(df[col].min()),
                "max": str(df[col].max()),
                "缺失率": f"{df[col].isna().mean():.1%}"
            }
    return result
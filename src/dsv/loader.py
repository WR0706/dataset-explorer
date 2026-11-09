import pandas as pd
import numpy as np

def load(path: str) -> pd.DataFrame:
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith((".xlsx", ".xls")):
        df = pd.read_excel(path)
    else:
        raise ValueError("不支持的文件格式")

    # ==========================================
    # 供应链专属数据清洗与特征工程
    # ==========================================
    print(">>> 开始供应链数据清洗...")
    initial_rows = len(df)

    # 1. 基础清洗：去除完全重复的行
    df = df.drop_duplicates()
    print(f"  - 去除重复行: 删除了 {initial_rows - len(df)} 行")

    # 2. 文本列清洗：去除首尾空格，并统一大写 (如状态列)
    for col in ['order_id', 'sku', 'supplier', 'status']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()

    # 3. 数值清洗：处理数量和单价（处理负数、缺失值）
    if 'quantity' in df.columns:
        # 将负数量视为异常，转换为 NaN，然后填充为 0
        df.loc[df['quantity'] < 0, 'quantity'] = np.nan
        df['quantity'] = df['quantity'].fillna(0)
    if 'unit_price' in df.columns:
        df['unit_price'] = df['unit_price'].fillna(0)

    # 4. 日期清洗：转换格式，并计算“延迟天数”
    date_cols = ['expected_arrival', 'actual_arrival']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce') # 无法识别的格式转为空值

    # 5. 特征工程：计算是否延迟以及延迟天数（极具业务价值）
    if 'expected_arrival' in df.columns and 'actual_arrival' in df.columns:
        df['delay_days'] = (df['actual_arrival'] - df['expected_arrival']).dt.days
        # 如果实际到达为空，说明还没到，延迟天数填空
        df['is_delayed'] = df['delay_days'].apply(lambda x: 'YES' if pd.notnull(x) and x > 0 else 'NO')

    # 6. 计算订单总价值 (特征工程)
    if 'quantity' in df.columns and 'unit_price' in df.columns:
        df['total_value'] = df['quantity'] * df['unit_price']

    print(f">>> 清洗完成！共处理 {len(df)} 行有效数据。")
    # ==========================================

    return df

def infer_types(df: pd.DataFrame) -> dict:
    # （保持你原有的代码不变）
    types = {}
    for col in df.columns:
        s = df[col]
        if pd.api.types.is_numeric_dtype(s):
            types[col] = "numeric"
        elif pd.api.types.is_datetime64_any_dtype(s):
            types[col] = "datetime"
        else:
            nunique = s.nunique(dropna=True)
            types[col] = "categorical" if nunique <= 50 else "text"
    return types
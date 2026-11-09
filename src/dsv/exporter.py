import pandas as pd
import os

def export_for_powerbi(df: pd.DataFrame, stats: dict, out_dir: str = "powerbi_data"):
    """
    将原始数据和统计结果导出为 CSV，供 Power BI 直接使用
    """
    # 如果文件夹不存在，则自动创建
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # 1. 导出原始明细数据 (PBI可以直接用它做各种切片)
    raw_path = os.path.join(out_dir, "dataset_raw.csv")
    df.to_csv(raw_path, index=False, encoding="utf-8-sig") # utf-8-sig 防止中文乱码
    print(f"[+] 原始数据已导出至: {raw_path}")

    # 2. 导出描述性统计汇总数据
    summary_rows = []
    for col, col_stats in stats.items():
        row = {"Column_Name": col}
        row.update(col_stats) # 把算出来的均值、中位数等直接拼进去
        summary_rows.append(row)
        
    summary_df = pd.DataFrame(summary_rows)
    # 处理一下类别列的 top_values 字典，转成字符串以便 PBI 读取
    if 'top_values' in summary_df.columns:
        summary_df['top_values'] = summary_df['top_values'].astype(str)

    summary_path = os.path.join(out_dir, "dataset_summary.csv")
    summary_df.to_csv(summary_path, index=False, encoding="utf-8-sig")
    print(f"[+] 统计汇总数据已导出至: {summary_path}")
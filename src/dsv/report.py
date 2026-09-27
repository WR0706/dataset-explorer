from rich.console import Console
from rich.table import Table

console = Console()

def print_report(df, types: dict, stats: dict) -> None:
    console.print(f"\n[bold cyan]数据集概览[/bold cyan]")
    console.print(f"  行数: {len(df)}  列数: {len(df.columns)}\n")

    num_cols = [c for c, t in types.items() if t == "numeric"]
    if num_cols:
        table = Table(title="数值列统计", show_lines=True)
        for h in ["列", "count", "mean", "std", "min", "median", "max", "缺失率"]:
            table.add_column(h, justify="right")
        for col in num_cols:
            s = stats[col]
            table.add_row(col, str(s["count"]), str(s["mean"]), str(s["std"]), str(s["min"]), str(s["median"]), str(s["max"]), s["缺失率"])
        console.print(table)

    cat_cols = [c for c, t in types.items() if t == "categorical"]
    if cat_cols:
        table = Table(title="类别列统计", show_lines=True)
        for h in ["列", "unique", "mode", "Top 值", "缺失率"]:
            table.add_column(h, justify="right")
        for col in cat_cols:
            s = stats[col]
            table.add_row(col, str(s["unique"]), str(s["mode"]), s["top_values"], s["缺失率"])
        console.print(table)
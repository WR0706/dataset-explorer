import sys
from .loader import load, infer_types
from .stats import describe_all
from .report import print_report
from .exporter import export_for_powerbi

def main():
    path = "examples/sample.csv"
    if len(sys.argv) > 1:
        path = sys.argv[1]

    df = load(path)
    types = infer_types(df)
    stats = describe_all(df, types)
    
    # 终端打印统计表格（保留之前的酷炫功能）
    print_report(df, types, stats)
    
    # 核心：导出给 Power BI 使用的数据！
    export_for_powerbi(df, stats)

if __name__ == "__main__":
    main()
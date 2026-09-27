import sys
from .loader import load, infer_types
from .stats import describe_all
from .report import print_report

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "examples/sample.csv"
    df = load(path)
    types = infer_types(df)
    stats = describe_all(df, types)
    print_report(df, types, stats)

if __name__ == "__main__":
    main()
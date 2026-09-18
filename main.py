import argparse
from loader import load_csv
from graphs import bar_chart, scatter_plot, grouped_bar
from utils import validate_columns

def main():
    parser = argparse.ArgumentParser(description="Data Visualization Toolkit")
    parser.add_argument("--file", required=True, help="Path to CSV file")
    parser.add_argument("--graph", required=True, choices=["bar", "scatter", "grouped"])
    parser.add_argument("--x", required=True, help="X-axis column")
    parser.add_argument("--y", nargs="+", required=True, help="Y-axis column(s)")
    parser.add_argument("--out", default="output.png", help="Output image file")

    args = parser.parse_args()

    df = load_csv(args.file)
    validate_columns(df, [args.x] + args.y)

    if args.graph == "bar":
        bar_chart(df, args.x, args.y[0], args.out)
    elif args.graph == "scatter":
        scatter_plot(df, args.x, args.y[0], args.out)
    elif args.graph == "grouped":
        grouped_bar(df, args.x, args.y, args.out)

    print(f"Graph saved to {args.out}")

if __name__ == "__main__":
    main()

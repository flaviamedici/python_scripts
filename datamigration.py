import pandas as pd
import argparse
import os

def migrate_data(source, destination, columns=None):
    try:
        # 1. Detect file type and read source
        if source.endswith('.csv'):
            df = pd.read_csv(source)
        elif source.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(source)
        else:
            print("Error: Source must be .csv or .xlsx")
            return

        # 2. Filter columns if specified
        if columns:
            available_cols = [c for c in columns if c in df.columns]
            df = df[available_cols]
            print(f"Extracted columns: {available_cols}")

        # 3. Detect output type and save
        if destination.endswith('.csv'):
            df.to_csv(destination, index=False)
        elif destination.endswith('.xlsx'):
            df.to_excel(destination, index=False)
        
        print(f"Successfully migrated {len(df)} rows to {destination}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract data from CSV/Excel and save to another file.")
    parser.add_argument("source", help="Path to the source file (.csv or .xlsx)")
    parser.add_argument("destination", help="Path to the destination file (.csv or .xlsx)")
    parser.add_argument("--cols", nargs='+', help="Optional: List specific columns to extract (e.g., --cols Name Date Total)")

    args = parser.parse_args()
    migrate_data(args.source, args.destination, args.cols)

if __name__ == "__main__":
    main()
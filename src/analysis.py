import csv

def analyze_csv(file_path):
    """Analyze CSV data from the given file path and return the number of rows."""
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        return len(data)
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        num_rows = analyze_csv(sys.argv[1])
        print(f"The CSV file contains {num_rows} rows.")
    else:
        print("Usage: python analysis.py <path_to_csv>")

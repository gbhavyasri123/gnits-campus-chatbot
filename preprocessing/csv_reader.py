import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(
            file_path,
            encoding="utf-8",
            on_bad_lines="skip"
        )

        records = []

        for _, row in df.iterrows():
            records.append(" ".join(row.astype(str)))

        return records

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []
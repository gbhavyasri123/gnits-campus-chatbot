import os
import json

from csv_reader import load_csv
from txt_reader import load_txt
from cleaner import clean_text
from chunker import create_chunks

RAW_FOLDER = "data/raw"
OUTPUT_FILE = "data/processed/all_chunks.json"

all_chunks = []
chunk_id = 1

for file_name in os.listdir(RAW_FOLDER):
    print(os.listdir(RAW_FOLDER))

    file_path = os.path.join(RAW_FOLDER, file_name)

    if file_name.endswith(".csv"):

        rows = load_csv(file_path)

        text = " ".join(rows)

    elif file_name.endswith(".txt"):

        text = load_txt(file_path)

    else:
        continue

    cleaned_text = clean_text(text)

    chunks = create_chunks(cleaned_text)

    for chunk in chunks:

        all_chunks.append({
            "chunk_id": chunk_id,
            "content": chunk,
            "source": file_name
        })

        chunk_id += 1

os.makedirs("data/processed", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=4)

print(f"Generated {len(all_chunks)} chunks")
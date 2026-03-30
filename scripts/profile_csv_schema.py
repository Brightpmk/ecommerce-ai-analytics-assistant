from __future__ import annotations

from pathlib import Path
import json

import pandas as pd

from app.schema_profiler import profile_dataframes
from scripts.load_csvs import FILE_TABLE_MAPPING

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"


def load_raw_dataframes() -> dict[str, pd.DataFrame]:
    dataframes: dict[str, pd.DataFrame] = {}

    for filename, table_name in FILE_TABLE_MAPPING.items():
        file_path = RAW_DIR / filename
        if not file_path.exists():
            continue
        dataframes[table_name] = pd.read_csv(file_path)

    return dataframes


def main() -> None:
    dataframes = load_raw_dataframes()
    if not dataframes:
        print("No CSV files found in data/raw for configured mappings.")
        return

    profile = profile_dataframes(dataframes)
    print(json.dumps(profile.to_dict(), indent=2))


if __name__ == "__main__":
    main()

"""Кэш набора для исследовательских скриптов: out/cache.pkl (снимки, метки, размер пикселя).

    python experiments/make_cache.py --data /path/to/НД_для_обучения
"""

import argparse
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dxa.data import load_dataset

ap = argparse.ArgumentParser()
ap.add_argument("--data", required=True)
images = load_dataset(ap.parse_args().data)
Path("out").mkdir(exist_ok=True)
pickle.dump(images, open("out/cache.pkl", "wb"))
print(f"out/cache.pkl: {len(images)} снимков")

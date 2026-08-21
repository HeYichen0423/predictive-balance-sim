import os
import pandas as pd


def save_csv(data, filename):
    os.makedirs(
        "results/data",
        exist_ok=True
    )

    df = pd.DataFrame(data)

    df.to_csv(
        f"results/data/{filename}",
        index=False
    )
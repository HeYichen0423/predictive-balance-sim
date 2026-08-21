import pandas as pd
import os


DATA_DIR = "results/data"
OUTPUT_DIR = "paper"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# =========================
# Delay Table
# =========================

def generate_delay_table():
    file = os.path.join(
        DATA_DIR,
        "delay_result.csv"
    )

    df = pd.read_csv(file)

    latex = df.to_latex(
        index=False,
        float_format="%.3f"
    )

    with open(
        os.path.join(
            OUTPUT_DIR,
            "delay_table.tex"
        ),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(latex)


# =========================
# Prediction Table
# =========================

def generate_prediction_table():
    file = os.path.join(
        DATA_DIR,
        "prediction_result.csv"
    )

    df = pd.read_csv(file)

    latex = df.to_latex(
        index=False,
        float_format="%.3f"
    )

    with open(
        os.path.join(
            OUTPUT_DIR,
            "prediction_table.tex"
        ),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(latex)


# =========================
# Noise Table
# =========================

def generate_noise_table():
    file = os.path.join(
        DATA_DIR,
        "noise_result.csv"
    )

    df = pd.read_csv(file)

    latex = df.to_latex(
        index=False,
        float_format="%.3f"
    )

    with open(
        os.path.join(
            OUTPUT_DIR,
            "noise_table.tex"
        ),
        "w",
        encoding="utf-8"
    ) as f:
        f.write(latex)


if __name__ == "__main__":
    print("Generating LaTeX tables...")
    generate_delay_table()
    generate_prediction_table()
    generate_noise_table()
    print("Tables generated!")
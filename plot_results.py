"""
Plot all experiment results

Generate figures for paper:

1. Delay robustness
2. Prediction horizon sensitivity
3. Noise robustness
4. Recovery performance
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


# ============================
# Directory
# ============================

DATA_DIR = "results/data"
FIGURE_DIR = "results/figures"

os.makedirs(
    FIGURE_DIR,
    exist_ok=True
)


# ============================
# Delay RMSE
# ============================

def plot_delay():
    filename = os.path.join(
        DATA_DIR,
        "delay_result.csv"
    )

    if not os.path.exists(filename):
        print(
            "Missing delay_result.csv"
        )
        return

    data = pd.read_csv(filename)

    plt.figure(
        figsize=(7,5)
    )

    plt.plot(
        data["delay_ms"],
        data["PD_RMSE"],
        marker="o",
        label="PD"
    )

    plt.plot(
        data["delay_ms"],
        data["Predict_RMSE"],
        marker="o",
        label="Predictive"
    )

    plt.plot(
        data["delay_ms"],
        data["Dynamic_RMSE"],
        marker="o",
        label="Dynamic Predictive"
    )

    plt.xlabel(
        "Delay (ms)"
    )

    plt.ylabel(
        "RMSE (deg)"
    )

    plt.title(
        "Delay Robustness"
    )

    plt.grid(
        True
    )

    plt.legend()

    plt.savefig(
        os.path.join(
            FIGURE_DIR,
            "delay_rmse.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================
# Prediction horizon
# ============================

def plot_prediction():
    filename = os.path.join(
        DATA_DIR,
        "prediction_result.csv"
    )

    if not os.path.exists(filename):
        print(
            "Missing prediction_result.csv"
        )
        return

    data = pd.read_csv(filename)

    plt.figure(
        figsize=(7,5)
    )

    plt.plot(
        data["prediction_ms"],
        data["RMSE"],
        marker="o"
    )

    plt.xlabel(
        "Prediction horizon (ms)"
    )

    plt.ylabel(
        "RMSE (deg)"
    )

    plt.title(
        "Prediction Horizon Sensitivity"
    )

    plt.grid(
        True
    )

    plt.savefig(
        os.path.join(
            FIGURE_DIR,
            "prediction_horizon.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================
# Noise robustness
# ============================

def plot_noise():
    filename = os.path.join(
        DATA_DIR,
        "noise_result.csv"
    )

    if not os.path.exists(filename):
        print(
            "Missing noise_result.csv"
        )
        return

    data = pd.read_csv(filename)

    plt.figure(
        figsize=(7,5)
    )

    plt.plot(
        data["noise_deg"],
        data["PD_RMSE"],
        marker="o",
        label="PD"
    )

    plt.plot(
        data["noise_deg"],
        data["Predict_RMSE"],
        marker="o",
        label="Predictive"
    )

    plt.plot(
        data["noise_deg"],
        data["Dynamic_RMSE"],
        marker="o",
        label="Dynamic Predictive"
    )

    plt.xlabel(
        "Noise level (deg)"
    )

    plt.ylabel(
        "RMSE (deg)"
    )

    plt.title(
        "Noise Robustness"
    )

    plt.grid(
        True
    )

    plt.legend()

    plt.savefig(
        os.path.join(
            FIGURE_DIR,
            "noise_robustness.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================
# Recovery experiment
# ============================

def plot_recovery():
    filename = os.path.join(
        DATA_DIR,
        "recovery_result.csv"
    )

    if not os.path.exists(filename):
        print(
            "Missing recovery_result.csv"
        )
        return

    data = pd.read_csv(filename)

    plt.figure(
        figsize=(7,5)
    )

    controllers = [
        "PD",
        "Predict",
        "Dynamic"
    ]

    for controller in controllers:
        controller_data = data[
            data["controller"]
            ==
            controller
        ]

        plt.plot(
            controller_data["initial_angle"],
            controller_data["recovery_time_ms"],
            marker="o",
            label=controller
        )

    plt.xlabel(
        "Initial angle (deg)"
    )

    plt.ylabel(
        "Recovery time (ms)"
    )

    plt.title(
        "Recovery Performance"
    )

    plt.grid(
        True
    )

    plt.legend()

    plt.savefig(
        os.path.join(
            FIGURE_DIR,
            "recovery_time.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# ============================
# Main
# ============================

if __name__ == "__main__":
    print(
        "Generating figures..."
    )

    plot_delay()
    plot_prediction()
    plot_noise()
    plot_recovery()

    print(
        "All figures generated."
    )
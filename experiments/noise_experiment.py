"""
Noise robustness experiment

Evaluate controller robustness
under measurement noise.

Multiple runs are averaged
to reduce randomness.
"""

import numpy as np
import config

from experiments.common import simulate
from utils.metrics import rmse
from utils.save import save_csv


# ==========================
# Fix random seed
# ==========================

# Ensure reproducible results
np.random.seed(42)


def run_noise():
    results = []

    # number of repeated experiments
    repeat = 20

    for noise in config.noise_list:
        pd_values = []
        pred_values = []
        dynamic_values = []

        for i in range(repeat):
            # ======================
            # PD controller
            # ======================
            pd_data = simulate(
                "PD",
                delay_time=0.1,
                noise=noise
            )

            # ======================
            # First-order prediction
            # ======================
            pred_data = simulate(
                "Predict",
                delay_time=0.1,
                prediction_time=0.1,
                noise=noise
            )

            # ======================
            # Dynamic prediction
            # ======================
            dynamic_data = simulate(
                "Dynamic",
                delay_time=0.1,
                prediction_time=0.1,
                noise=noise
            )

            pd_values.append(
                np.degrees(
                    rmse(pd_data)
                )
            )

            pred_values.append(
                np.degrees(
                    rmse(pred_data)
                )
            )

            dynamic_values.append(
                np.degrees(
                    rmse(dynamic_data)
                )
            )

        # ==========================
        # Average results
        # ==========================

        pd_rmse = np.mean(
            pd_values
        )

        pred_rmse = np.mean(
            pred_values
        )

        dynamic_rmse = np.mean(
            dynamic_values
        )

        print(
            f"""
Noise:
{noise} deg

PD:
{pd_rmse:.3f} deg

Predictive:
{pred_rmse:.3f} deg

Dynamic:
{dynamic_rmse:.3f} deg
"""
        )

        results.append(
            {
                "noise_deg":
                    noise,

                "PD_RMSE":
                    pd_rmse,

                "Predict_RMSE":
                    pred_rmse,

                "Dynamic_RMSE":
                    dynamic_rmse
            }
        )

    # save csv
    save_csv(
        results,
        "noise_result.csv"
    )

    return results
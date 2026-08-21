"""
Delay robustness experiment

Purpose:
Compare controller performance under different feedback delays.

Prediction horizon:
Tp = delay
"""

import numpy as np
import config

from experiments.common import simulate
from utils.metrics import rmse
from utils.save import save_csv


def run_delay():
    results = []

    for delay in config.delay_list:
        print(
            f"\nTesting delay {delay*1000:.0f} ms"
        )

        # PD controller
        pd_data = simulate(
            "PD",
            delay
        )

        # First-order prediction
        pred_data = simulate(
            "Predict",
            delay,
            prediction_time=delay
        )

        # Dynamic prediction
        dynamic_data = simulate(
            "Dynamic",
            delay,
            prediction_time=delay
        )

        pd_rmse = np.degrees(
            rmse(pd_data)
        )

        pred_rmse = np.degrees(
            rmse(pred_data)
        )

        dynamic_rmse = np.degrees(
            rmse(dynamic_data)
        )

        print(
            f"""
PD RMSE:
{pd_rmse:.3f} deg

Predictive RMSE:
{pred_rmse:.3f} deg

Dynamic RMSE:
{dynamic_rmse:.3f} deg
"""
        )

        results.append(
            {
                "delay_ms":
                    delay*1000,

                "PD_RMSE":
                    pd_rmse,

                "Predict_RMSE":
                    pred_rmse,

                "Dynamic_RMSE":
                    dynamic_rmse
            }
        )

    # save result
    save_csv(
        results,
        "delay_result.csv"
    )

    print(
        "\nDelay experiment finished."
    )

    return results
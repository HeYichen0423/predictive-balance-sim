"""
Prediction horizon sensitivity experiment

Study relationship between:

prediction_time

and

control performance
"""

import numpy as np
import config

from experiments.common import simulate
from utils.metrics import rmse
from utils.save import save_csv


np.random.seed(42)


def run_prediction():
    results = []

    for prediction_time in config.prediction_list:
        data = simulate(
            "Predict",
            delay_time=0.1,
            prediction_time=prediction_time
        )

        error = np.degrees(
            rmse(data)
        )

        print(
            f"""
Prediction:

{prediction_time*1000:.0f} ms

RMSE:

{error:.3f} deg
"""
        )

        results.append(
            {
                "prediction_ms":
                    prediction_time*1000,

                "RMSE":
                    error
            }
        )

    save_csv(
        results,
        "prediction_result.csv"
    )

    return results
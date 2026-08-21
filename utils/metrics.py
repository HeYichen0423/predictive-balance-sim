import numpy as np
import config


def rmse(data):
    """
    Root Mean Square Error

    Ignore initial transient response.
    """
    data = np.asarray(data)

    # remove first 1 second
    # avoid influence of initial angle
    start = int(
        1.0 / config.dt
    )

    steady_data = data[start:]

    return np.sqrt(
        np.mean(
            steady_data ** 2
        )
    )
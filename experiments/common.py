"""
Common simulation function

Includes:

- delayed measurement
- noise
- low-pass filtering
- controller simulation
"""

import numpy as np
import config

from model.controller import (
    PD,
    Predictive,
    DynamicPredictive
)
from model.dynamics import update


def simulate(
        controller_type,
        delay_time,
        prediction_time=0,
        noise=0):

    steps = int(
        config.simulation_time
        /
        config.dt
    )

    delay_steps = int(
        delay_time
        /
        config.dt
    )

    # =========================
    # initial state
    # =========================

    theta = np.radians(
        config.initial_angle
    )
    omega = 0.0

    # =========================
    # delay buffer
    # =========================

    state_buffer = [
        (theta, omega)
    ] * (
        delay_steps + 1
    )

    # =========================
    # low pass filter
    # =========================

    alpha = 0.8
    filtered_theta = theta
    filtered_omega = omega

    theta_history = []

    for i in range(steps):
        # =========================
        # delayed measurement
        # =========================

        raw_theta, raw_omega = (
            state_buffer[0]
        )

        # =========================
        # sensor noise
        # =========================

        noisy_theta = (
            raw_theta
            +
            np.radians(
                np.random.normal(
                    0,
                    noise
                )
            )
        )

        # gyro noise
        # increase from 0.1 to 0.5
        # closer to real MEMS IMU
        noisy_omega = (
            raw_omega
            +
            np.radians(
                np.random.normal(
                    0,
                    noise * 0.5
                )
            )
        )

        # =========================
        # filtering
        # =========================

        if noise > 0:
            filtered_theta = (
                alpha * filtered_theta
                +
                (1-alpha)
                * noisy_theta
            )

            filtered_omega = (
                alpha * filtered_omega
                +
                (1-alpha)
                * noisy_omega
            )
        else:
            # no noise:
            # do not introduce artificial delay
            filtered_theta = noisy_theta
            filtered_omega = noisy_omega

        delayed_theta = filtered_theta
        delayed_omega = filtered_omega

        # =========================
        # controller
        # =========================

        if controller_type == "PD":
            u = PD(
                delayed_theta,
                delayed_omega
            )

        elif controller_type == "Predict":
            u = Predictive(
                delayed_theta,
                delayed_omega,
                prediction_time
            )

        elif controller_type == "Dynamic":
            # acceleration estimation
            # only use delayed information
            estimated_acceleration = (
                config.system_strength
                *
                delayed_theta
            )

            u = DynamicPredictive(
                delayed_theta,
                delayed_omega,
                estimated_acceleration,
                prediction_time
            )

        else:
            raise ValueError(
                "Unknown controller type"
            )

        # =========================
        # physical update
        # =========================

        theta, omega, a = update(
            theta,
            omega,
            u
        )

        theta_history.append(
            theta
        )

        # =========================
        # update delay buffer
        # =========================

        state_buffer.append(
            (
                theta,
                omega
            )
        )

        if len(state_buffer) > delay_steps + 1:
            state_buffer.pop(0)

    return np.array(theta_history)
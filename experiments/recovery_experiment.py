"""
Recovery time experiment

Test recovery ability under
different initial disturbances.

Controllers:

1. PD
2. First-order Predictive
3. Dynamic Predictive


Recovery criterion:

|theta| < 1 degree

and remain stable for 0.25 seconds.

The reported recovery time is:

the first moment entering
the stable region,

NOT the end of the confirmation window.
"""

import numpy as np
import config

from model.controller import (
    PD,
    Predictive,
    DynamicPredictive
)
from model.dynamics import update
from utils.save import save_csv


def simulate_recovery(
        controller_type,
        initial_angle,
        delay_time=0.1,
        prediction_time=0.1):

    dt = config.dt

    # =========================
    # Initial state
    # =========================

    theta = np.radians(
        initial_angle
    )
    omega = 0.0

    # =========================
    # Delay buffer
    # =========================

    delay_steps = int(
        delay_time / dt
    )

    state_buffer = [
        (theta, omega)
    ] * (
        delay_steps + 1
    )

    # =========================
    # Recovery condition
    # =========================

    threshold = np.radians(
        1.0
    )

    # remain stable for 0.25s
    required_stable_steps = int(
        0.25 / dt
    )

    stable_count = 0

    # =========================
    # Simulation length
    # =========================

    steps = int(
        config.simulation_time
        /
        dt
    )

    for i in range(steps):
        # =====================
        # delayed measurement
        # =====================

        delayed_theta, delayed_omega = (
            state_buffer[0]
        )

        # =====================
        # Controller
        # =====================

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
                "Unknown controller"
            )

        # =====================
        # Physical update
        # =====================

        theta, omega, a = update(
            theta,
            omega,
            u
        )

        # =====================
        # Recovery check
        # =====================

        if abs(theta) < threshold:
            stable_count += 1
        else:
            stable_count = 0

        if stable_count >= required_stable_steps:
            # Return the first moment
            # when entering stable region,
            # remove confirmation window.

            return (
                (i - required_stable_steps + 1)
                *
                dt
                *
                1000
            )

        # =====================
        # Update delay buffer
        # =====================

        state_buffer.append(
            (
                theta,
                omega
            )
        )

        if len(state_buffer) > delay_steps + 1:
            state_buffer.pop(0)

    # =========================
    # Not recovered
    # =========================

    return (
        config.simulation_time
        *
        1000
    )


def run_recovery():
    results = []

    # Initial disturbances
    initial_angles = [
        5,
        10,
        15,
        20
    ]

    controllers = [
        "PD",
        "Predict",
        "Dynamic"
    ]

    for angle in initial_angles:
        print(
            "\n===================="
        )
        print(
            f"Initial angle: {angle} deg"
        )
        print(
            "===================="
        )

        for controller in controllers:
            recovery_time = simulate_recovery(
                controller_type=controller,
                initial_angle=angle,
                delay_time=0.1,
                prediction_time=0.1
            )

            print(
                f"{controller}: "
                f"{recovery_time:.1f} ms"
            )

            results.append(
                {
                    "initial_angle":
                        angle,

                    "controller":
                        controller,

                    "recovery_time_ms":
                        recovery_time
                }
            )

    save_csv(
        results,
        "recovery_result.csv"
    )

    return results
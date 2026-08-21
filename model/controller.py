"""
Controller algorithms

Controllers:

1. PD
2. First-order predictive
3. Dynamic predictive
"""

import config


def PD(theta, omega):
    """
    Conventional PD controller
    """
    return (
        -config.Kp * theta
        -config.Kd * omega
    )


def Predictive(theta, omega, prediction_time):
    """
    First-order prediction

    theta_future =
        theta + omega*T
    """
    theta_predict = (
        theta
        + omega * prediction_time
    )

    return (
        -config.Kp * theta_predict
        -config.Kd * omega
    )


def DynamicPredictive(
        theta,
        omega,
        acceleration,
        prediction_time):
    """
    Second-order prediction

    theta_future =
        theta
        + omega*T
        + 0.5*a*T^2
    """
    theta_predict = (
        theta
        + omega * prediction_time
        + 0.5
        * acceleration
        * prediction_time ** 2
    )

    return (
        -config.Kp * theta_predict
        -config.Kd * omega
    )
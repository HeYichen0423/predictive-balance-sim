"""
System dynamics model

Inverted balance system:

theta'' = k*theta + u
"""

import config


def acceleration(theta, control):
    """
    Natural unstable dynamics + control input

    theta'' = k*theta + u
    """
    return (
        config.system_strength * theta
        + control
    )


def update(theta, omega, control):
    """
    Symplectic Euler integration
    """
    a = acceleration(theta, control)

    # update angular velocity first
    omega_new = omega + a * config.dt

    # then update angle
    theta_new = theta + omega_new * config.dt

    return theta_new, omega_new, a
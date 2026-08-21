"""
Global configuration

Predictive Balance Simulation
"""

# =========================
# Simulation parameters
# =========================

# simulation timestep
dt = 0.005        # seconds

# total simulation time
simulation_time = 5.0   # seconds


# =========================
# Initial condition
# =========================

# initial tilt angle
initial_angle = 8.0   # degree


# =========================
# Physical parameters
# =========================

# inverted pendulum instability coefficient
# theta'' = k*theta + u
system_strength = 2.0


# =========================
# Controller parameters
# =========================

Kp = 8.0
Kd = 2.0


# =========================
# Measurement filter
# =========================

# Enable low-pass filter
# True:
#   simulate real embedded sensor processing
#
# False:
#   ideal measurement without filtering
ENABLE_FILTER = True

# LPF coefficient
# y(k)=alpha*y(k-1)+(1-alpha)x(k)
filter_alpha = 0.8


# =========================
# Experiment parameters
# =========================

# Delay experiment
delay_list = [
    0.00,
    0.02,
    0.04,
    0.06,
    0.08,
    0.10,
    0.12,
    0.14,
    0.16,
    0.18,
    0.20
]

# Prediction horizon experiment
prediction_list = [
    0.00,
    0.01,
    0.02,
    0.03,
    0.04,
    0.05,
    0.06,
    0.08,
    0.10,
    0.12,
    0.15,
    0.20,
    0.25,
    0.30,
    0.40
]

# Noise experiment
noise_list = [
    0.0,
    0.5,
    1.0,
    2.0,
    3.0,
    5.0
]
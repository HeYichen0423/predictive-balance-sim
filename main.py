from experiments.delay_experiment import run_delay
from experiments.prediction_experiment import run_prediction
from experiments.noise_experiment import run_noise
from experiments.recovery_experiment import run_recovery


if __name__ == "__main__":
    print("====================")
    print("Predictive Balance Simulation")
    print("====================")

    print("\nRunning Delay Experiment")
    run_delay()

    print("\nRunning Prediction Experiment")
    run_prediction()

    print("\nRunning Noise Experiment")
    run_noise()

    print("\nRunning Recovery Experiment")
    run_recovery()

    print("\nALL DONE")
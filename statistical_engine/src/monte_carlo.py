# src/monte_carlo.py

import random

def simulate_crashes(days):
    """
    Simulates server crashes with 4.5% probability.
    """
    crash_probability = 0.045
    crashes = 0

    for _ in range(days):
        if random.random() < crash_probability:
            crashes += 1

    return crashes / days

if __name__ == "__main__":
    for days in [30, 365, 10000]:
        prob = simulate_crashes(days)
        print(f"Days: {days}, Simulated Crash Rate: {prob}")
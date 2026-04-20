import numpy as np

def single_cycle(t, A, P):
    return A * np.sin(2 * np.pi * t / P)

def life_curve(t, params):
    y = (
        single_cycle(t, params["A1"], params["P1"]) +
        single_cycle(t, params["A2"], params["P2"]) +
        single_cycle(t, params["A3"], params["P3"])
    )
    trend = params["trend"] * t
    noise = np.random.normal(0, 0.2, len(t))
    return y + trend + noise
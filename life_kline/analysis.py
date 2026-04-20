import numpy as np

def analyze_trend(values):
    slope = np.polyfit(range(len(values)), values, 1)[0]
    volatility = np.std(values)

    if slope > 0:
        direction = "Uptrend 📈"
    else:
        direction = "Downtrend 📉"

    return {
        "slope": slope,
        "volatility": volatility,
        "direction": direction
    }
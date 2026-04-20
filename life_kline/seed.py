import datetime
import numpy as np

def generate_parameters(birthday: str):
    date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    seed = int(date.strftime("%Y%m%d"))
    np.random.seed(seed)

    params = {
        "P1": np.random.randint(20, 40),
        "P2": np.random.randint(80, 150),
        "P3": np.random.randint(300, 600),
        "A1": np.random.uniform(0.5, 1.5),
        "A2": np.random.uniform(0.5, 1.5),
        "A3": np.random.uniform(0.5, 1.5),
        "trend": np.random.uniform(-0.001, 0.002)
    }
    return params
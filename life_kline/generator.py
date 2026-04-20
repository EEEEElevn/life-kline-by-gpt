import numpy as np
import datetime

def generate_time_series(birthday: str, days=10000):
    start = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    t = np.arange(days)
    dates = [start + datetime.timedelta(days=int(i)) for i in t]
    return t, dates
import matplotlib.pyplot as plt

def plot_life_kline(dates, values, birthday):
    plt.figure(figsize=(12,6))
    plt.plot(dates, values)
    plt.title(f"Life K-Line Simulation ({birthday})")
    plt.xlabel("Date")
    plt.ylabel("Life Index")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("life_kline.png")
    plt.show()
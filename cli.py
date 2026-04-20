import argparse
from life_kline.seed import generate_parameters
from life_kline.generator import generate_time_series
from life_kline.model import life_curve
from life_kline.analysis import analyze_trend
from life_kline.visualization import plot_life_kline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--birthday", required=True, help="Format: YYYY-MM-DD")
    args = parser.parse_args()

    params = generate_parameters(args.birthday)
    t, dates = generate_time_series(args.birthday)
    values = life_curve(t, params)

    result = analyze_trend(values)

    print("==== Life K-Line Analysis ====")
    print(f"Trend: {result['direction']}")
    print(f"Slope: {result['slope']:.6f}")
    print(f"Volatility: {result['volatility']:.4f}")

    plot_life_kline(dates, values, args.birthday)

if __name__ == "__main__":
    main()
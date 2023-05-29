import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf


def fetch_historical_data(symbols, start_date, end_date):
    """
    Fetches historical price data for the given symbols using yfinance.

    Args:
        symbols (list): List of symbols to fetch data for.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    """
    data = yf.download(symbols, start=start_date, end=end_date)
    return data["Close"]


def generate_correlation_heatmap(symbols, start_date, end_date):
    """
    Generates a correlation heatmap of the given symbols' price data

    Args:
        symbols (list): List of symbols to generate the heatmap for.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    """
    # Fetch historical price data for the symbols
    data_frame = fetch_historical_data(symbols, start_date, end_date)

    # Calculate the correlation matrix
    corr_matrix = data_frame.corr()

    # Create a heatmap using Seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        cbar=True,
        annot_kws={"fontsize": 10, "fontweight": "bold", "color": "black"},
    )
    plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
    plt.xlabel("Symbols", fontsize=12)
    plt.ylabel("Symbols", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()


symbols = ["BTC-USD", "ETH-USD", "EOS-USD", "ADA-USD", "NEO-USD", "XRP-USD"]
start_date = "2020-01-01"
end_date = pd.Timestamp.today().strftime("%Y-%m-%d")

generate_correlation_heatmap(symbols, start_date, end_date)

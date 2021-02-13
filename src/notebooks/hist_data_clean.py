import pandas as pd
import datetime as dt

btc_daily = pd.read_csv(
    '/Users/henry/code/projects/bot_trading/data/binance_BTCUSDT_1d_2017-01-01.csv')

# DELETE ----------------------------------------------------
btc_daily.head()
# DELETE ----------------------------------------------------

# As daily pricing, timestamp col = close_timestamp so convert to datetime and drop both
btc_daily['date'] = [dt.date.fromtimestamp(
    x / 1000) for x in btc_daily['timestamp']]
btc_daily.drop(columns=['timestamp', 'close_timestamp'], inplace=True)

# Calculate true range


def true_range(high, low, prev_close):
    todays_range = high - low
    todays_max_gain = abs(high - prev_close)
    todays_max_loss = abs(low - prev_close)

    true_range = max(todays_range, todays_max_gain, todays_max_loss)

    return true_range


btc_daily['prev_close'] = btc_daily['close'].shift(1)

btc_daily['true_range'] = btc_daily.apply(lambda x: true_range(
    x['high'], x['low'], x['prev_close']), axis=1)


# Calculate ATR
btc_daily['ATR_14'] = btc_daily['true_range'].ewm(alpha=1/14).mean()
btc_daily['ATR_20'] = btc_daily['true_range'].ewm(alpha=1/20).mean()
btc_daily['ATR_55'] = btc_daily['true_range'].ewm(alpha=1/55).mean()

# Calculate basic entries
# Add short term don't enter if prev breakout was winner later
# Long entries
btc_daily['sys1_a_long_entry'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=14).max()
btc_daily['sys1_b_long_entry'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=20).max()
btc_daily['sys2_long_entry'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=55).max()

# Short entries
btc_daily['sys1_a_short_entry'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=14).min()
btc_daily['sys1_b_short_entry'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=20).min()
btc_daily['sys2_short_entry'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=55).min()

# Calculate exits
# Long exits
btc_daily['sys1_a_long_exit'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=10).max()
btc_daily['sys1_b_long_exit'] = btc_daily['low'] > btc_daily['lowhigh'].shift(
    1).rolling(window=10).max()
btc_daily['sys2_long_exit'] = btc_daily['low'] > btc_daily['low'].shift(
    1).rolling(window=20).max()

# Short entries
btc_daily['sys1_a_short_exit'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=14).min()
btc_daily['sys1_b_short_exit'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=20).min()
btc_daily['sys2_short_exit'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=55).min()
btc_daily

# ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ----
# ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ----

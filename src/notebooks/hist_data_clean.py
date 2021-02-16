# TODO
# [] Refactor
# [] Add tests

import re
import numpy as np
import datetime as dt
import pandas as pd

btc_daily = pd.read_csv(
    '/Users/henry/code/projects/bot_trading/data/binance_BTCUSDT_1d_2017-01-01.csv')

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

# Calculate stops
# Long stops
# Strategy 1
# Stop = 2ATR
btc_daily['stop'] = btc_


# Generalise:
Window:
stop strategy: normal / whipsaw


btc_daily['sys1_a_long_exit'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=10).max()
btc_daily['sys1_b_long_exit'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=10).max()
btc_daily['sys2_long_exit'] = btc_daily['low'] < btc_daily['low'].shift(
    1).rolling(window=20).max()

# Short stops
btc_daily['sys1_a_short_exit'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=14).min()
btc_daily['sys1_b_short_exit'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=20).min()
btc_daily['sys2_short_exit'] = btc_daily['high'] > btc_daily['high'].shift(
    1).rolling(window=55).min()

# Positions
btc_daily['sys1_a_long_pos'] = np.nan
btc_daily.loc[btc_daily['sys1_a_long_entry'], 'sys1_a_long_pos'] = 1
btc_daily.loc[btc_daily['sys1_a_long_exit'], 'sys1_a_long_pos'] = 0
btc_daily['sys1_a_long_pos'].fillna(method='ffill', inplace=True)

# ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ----
# ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ---- ---- TESTING ----


def establish_positions(df, entry_col, exit_col, direction='long', position_col='position'):
    # Check cols in df
    assert entry_col in df.columns, 'Entry column not in dataframe'
    assert exit_col in df.columns, 'Exit column not in dataframe'

    # Create empty column for binary position flag - 1 = buy/holding, 0 = sell/not holding
    df[position_col] = np.nan

    # Act when entry indicated:
    # If long, set position col = 1
    if direction == 'long':
        df.loc[btc_daily[entry_col], position_col] = 1
    # If short, set position col = -1
    elif direction == 'short':
        df.loc[btc_daily[entry_col], position_col] = -1

    # Sell when exit indicated: if exit col = True, set position col = 0
    df.loc[btc_daily[exit_col], position_col] = 0

    # If nan, maintain previous position
    df[position_col].fillna(method='ffill', inplace=True)


strategies = ['sys1_a', 'sys1_b', 'sys2']
directions = ['long', 'short']

for sd in [s + '_' + d for d in directions for s in strategies]:

    # Find direction
    if re.search(r'short', sd):
        direction = 'short'
    else:
        direction = 'long'

    establish_positions(
        btc_daily, f'{sd}_entry', f'{sd}_exit', direction, f'{sd}_pos')


# Trade costs

# Bet sizing


btc_daily.head(100).to_csv('btc_test.csv')

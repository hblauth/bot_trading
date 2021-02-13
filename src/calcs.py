def true_range(high, low, prev_close):
    todays_range = (high - low)
    todays_max_gain = abs(high - prev_close)
    todays_max_loss = abs(low - prev_close)

    true_range = max(todays_range, todays_max_gain, todays_max_loss)

    return true_range

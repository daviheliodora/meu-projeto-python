import pandas as pd
import numpy as np

def calculate_ema(data, period=20):
    """
    Calculate the Exponential Moving Average (EMA) for the given period.
    """
    data['EMA'] = data['Close'].ewm(span=period, adjust=False).mean()
    return data

def generate_signals(data):
    """
    Generate buy/sell signals based on trend filter and breakout strategy.
    """
    signals = []
    max_operations_per_day = 3
    operating_hours = ("09:00", "17:00")

    daily_operations = {}

    for i in range(1, len(data)):
        current_date = data['Date'].iloc[i]
        current_time = data['Time'].iloc[i]

        if current_time < operating_hours[0] or current_time > operating_hours[1]:
            continue

        daily_operations.setdefault(current_date, 0)
        if daily_operations[current_date] >= max_operations_per_day:
            continue

        ema = data['EMA'].iloc[i]
        prev_high = data['High'].iloc[i - 1]
        prev_low = data['Low'].iloc[i - 1]
        prev_close = data['Close'].iloc[i - 1]

        if prev_close > ema and data['High'].iloc[i] > prev_high:
            signals.append({
                'datetime': f"{current_date} {current_time}",
                'type': 'buy',
                'entry_price': prev_high,
                'stop_loss': prev_low,
                'take_profit': prev_high + 2 * (prev_high - prev_low)
            })
            daily_operations[current_date] += 1

        elif prev_close < ema and data['Low'].iloc[i] < prev_low:
            signals.append({
                'datetime': f"{current_date} {current_time}",
                'type': 'sell',
                'entry_price': prev_low,
                'stop_loss': prev_high,
                'take_profit': prev_low - 2 * (prev_high - prev_low)
            })
            daily_operations[current_date] += 1

    return pd.DataFrame(signals)
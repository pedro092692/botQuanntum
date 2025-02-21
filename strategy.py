import pandas as pd
import pandas_ta as ta


class Strategy:
    def __init__(self, symbol_data):
        self.df = symbol_data

    def check_long_signal(self, over_bought_rsi, over_sold_rsi):
        # add long signal column to df
        self.df['long_signal'] = ''

        for index in range(len(self.df)):
            # check for long signal in data
            if (over_bought_rsi > self.df['rsi'].iloc[index] > over_sold_rsi) and \
                    (self.df['low'].iloc[index - 1] < self.df['lbb'].iloc[index - 1]) and \
                    (self.df['low'].iloc[index] > self.df['lbb'].iloc[index]):

                # check if last 5 candles there was a doji
                for i in range(1, 5):
                    if self.df['CDL_DOJI_10_0.1'].iloc[index - i] == 100:
                        self.df.loc[index, 'long_signal'] = 'Buy'
                        break

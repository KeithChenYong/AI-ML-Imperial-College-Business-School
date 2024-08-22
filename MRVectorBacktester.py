# Adopted fom Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
from MomVectorBacktester import *


class MRVectorBacktester(MomVectorBacktester):
    ''' Class for the vectorized backtesting of
    Mean Reversion-based trading strategies.

    Attributes
    ==========
    symbol: str
        RIC symbol with which to work with
    start: str
        start date for data retrieval
    end: str
        end date for data retrieval
    amount: int, float
        amount to be invested at the beginning
    tc: float
        proportional transaction costs (e.g. 0.5% = 0.005) per trade

    Methods
    =======
    get_data:
        retrieves and prepares the base data set
    run_strategy:
        runs the backtest for the mean reversion-based strategy
    plot_results:
        plots the performance of the strategy compared to the symbol
    '''

    def __init__(self, symbol, data, start, end, amount, tc):
        self.symbol = symbol
        self.data = data.loc[start:end]  # Filter the data within the start and end dates
        self.amount = amount
        self.tc = tc
        self.results = None
        self.get_data()

    def get_data(self):
        ''' Prepares the data. '''
        raw = pd.DataFrame(self.data[self.symbol])
        raw.rename(columns={self.symbol: 'price'}, inplace=True)
        raw['return'] = np.log(raw['price'] / raw['price'].shift(1))
        self.data = raw

    def run_strategy(self, SMA, threshold):
        ''' Backtests the trading strategy. '''
        data = self.data.copy().dropna()
        data['sma'] = data['price'].rolling(SMA).mean()
        data['distance'] = data['price'] - data['sma']
        data.dropna(inplace=True)
        
        # Use .loc[] to avoid chained assignment warnings
        data.loc[data['distance'] > threshold, 'position'] = -1  # Sell signals
        data.loc[data['distance'] < -threshold, 'position'] = 1  # Buy signals
        data.loc[data['distance'] * data['distance'].shift(1) < 0, 'position'] = 0  # Crossing signals
        
        data['position'] = data['position'].ffill().fillna(0)
        data['strategy'] = data['position'].shift(1) * data['return']
        
        # Determine when a trade takes place
        trades = data['position'].diff().fillna(0) != 0
        data.loc[trades, 'strategy'] -= self.tc  # Subtract transaction costs
        
        data['creturns'] = self.amount * data['return'].cumsum().apply(np.exp)
        data['cstrategy'] = self.amount * data['strategy'].cumsum().apply(np.exp)
        self.results = data
        
        # Absolute performance of the strategy
        aperf = self.results['cstrategy'].iloc[-1]
        # Out-/underperformance of strategy
        operf = aperf - self.results['creturns'].iloc[-1]
        
        return round(aperf, 2), round(operf, 2)


if __name__ == '__main__':
    mrbt = MRVectorBacktester('GDX', '2010-1-1', '2020-12-31',
                              10000, 0.0)
    print(mrbt.run_strategy(SMA=25, threshold=5))
    mrbt = MRVectorBacktester('GDX', '2010-1-1', '2020-12-31',
                              10000, 0.001)
    print(mrbt.run_strategy(SMA=25, threshold=5))
    mrbt = MRVectorBacktester('GLD', '2010-1-1', '2020-12-31',
                              10000, 0.001)
    print(mrbt.run_strategy(SMA=42, threshold=7.5))

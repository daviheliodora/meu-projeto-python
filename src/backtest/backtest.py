class BacktestResults:
    def __init__(self):
        self.trades = []  # List to hold individual trade results
        self.daily_results = {}  # Dictionary to hold results per day

    def add_trade(self, profit_loss, date):
        self.trades.append({'profit_loss': profit_loss, 'date': date})
        if date in self.daily_results:
            self.daily_results[date] += profit_loss
        else:
            self.daily_results[date] = profit_loss

    def total_profit_loss(self):
        return sum(trade['profit_loss'] for trade in self.trades)

    def daily_performance(self):
        return self.daily_results

    def drawdown(self):
        peak = float('-inf')
        max_drawdown = 0
        for trade in self.trades:
            if trade['profit_loss'] > peak:
                peak = trade['profit_loss']
            current_drawdown = peak - trade['profit_loss']
            max_drawdown = max(max_drawdown, current_drawdown)
        return max_drawdown

# Example usage
if __name__ == "__main__":
    backtest = BacktestResults()
    # Example trades, add your own logic here
    backtest.add_trade(100, '2023-04-01')
    backtest.add_trade(-50, '2023-04-01')
    backtest.add_trade(200, '2023-04-02')
    
    print(f"Total Profit/Loss: {backtest.total_profit_loss()}")
    print(f"Daily Performance: {backtest.daily_performance()}")
    print(f"Maximum Drawdown: {backtest.drawdown()}")
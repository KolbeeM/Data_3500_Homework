import json


def meanReversionStrategy(prices):
    buy = 0 # Stores the price you bought at
    first_buy = 0 # This stores the very first buy price (it helps us calculate % of return at the end)
    total_profit = 0 # Keeps a running total of all profits across trades
    holding = False # lets us know if we are currently holding the stock or not.

    for i in range(5, len(prices)):
        price = prices[i] # todays price
        avg = sum(prices[i-5:i]) / 5 # The average of the previous 5 days

        if price < avg * 0.98 and not holding: # buys when price drops more than 2% below the average
            buy = price
            holding = True
            if first_buy == 0:
                first_buy = buy
            print("BUYING  at $" + str(round(buy, 2)))

        elif price > avg * 1.02 and holding: # Sells when the price is 2% above the average.
            profit = price - buy
            total_profit += profit
            holding = False
            print("SELLING at $" + str(round(price, 2)))

        else:
            pass

    if holding: # If we haven't sold because the price hasn't gone up 2%.
        print("Still holding at $" + str(round(prices[-1], 2)) + " — position not closed.")

    print("-" * 60)
    if first_buy == 0:
        print("No trades were made.")
        returns = 0.0
    else:
        returns = round((total_profit / first_buy) * 100, 2)
        print("First buy price: $" + str(round(first_buy, 2)))
        print("Total profit:    $" + str(round(total_profit, 2)))
        print("Final profit %:  " + str(returns) + "%")

    return round(total_profit, 2), returns # the profit in dollars and percentage are returned to us

def simpleMovingAverageStrategy(prices):
    buy = 0 # same as the first Strategy
    first_buy = 0 # Same 
    total_profit = 0 # Same
    holding = False # Same

    for i in range(5, len(prices)):
        price = prices[i]
        avg = sum(prices[i-5:i]) / 5
        # Buys when price goes above the average. With expectation of going up still.
        if price > avg and not holding:
            buy = price
            holding = True
            if first_buy == 0:
                first_buy = buy
            print("BUYING  at $" + str(round(buy, 2)))
        # Selling when the price goes below the average. with expectation of it going down still.
        elif price < avg and holding:
            profit = price - buy
            total_profit += profit
            holding = False
            print("SELLING at $" + str(round(price, 2)))

        else:
            pass

    if holding: # If we haven't sold due to it not going below the average.
        print("Still holding at $" + str(round(prices[-1], 2)) + " — position not closed.")

    print("-" * 60)
    if first_buy == 0:
        print("No trades were made.")
        returns = 0.0
    else:
        returns = round((total_profit / first_buy) * 100, 2)
        print("First buy price: $" + str(round(first_buy, 2)))
        print("Total profit:    $" + str(round(total_profit, 2)))
        print("Final profit %:  " + str(returns) + "%")

    return round(total_profit, 2), returns

# This opens my Json file and writes dictionary into it.
# I had Claude Help me create this portion of my assignment.
# Prompt: "Help me build a code to Build JSON and add all 10 stocks given."
def saveResults(results):
    with open("/workspaces/Data_3500_Homework/hw5/results.json", "w") as f:
        json.dump(results, f, indent=4)
    print("\nAll results saved to results.json")

# create list to store 10 tickers
tickers = ["AAPL", "GOOG", "ADBE", "TSLA", "BA", "CMCSA", "CSCO", "CVX", "JPM", "V"]

# create dictionary called results to store prices, profits and return percentages
results = {}

for ticker in tickers: # loops through all 10 stocks at one time
    
    file = open("/workspaces/Data_3500_Homework/hw5/" + ticker + ".txt")
    lines = file.readlines()
    prices = []
    for line in lines:
        if line.strip() != "":
            prices.append(round(float(line), 2))

    # Run Mean Reversion strategy
    print("\n" + "="*60)
    print("  MEAN REVERSION  —  " + ticker)
    print("="*60)
    means_reversion_profit, means_reversion_returns = meanReversionStrategy(prices)
 
    # run simple moving average strategy
    print("\n" + "="*60)
    print("  SIMPLE MOVING AVERAGE  —  " + ticker)
    print("="*60)
    simple_means_average_profit, simple_means_average_returns = simpleMovingAverageStrategy(prices)
 
    # store results
    
    results[ticker + "_prices"] = prices
    results[ticker + "_simple_means_average_profit"] = simple_means_average_profit
    results[ticker + "_simple_means_average_returns"] = simple_means_average_returns
    results[ticker + "_means_reversion_profit"] = means_reversion_profit
    results[ticker + "_means_reversion_returns"] = means_reversion_returns
 
saveResults(results)
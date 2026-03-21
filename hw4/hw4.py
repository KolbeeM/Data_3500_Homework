file = open("/workspaces/Data_3500_Homework/hw4/Tesla.txt")

lines = file.readlines()
prices = []
for line in lines:
    if line.strip() != "":
        price = float(line)
        price = round(price, 2)
        prices.append(price)

buy = 0
first_buy = 0
total_profit = 0
holding = False

for i in range(5, len(prices)):
    current_price = prices[i]

    avg_price = sum(prices[i-5:i]) / 5

    if current_price < avg_price * 0.98 and not holding:   # not holding = don't own it yet, so BUY
        buy = current_price
        holding = True

        if first_buy == 0:
            first_buy = buy

        print("BUYING  at $" + str(round(buy, 2)) + "  |  5-day avg: $" + str(round(avg_price, 2)))

    elif current_price > avg_price * 1.02 and holding:     # holding = we own it, so SELL
        profit = current_price - buy
        total_profit += profit
        holding = False

        print("SELLING at $" + str(round(current_price, 2)) + "  |  5-day avg: $" + str(round(avg_price, 2)) + "  |  Trade profit: $" + str(round(profit, 2)) + "  |  Total profit: $" + str(round(total_profit, 2)))


if first_buy == 0:
    print("No trades were made. Try lowering the threshold further.")
else:
    final_profit_percentage = (total_profit / first_buy) * 100
    print("-----------------------")
    print("\nFirst buy price: $" + str(round(first_buy, 2)))
    print("Total profit:    $" + str(round(total_profit, 2)))
    print("Final profit %:  " + str(round(final_profit_percentage, 2)) + "%")
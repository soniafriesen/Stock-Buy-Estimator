import stockInvestment

print("Stock sell/buy estimator by Sonia Friesen and Roberto Davies-Amaral 2021")
print()
sentences = stockInvestment.ReadFile()
data = ""
total = 0.00
for line in sentences:
    if(line != "<<End>>"):
        data = data + " " + line 
    else:
        total += stockInvestment.get_stock_investment(data)
        data = ""
overallTotal = "{:,}$".format(total, 'USD', locale='en_US')
print()
print(f'Total Requests: {overallTotal}')
print()

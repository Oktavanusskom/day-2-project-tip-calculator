print("Welcome to the tip calulator.")
totalBill = input("What was the total bill? $")
percentageTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
manyPeopleSplit = input("How many people to split the bill? ")

percentageTipGive = int(percentageTip)/100
totalBillGive = float(totalBill) * percentageTipGive
eachPersonPay = round((float(totalBill) + totalBillGive)/int(manyPeopleSplit), 2)

print(f"Each person should pay: ${eachPersonPay}")

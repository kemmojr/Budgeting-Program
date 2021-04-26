def divideIncomeAmount(amount, diff):
    tAccounts = {}
    vAccounts = {}
    tAccounts['giving'], tAccounts['life'], tAccounts['car'], tAccounts['spending'], tAccounts['everyday'] = "{:.2f}".format(0.1*amount), "{:.2f}".format(0.35*amount), "{:.2f}".format(0.25*amount), "{:.2f}".format(0.2*amount), "{:.2f}".format(0.1*amount)
    vAccounts['giving'], vAccounts['life'], vAccounts['car'], vAccounts['spending'], vAccounts['everyday'] = "{:.2f}".format(0.1*amount), "{:.2f}".format(0.35*amount), "{:.2f}".format(0.25*amount), "{:.2f}".format(0.2*amount), "{:.2f}".format(0.1*amount)
    accounts = [tAccounts, vAccounts]

    print(f'The Tim values add to one: {checkIfValuesCorrect(accounts[0], amount)}')
    print(f'The Vanessa values add to one: {checkIfValuesCorrect(accounts[1], amount)}')
    
    
    print(f"Giving: ${accounts[diff]['giving']}")
    print(f"Life Saver: ${accounts[diff]['life']}")
    print(f"Car: ${accounts[diff]['car']}")
    print(f"Spending Savings: ${accounts[diff]['spending']}")
    print(f"Everyday Expenses: ${accounts[diff]['everyday']}")
    #  print("Specific purpose: $"+(0.1*amount))


def checkIfValuesCorrect(dict, amount):
    sum = 0.0
    for i in dict:
        sum += float(dict[i])/amount
    
    return sum

paySlip = float(input("Please enter the amount of money that you have earned that you wish to have divided: "))
diff = 1 # 0 is Tim, 1 is Vanessa
divideIncomeAmount(paySlip, 1)
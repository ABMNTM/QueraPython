income = int(input())
tax = 0
pureIncomes = []

while income != 0:
    if income <= 1000000:
        tax = 0
    elif income <= 5000000:
        tax = income / 10
    else:
        tax = income / 5
    pureIncomes.append(int(income - tax))
    income =  int(input())

for PI in pureIncomes:
    print(PI)
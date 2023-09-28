
investment=float(input("Please enter Investment: "))
rate=float(input("Please enter anualized input rate: ")) * .01
balance=investment
i = 0
while balance < investment * 2:
  balance = balance + (balance*float(rate))
  i += 1
print(f"Years it will take: {str(i)}")
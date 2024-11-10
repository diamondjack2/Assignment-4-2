

employeeName = str(input("Enter Employee Name: "))
numOfShifts = int(input("Enter Number of Shifts Worked: "))
numOfTrans = int(input("Enter Number of Transactions: "))
transValue = float(input("Enter Total Dollar Value of Transactions: "))
bonus = 0 

averageTransValue = transValue / numOfTrans

productScore = averageTransValue / numOfShifts

if productScore <= 30:
    bonus += 50.00

elif productScore <= 69:
    bonus += 75.00
elif productScore <= 199:
    bonus += 100.00
else:
    bonus += 200.00

print("Employee Name:", employeeName)
print("Employee Bonus:", bonus)


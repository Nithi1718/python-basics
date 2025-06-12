###Calculator
num1=float(input("Enter the first number: "))
operator=input("Enter the operator (+,-,*./): ")
num2=float(input("Enter the second number: "))
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    if num2!=0:
        result=num1/num2
    else:
        print("The number cant divided by zero")
else:
    print("invalid operator")
print("Result: ", result)


### ATM withdrawl rules
balance = 10000
amount = int(input("Enter the amount: "))
if amount <= balance:
    if amount%100==0:
        print("Transaction successful")
    else:
        print("Enter the rupees in multiples of 100")
else:
    print("Your account balance is low")

#Election voters checking
age=float(input("Enter the age: "))
if age>=18:
    print("The voter is eligible to vote")
else:
    print("""Voter is minor
Voter is ineligible to vote""")
print("He need", 18-age, "years to be a major")
empty_list=list()
print(empty_list)
empty=[]
print(empty)

#Creating the list with 5 items
lst=["apple","banana","orange","mango","cherry"]
print(len(lst))         #finding length of the list is 5
print(lst[::2])

#input all type of data types in the list
name="Kavin"
age=44
height=6.7
marital_status="single"
address="chennai"
mixed_data_types=[f"{name}, {age}, {height}, {marital_status}, {address}"]
print(mixed_data_types)

#list of IT companies
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print("Number of companies in the list: ", len(it_companies))
print(it_companies)
print(it_companies[::3])
it_companies[0]="Zoho"
print(it_companies)
it_companies.append("TCS")
it_companies.insert(4, "HCL")
print(it_companies)
it_companies[0]="FACEBOOK"
print(it_companies)
str=["#;"]
print(it_companies+str)
print("Google" in it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[3])
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.pop(0)
print(it_companies)
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.pop(3)
print(it_companies)
it_companies.clear()
print(it_companies)
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
del it_companies
print(it_companies)
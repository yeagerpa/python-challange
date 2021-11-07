from pprint import pprint 
analysis = ""
filename = "C:\\Users\\Paul\\Documents\\GitHub\\python-challange\\PyBank\\Resources\\budget_data.csv"
records = []
lines = []

for line in open(filename):
    lines.append(line)
for line in lines[1:]:
    date, amount = line.strip().split(",")
    records.append([date, int(amount)])
months = len(records)
analysis += f"number of months is {months}\n"
pprint(records)
total = 0       
for record in records:
    date, amount = record 
    total += amount 
analysis += f"total profit/losses is {total}\n"
avg = total/months 
analysis += f"avg profit/losses is {avg}\n"




# A function that returns the length of the value:
def myFunc(record):
    date, amount = record 
    return (amount)

records.sort(reverse=True, key=myFunc)
largest_change = records[0]
analysis += f"largest change is {largest_change}"

# records.sort(key=myFunc)
smallest_change = records[-1]
analysis += f"smallest change is {smallest_change}"


print(analysis)
with open("analysis.txt", "w") as file:
    file.write(analysis)
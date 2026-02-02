import random
import csv

#X VARIABLE
x_data = []
for x in range(100):
    X=round(random.uniform(0,3),2)
    x_data.append(X)
print(x_data)

#Y VARIABLE
y_data = []
for xvalue in x_data:
    noise= random.uniform(-1,1)
    Y= 4 + 3 * xvalue + noise
    y_data.append(Y)

#Z VARIABLE
z_data = []
for c in y_data:
    if c >= 7:
        label="Highly Affected"
    else:
        label="Less Affected"
    z_data.append(label)
print(x_data)
print(y_data)
print(z_data)
with open("rule_based_AI.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["Equipment_Affected","Incident_Cost","Impact_Lable"])
    rows=zip(x_data,y_data,z_data)
    writer.writerows(rows)
print("CSV FILE CREATED!")

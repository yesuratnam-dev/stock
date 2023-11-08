val = ["X0017RVYET",
"X0017RVYEJ",
"X0016YBTCP",
"X00189TBM3",
"X001FTO7FR",
"X00189OUWT",
"X001A522X5",
"X001ED8AM5",
"X0018FVB3J",
"X001A4ZMZ1",
"X0017RZHZB",
"X00189TBLT",
"X0017RT92X",
"X001NF1K0X",
"X0017RVYF3",
"X00183XE7R",
"X001EB3JFZ",
"X001EB3LNF"]

lis = []

var = "https://butane.efp.amazonoperations.app/inventory/research?itemIdentifier=X0017RVYET&warehouses=TQZV&inventoryType=fnSku"

for i in range(len(val)):
    lis.append(var.replace("X0017RVYET", val[i]))

print(lis)

list1 = []
list2 = []
for i in range(len(lis)):
        list1.append(lis[i].replace("TQZV", "YET5"))
        list2.append(lis[i].replace("TQZV", "TPXV"))

list1.extend(list2)

print(list1)

import csv

with open('inventoryData.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["efp"])
    writer.writerows([list1])
      
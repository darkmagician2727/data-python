open_file = open("c:/Users/Tj/Desktop/devmountain/data-python/CupcakeInvoices.csv")

for row in open_file:
    print(row)   

open_file.close()
open_file = open("c:/Users/Tj/Desktop/devmountain/data-python/CupcakeInvoices.csv")

for row in open_file:
    print(row.split(",")[2])


open_file.close()
open_file = open("c:/Users/Tj/Desktop/devmountain/data-python/CupcakeInvoices.csv")


for row in open_file:
    print(float((row.split(",")[3])) * float((row.split(",")[4])))

open_file.close()
open_file = open("c:/Users/Tj/Desktop/devmountain/data-python/CupcakeInvoices.csv")

total = 0
for row in open_file:
    total += (float((row.split(",")[3])) * float((row.split(",")[4])))
    
print(total)
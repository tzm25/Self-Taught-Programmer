import csv

with open ("/home/void/Self-Taught Programmer Course/test.csv","w", newline="") as f:
    write = csv.writer(f, delimiter= ",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])
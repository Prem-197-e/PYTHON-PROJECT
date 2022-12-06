#input
IP = input("enter inputs to process: ").split(" ")
print(IP)

#adding first of each string to output

op =" "
for i in IP:
    op = op + i[0]

#converting to upper

print(op.upper())

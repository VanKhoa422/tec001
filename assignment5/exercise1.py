l=[]
while True:
    uinput=int(input("Nhap so can sap xep: "))
    if uinput=="":
        break
    l.append(uinput)
    l.sort(reverse=True)
print(l)
def pizza_price(psize, pprice):
    return ((psize/100)*(psize/100)*3.14)/pprice
psize1=float(input("Enter the first pizza's diameter(cm):"))
pprice1=float(input("Enter the first pizza's price(USD):"))
psize2=float(input("Enter the second pizza's diameter(cm):"))
pprice2=float(input("Enter the second pizza's price(USD):"))
pizza1=pizza_price(psize1, pprice1)
pizza2=pizza_price(psize2, pprice2)
if pizza1==pizza2:
    print("Both pizzas are equal in value.")
elif pizza1>pizza2:
    print("First pizza worths more than second pizza!")
else:
    print("Second pizza worths more than first pizza!")
talent=float(input("Enter Talent: "))
pound=float(input("Enter Pounds: "))
lot=float(input("Enter Lots: "))
gr=((32*((20*talent)+pound))+lot)*13.3
kg=gr/1000
print("The weight in modern units:", gr, "grams, or", kg, "kilograms")
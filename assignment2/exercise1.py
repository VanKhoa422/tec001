def zmeasure():
    zlength=float(input("Enter your caught zander's length in centimeters: "))
    if zlength<42.0:
        miss=42.0-zlength
        print("Your zander is", miss,"centimeters lacking. Please release it back into the lake.")
    else:
        print("Your zander meets the size limit.")
zmeasure()
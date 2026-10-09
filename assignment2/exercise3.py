def hemoglobin():
    sex=input("Enter your biological gender (M/F): ")
    hemval=float(input("Enter your hemoglobin value (in g/l): "))
    if sex=="F":
        if hemval>155:
            print("Your hemoglobin value is high!")
        elif hemval<155 and hemval>117:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is low!")
    elif sex=="M":
        if hemval>167:
            print("Your hemoglobin value is high!")
        elif hemval<167 and hemval>134:
            print("Your hemoglobin value is normal.")
        else:
            print("Your hemoglobin value is low!")
    else:
        print("Invalid gender input!")
hemoglobin()
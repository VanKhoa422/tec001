def cabin():
    cclass=input("Enter your assigned cruise ship cabin class:")
    if cclass=="LUX":
        print("Your cabin is an uppder-deck cabin with balcony.")
    elif cclass=="A":
        print("Your cabin is above the car deck with a window.")
    elif cclass=="B":
        print("Your cabin is a windowless cabin above the car deck.")
    elif cclass=="C":
        print("Your cabin is a windowless cabin below the car deck.")
    else:
        print("Your cabin class doesn't exist.")
cabin()
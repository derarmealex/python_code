from re import findall
while True:
    lb = input("Enter libres: ").strip()
    if findall('[^0-9.]', lb) or lb == '0' or lb == '.' or lb in '':
        print("Enter a correct number!")
    else:
        print(lb, "lb is", round(float(lb) / 2.2, 2), "kg", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                exit()

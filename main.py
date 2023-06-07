intOper = abs(int(input("\n\tOperation.\n\tEnter number: ")))

if intOper == 1:
    print("\nTask 1")
    ind = 1
    while True:
        print("\n" + str(ind) + " - ITERATION")
        intA = float(input("\tEnter value A = "))
        intB = float(input("\tEnter value B = "))
        if intA + intB == 0.0:
            print("\nA + B = 0. " + "STOP. EXIT")
            break
        else:
            print("SUM:\t\tA + B = ", intA + intB)
            print("SUBTRACT:\tA - B = ", intA - intB)
            print("MULTY:\t\tA * B = ", intA * intB)
            print("DIVISION:\tA + B = ", end='')
            if intB == 0:
                print("\"DIVIDE ON \"" + str(intB) + "\" IS FORBIDDEN!\"")
            else:
                print(round((intA/intB), 3))
            print("POWER:\t\tA + B = ", intA + intB)
        ind += 1
elif intOper == 2:
    print("\n\tTask 2")
elif intOper == 3:
    print("\n\tTask 3")
else:
    print("NO OPERATION SELECTED")
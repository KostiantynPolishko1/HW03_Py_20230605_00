print("\nTask 1")
ind = 0
while True:
    ind += 1
    print("\n" + str(ind) + " - ITERATION")
    intA = float(input("\tEnter value A = "))
    intB = float(input("\tEnter value B = "))
    if abs(intA) + abs(intB) == 0.0:
        print("\nA & B = 0.\nSTOP. EXIT")
        break
    else:
        print("SUM:\t\tA + B -> " + str(intA) + " + " + str(intB) + " = ", intA + intB)
        print("SUBTRACT:\tA - B -> " + str(intA) + " - " + str(intB) + " = ", intA - intB)
        print("MULTY:\t\tA x B -> " + str(intA) + " x " + str(intB) + " = ", intA * intB)
        print("DIVISION:\tA / B -> " + str(intA) + " / " + str(intB) + " = ", end='')
        if intB == 0:
            print("\"DIVIDE ON \"" + str(intB) + "\" IS FORBIDDEN!\"")
        else:
            print(round((intA / intB), 3))
        print("POWER:\t\tA ^ B -> " + str(intA) + " ^ " + str(intB) + " = ", intA ** intB)

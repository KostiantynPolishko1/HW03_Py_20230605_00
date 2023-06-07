print("\n\tTask 2")
print("\nARITHMETICAL OPERATIONS:")
print("1 - SUM\n2 - SUBTRACT\n3 - MULTY\n4 - DIVISION"
      "\n5 - FLOOR DIVISION\n6 - MODULO\n7 - POWER")

ind = 0

while True:
    ind += 1
    print("\n" + str(ind) + " - ITERATION")

    indOp = input("Enter num operation: ")
    indOp = abs(int(indOp))
    if indOp == 0 or indOp > 7:
        print("\tERROR!\n\tENTER NUMBER from 1...to...7")
        continue

    intA = float(input("\tEnter value A = "))
    intB = float(input("\tEnter value B = "))
    if abs(intA) + abs(intB) == 0.0:
        print("\nA & B = 0.\nSTOP. EXIT")
        break

    if indOp == 1:
        print("SUM:\tA + B = ", intA + intB)
    elif indOp == 2:
        print("SUBTRACT:\tA - B = ", intA - intB)
    elif indOp == 3:
        print("MULTY:\tA * B = ", intA * intB)
    elif indOp == 4 or indOp == 5 or indOp == 6:
        if intB == 0:
            print("\"DIVIDE ON \"" + str(int(intB)) + "\" IS FORBIDDEN!\"")
        else:
            if indOp == 4:
                print("DIVISION:\tA / B = ", round((intA / intB), 3))
            elif indOp == 5:
                print("FLOOR DIV.:\tA // B = ", round((intA // intB), 3))
            elif indOp == 6:
                print("MODULO:\tA % B = ", round((intA % intB), 3))
    else:
        print("POWER:\tA ^ B = ", round((intA ** intB),3))
print("\n\tTask 3")
intVal = float(input("Enter int value > 1 or < -1: "))
intVal = int(intVal)
intFn1 = 0
intFn2 = 1
intSum = 0
ind = 0

if intVal == 0:
    print("\tFIBONACCI NUM: 0")
elif intVal == 1 or intVal == -1:
    print("\tFIBONACCI NUM: 0 1")
else:
    print("\tFIBONACCI NUM: {} {} ". format(intFn1, intFn2), end='')
    while ind < abs(intVal) - 1:
        if intVal > 1:
            intSum = intFn1+intFn2
        elif intVal < -1:
            intSum = intFn1 - intFn2
        print(intSum, end=' ')
        intFn1 = intFn2
        intFn2 = intSum
        ind += 1
    else:
        print("\n\tNUMBER: (" + str(intVal) + ") = FIBONACCI (" + str(intSum) + ")")
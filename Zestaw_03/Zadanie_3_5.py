def zadanie_3_5(x):
    result = "|...."*x + "|"
    result = result + "\n"
    for i in range(x+1):
        result = result + str(i)
        if i <9:
            result += "    "
        elif i < 99:
            result +="   "
        elif i < 999:
            result +="  "
        elif i < 9999:
            result +=" "

    return result.rstrip()

print(zadanie_3_5(9999))
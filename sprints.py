def MyFunc(listOfNumbers, listOfFloat):
    float = -1.0
    total = 0
    mean = []
    for a in listOfNumbers:
        if type(a) == type(1):
            if a % 2 == 0:
                mean.append(a)
                total = total + a


    for b in listOfFloat:
        if type(b) == type(0.0):
            if b > float:
                float = b
    
    if float == -1.0 or len(mean) == 0:
        return 0
    
    return (total//len(mean), float)
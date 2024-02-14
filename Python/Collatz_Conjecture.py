def steps(number):
    step = 0
    if int(number)>=1:
        while(number!=1): 
            if(number % 2 == 0):
                number = number/2
            else:
                number = number * 3 + 1
            step = step +1
        return step
    elif int(number)<1:
        raise ValueError("Only positive integers are allowed")
        

    
    

def is_armstrong_number(number:int)->bool:
    arm = str(number)
    lenght = len(arm)
    sum = 0
    for digit in arm:
        sum += int(digit)**lenght
    return sum == number

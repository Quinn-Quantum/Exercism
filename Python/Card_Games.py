"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
from statistics import mean

def get_rounds(number):
    return [number, number +1, number +2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2



def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return mean(hand)


def approx_average_is_average(hand):
    avg = card_average(hand)
    return ((hand[0]+hand[-1])/2 == avg) or (hand[len(hand)//2] == avg) 


def average_even_is_average_odd(hand):

    evenAverges = 0
    oddAverages = 0
    lisEven = []
    listOdd = []
    for i in range(len(hand)):
        if i % 2:
            lisEven.append(hand[i])
        else:
            listOdd.append(hand[i])
    evenAverges = card_average(lisEven)
    oddAverages = card_average(listOdd)

    return True if evenAverges == oddAverages else False



def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 11 * 2
    return hand

#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Copyright (c) 2020 Achim Barczok (achim@barczok.de)
All rights reserved.

Solves number puzzles in the style of Heinz Böer

"""

import math
import logging

# some debug options
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


# define, how a dice can look like and how its calculated
class Dice:
    """ At every position, a dice is placed """
    def __init__(self, side, calc, fact):
        if side in range(1, 7):
            self.side = side
        else:
            print("Ungültiger Würfel")

        if calc in range(0, 4):
            self.calc = calc
        else:
            print("Ungültige Berechnung")

        if fact is True:
            self.fact = True
            self.side = math.factorial(self.side)
        else:
            self.fact = False


    def __str__(self):
        if self.fact is false:
            return str(self.side)
        else:
            return(str(self.side) + "!")

    def get_fact(self):
        """ returns factorial of the dice """
        return math.factorial(self.side)

# define, what a result looks like
class Combination:
    """ a Combination consists of up to 4 dices and a result """
    def __init__(self):
        dices = []
        self.dices = dices
        order = []
        self.order = order
        calc_string = ""
        self.calc_string = calc_string

    def __str__(self):
        return self.calc_string

    def get_result(self):
        self.result = 0
        for position in self.dices:
            if position.calc == 0:
                self.result = self.result + position.side
                if self.calc_string == "":
                    self.calc_string = str(position.side)
                else:
                    self.calc_string = "(" + self.calc_string + "+" + str(position.side) + ")"
            elif position.calc == 1:
                self.result = self.result - position.side
                self.calc_string = "(" + self.calc_string + "-" + str(position.side) + ")"
            elif position.calc == 2:
                self.result = self.result * position.side
                self.calc_string = "(" + self.calc_string + "*" + str(position.side) + ")"
            elif position.calc == 3:
                self.result = self.result / position.side
                self.calc_string = "(" + self.calc_string + "/" + str(position.side) + ")"
            elif position.calc == 4:
                self.result = self.result ** position.side
                self.calc_string = "(" + self.calc_string + "**" + str(position.side) + ")"
            else:
                print("Error")
            # logging.debug(self.result)
        return self.result, self.calc_string

    def add_dice(self, dice):
        """ add a dice to the Combination """
        if len(self.dices) < 4:
            self.dices.append(dice)
        else:
            print("max. 4 Würfel pro Kombination!")

    def add_calc(self, calc):
        """ add a calculation to the Combinaction """
        if len(self.calculations) < 3:
            self.calculations.append(calc)
        else:
            print("max. 3 Berechnungen!")

def all_combinations(number1, number2, result):
    """
    Defines a set of all possible outcomes that lead to the result
    The result is a string in the format of "(1+1)*3*3"
    """

    # each number can also be used as factorial,
    # that gives up to four possible numbers for each position
    number_set = set()
    number_set.update([number1, number2, math.factorial(number1), math.factorial(number2)])

    for pos1 in number_set:
        logging.debug(pos1)
        if pos1 is result:
            logging.debug("%s ergibt %s", pos1, pos2)
        for pos2 in number_set:
            logging.debug("%s, %s", pos1, pos2)

    return ()


def main():
    """
    Solves number puzzles in the style of  Heinz Böer:
        x ? y = z
    While x and y are dice results between 1 and 6
    Each dice can be used 0, 1 or 2 times in the calculation
    Allowed are +, -, *, /, Power and Factorials
    """

    # all_combinations(1, 2, 2)

    # mit Klassen testen:
    neue_kombi = Combination()
    neue_kombi.add_dice(Dice(6,0, False))
    neue_kombi.add_dice(Dice(6,1, False))
    neue_kombi.add_dice(Dice(2,2, False))
    neue_kombi.add_dice(Dice(2,3, False))
    print(neue_kombi.get_result()[1] + "=" + str(neue_kombi.get_result()[0]))

main()

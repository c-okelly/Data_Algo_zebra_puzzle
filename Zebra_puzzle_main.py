# Author = Conor O'Kelly
# This file will contain all of the code required to solve the zebra puzzle

from Zebra_puzzle_classes import *

def main():
    variables = [["English", "Spaniard", "Ukrainian", "Norwegian", "Japanese"],
                 ["red","green","ivory","blue","yellow"],
                 ["dog","snails","fox","zebra","horse"],
                 ["Snakes and Ladders", "Cluedo", "Pictionary", "Travel the World", "Backgammon"],
                 ["Coffee","milk","orange Juice","tea","water"]]




if __name__ == '__main__':

    var_list = [1]

    for i in var_list:
        var_list.append(var_list[0] +i)
        print(i)
        if i == 10:
            break


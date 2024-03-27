"""
Create a function that will build a staircase using the underscore _ and hash # symbols. A positive value denotes the staircase's upward direction and downwards for a negative value.

Examples
staircase(3) ➞ "__#\n_##\n###"
__#
_##
###

staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######

staircase(2) ➞ "_#\n##"
_#
##

staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#
"""


def main(num):
    if num > 0:
        for i in range(1, num+1):
            print("".join(["_" for _ in range(num - i)]) + "".join(["#" for _ in range(i)]))
    elif num < 0:
        num *= (-1)
        for i in range(1, num+1):
            print("".join(["_" for _ in range(i-1)]) + "".join(["#" for _ in range(num-i + 1)]))



if __name__ == "__main__":
    # res = main(2)
    # res = main(7)
    res = main(-8)
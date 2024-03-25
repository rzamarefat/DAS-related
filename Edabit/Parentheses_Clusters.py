"""
Write a function that groups a string into parentheses clusters. Each cluster should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
Notes
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.
"""


def main(input_):
    clusters = []
    temp_cluster = ""
    balance = 0

    for char in input_:
        temp_cluster += char

        if char == "(":
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            clusters.append(temp_cluster)
            temp_cluster = ""

    return clusters



if __name__ == "__main__":
    res = main("()()()")
    print(res)
    res = main("((()))(())()()(()())")
    print(res)
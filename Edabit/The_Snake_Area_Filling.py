"""
This challenge is based on the classic videogame "Snake".

Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.

Examples
snakefill(3) ➞ 3

snakefill(6) ➞ 5

snakefill(24) ➞ 9
"""

def main(n):
    eating_times = 0

    if n == 1:
        return eating_times

    snake_lenght = 1

    while 2 * snake_lenght < n*n:
        eating_times += 1
        snake_lenght *= 2 

    return eating_times


if __name__ == "__main__":
    res = main(3)
    print(res)
    res = main(6)
    print(res)
    res = main(24)
    print(res)
"""
Create a function whose argument is the time in 12 hour format (hh:mm:ss). The function returns the smaller angle between the hour and minute hands in degrees, rounded to three decimal points.

Examples
clock("12:00:00") ➞ 0.0

clock("12:15:00") ➞ 82.5

clock("12:32:44") ➞ 179.967

clock("03:33:33") ➞ 94.525
"""


def main(time):
    hours, minutes, seconds = map(int, time.split(":"))

    hour_angle = (hours % 12) * 30 + minutes * 0.5 + seconds * (1/120)
    minute_angle = minutes * 6 + seconds * 0.1

    angle = abs(hour_angle - minute_angle)

    return min(angle, 360 - angle)





if __name__ == "__main__":
    res = main("12:00:00")
    print(res == 0.0)
    res = main("12:15:00")
    print(res == 82.5)
    res = main("12:32:44")
    print(res == 179.967)
    res = main("03:33:33")
    print(res == 94.525)
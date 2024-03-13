def switch_light(candles):
    for index, c in enumerate(candles):
        if c == 1:
            candles[0: index+1] = [0 for i in range(len(candles[0: index+1]))]
        else:
            candles[0: index+1] = [1 for i in range(len(candles[0: index+1]))]
    
    return candles


if __name__ == "__main__":
    candles = switch_light([0, 1, 0, 1, 1, 0])

    print(candles)
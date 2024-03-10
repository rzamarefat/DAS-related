def is_tandem_repeat(string):
    if len(string) % 2 != 0 or len(string) < 2:
        return False

    if string[0: int((len(string) / 2))] == string[int(len(string) / 2):]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    string = "abcabc"
    string = "aabaa"
    res = is_tandem_repeat(string)
    print(res)
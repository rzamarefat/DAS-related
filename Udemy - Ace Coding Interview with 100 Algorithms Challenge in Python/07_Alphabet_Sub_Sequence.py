def alphabet_sub_sequence(string1, string2):
    holder = []
    for char in string2:
        if not(char in string1):
            return False
        else:
            for index, c in enumerate(string1):
                if c == char:
                    
                    if len(holder) == 0:
                        holder.append(index)
                    else:    
                        if index < holder[-1]:
                            return False
                        else:
                            holder.append(index)
                
    return True

if __name__ == "__main__":
    string1 = "abcdefghijklmnopqrstuvwxyz"
    string2 = "abc"
    res = alphabet_sub_sequence(string1, string2)

    print(res)
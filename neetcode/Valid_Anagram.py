"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def main(s,t):
    if len(s) != len(t):
        return False
    
    s_hashmap = {}
    t_hashmap = {}

    for i in range(len(s)):
        if s[i] not in s_hashmap.keys():
            s_hashmap[s[i]] = 1
        else:
            s_hashmap[s[i]] += 1

        if t[i] not in t_hashmap.keys():
            t_hashmap[t[i]] = 1
        else:
            t_hashmap[t[i]] += 1

    for k, v in s_hashmap.items():
        if k not in t_hashmap.keys():
            return False
        
        if t_hashmap[k] != v:
            return False

    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    res = main(s, t)
    print(res == True)

    s = "rat"
    t = "car"
    res = main(s, t)
    print(res == False)



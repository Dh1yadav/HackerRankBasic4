def minion_game(string):
    vowel = "AEIOU"
    st = 0
    kv = 0
    x = len(string)
    for i in range(x):
        if string[i] in vowel:
            kv += x - i
        else:
            st += x - i
    if st > kv:
        print("Stuart", str(st))
    elif kv > st:
        print("Kevin", str(kv))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
def print_rangoli(size):
    rangoli = '-'.join(chr(ch) for ch in reversed(range(ord('a'), ord('a') + size)))
    l = []
    for limit in range(1, size * 2, 2):
        layer = f'{rangoli[:limit]}{rangoli[:limit - 1][::-1]}'
        l.append(f'{layer:-^{size * 4 - 3}}')
        print(l[-1])
    print('\n'.join(reversed(l[:-1])))
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
def print_formatted(number):
    n_bi = format(number,'b')
    size = len(n_bi)
    for i in range(1,n+1):
        oct_ = format(i,'o')
        hex_ = format(i,'X')
        bin_ = format(i,'b')
        
        print(str(i).rjust(size),str(oct_).rjust(size),str(hex_).rjust(size),str(bin_).rjust(size))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
def count_substring(string, sub_string):
    flag = 0
    while sub_string in string:
        a=string.find(sub_string)
        string=string[a+1:]
        flag+=1
    return flag
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
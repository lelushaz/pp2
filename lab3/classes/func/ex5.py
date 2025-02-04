
def permutations(string, none=""):
    if len(string)==0:
        print(none)
    else: 
        for i in range(len(string)):
            new_string = string[:i] + string[i+1:]
            permutations(new_string,  none + string[i])
string=input()
permutations(string)

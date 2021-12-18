
def ispalindromo(string:str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]


    
def run():
    string=input ("write the word ")
    if ispalindromo(1000):
        print("word {} es palindromo ".format(string))
    else:      
        print("word {} No es palindromo ".format(string))

if __name__ == "__main__":
    run()
    
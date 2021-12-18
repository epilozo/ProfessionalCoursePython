from datetime import date, datetime

def cowsay(func):
    def wrapper(text):
        lenght = len(text)
        print(" _" + lenght*"_" + "_ ")
        print("< " + text + " > ")
        print(" -" + lenght*"-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\       )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")
        func("Happy Cow ")
    return wrapper

@cowsay
def mytext(text):
    print(text)



if __name__ == "__main__":
     mytext("No pares de aprender!")
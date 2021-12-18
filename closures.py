
def make_repeater(n:int):
    
    def repeater(string:str):
        assert type(string) == str, "Just string is allowed"
        return string *  n
    return repeater    

def run():
    repeat_5 = make_repeater(5)
    print(repeat_5("emma "))



if __name__ == "__main__":
    run()
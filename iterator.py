

def run():
    my_list = [x for x in range(1,100) if x % 2 == 0]
    my_iter = iter(my_list)
    
    while True:
        try:
           print(next(my_iter))
        except StopIteration:
           break


if __name__ == "__main__":
    run()
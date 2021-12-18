from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print ("its " + str(time_elapsed.total_seconds()) + " seconds")
    return wrapper            
    
@execution_time   
def random_func():
    for _ in range(1,10000000):
        pass

@execution_time
def suma(a:int, b:int) -> int:
    return a + b


@execution_time
def saludo(nombre="Emma"):
    return print(f"hola {nombre}")


if __name__ == "__main__":
    suma(5,5)
    random_func()
    saludo("Maite")
    saludo()
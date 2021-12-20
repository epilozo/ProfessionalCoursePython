import time

def fibo_gener(max):
    a ,b = 0,1
    while a <= max:
        yield a
        a, b = b, a+b
        
        
        
        
if __name__ == "__main__":
     for element in fibo_gener(10):
         print(element)
         time.sleep(0.5)       
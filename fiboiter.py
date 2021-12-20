import time


class FiboIter():
    
    def __init__(self,fibo_max=None):
        self.fibo_max = fibo_max
        
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
         if self.fibo_max == None:
             
         if self.n1 + self.n2 <= self.fibo_max:
            if self.counter == 0:
                self.counter +=1
                return self.n1   
            elif self.counter == 1:
                self.counter +=1
                return self.n2
            else:
                aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, aux
                self.counter +=1
                return aux
         else:
             raise StopIteration   
  

if __name__ == "__main__":
    fibo_max = int(input("Maximium element in Fibonacci that you want to show ?"))
    fibo = FiboIter(fibo_max)
    for index, element in enumerate(fibo):
        print(element, index)
        time.sleep(0.5)
        
        
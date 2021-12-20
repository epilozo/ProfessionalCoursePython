## ejercicios con set

def run():
    my_list = ['a', 'b', 'c', 'd', 'e', 'a']
    print(my_list)
    my_set = set(my_list)
    print(my_set)

    my_set.add('f')
    print(my_set)
    
    my_set.update('1','h','k', {'a','z'})
    print(my_set)
    
    my_set.discard(10)
    print("Eliminado el elemento 10 con discard")
    print(my_set)
    
    my_set.remove('1')
    print("Eliminado el elemento 1 with remove")
    print(my_set)    
    
    my_set.pop()
    print("deleting aleatory with pop")
    print(my_set)  
    
    my_set.clear()
    print("Clearing all element of my set")
    print(my_set)  
    
    ## practicing with union, intersection, difference and difference simetric
    
    my_set1 = {1,2,3,4,5,6}
    my_set2 = {3,4,6,8,10,12}
    
    print(my_set1)
    print(my_set2)
    
    print("union both sets")
    print(my_set1 | my_set2)
      
    print("interesection both sets")
    print(my_set1 & my_set2)
    
    print("difference both sets 1 - 2")
    print(my_set1 - my_set2)  
      
    print("difference both sets 2 - 1")
    print(my_set2 - my_set1) 
    
    print("difference simetric both sets")
    print(my_set1 ^ my_set2) 
    
    
    



if __name__ == "__main__":
    run()
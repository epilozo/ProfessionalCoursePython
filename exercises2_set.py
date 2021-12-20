import random

## deleting element in a list created randomly
## using traditional method
def remove_element_inlist(data_list):
    
    data_list_without_repetead = []
    for element in data_list:
        if element not in data_list_without_repetead:
            data_list_without_repetead.append(element)
    return data_list_without_repetead        

## using sets for deleted element in a list

def remove_element_inlist_using_set(data_list):
    data_list_without_repetead = list(set(data_list))
    return data_list_without_repetead  
        
def run():
    data_list = []
    counter = 0
    while True:
          data_list.append(random.randint(1,10))
          counter += 1
          if counter > 20:
              break   
              
    print("My original list is ", data_list)        
    print("My new list usign traditional method is ", remove_element_inlist(data_list))
    print("My new list using set is ", remove_element_inlist_using_set(data_list)) 

if __name__ == "__main__":
    run()
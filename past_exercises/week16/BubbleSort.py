class BubbleSortList:

    def __init__(self, list): # O(1)
        self.list = list # O(1) 

    def sort_list(self): 
        
        current_element = 0 # O(1)
        next_element = 0 # O(1)
        list = self.list # O(1)
        change_flag = False # O(1) 

        for outer_index in range (0,len(list)-1): # O(n)
            for index in range (0,(len(list)-1)-outer_index):  # O(n^2)
                current_element =  list[index] # O(1) 
                next_element= list[index+1] # O(1) 

                print(f"Current {current_element} + Next Element: {next_element}") # O(1) 
                if (current_element>next_element): # O(1) 
                    change_flag=True # O(1) 
                    print(f"CURRENT {current_element} is HIGHER NEXT : {next_element}")   # O(1) 
                    list[index]= next_element # O(1) 
                    list[index+1]= current_element # O(1) 

            if(change_flag == False): # O(1) 
                return # O(1) 

        return list
        


def main():
    unordered_list1 = [57,7,8,9,3,5,6,35,89,3] # O(1) 
    ordered_list1 = BubbleSortList(unordered_list1) # O(1) 
    list = ordered_list1.sort_list()  # O(n^2)

    print (f"Final LIST {list}") # O(1) 

main()  # O(n^2)
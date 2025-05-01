class BubbleSortList:

    def __init__(self, list):
        self.list = list

    def sort_list(self):
        
        current_element = 0
        prev_element = 0
        list = self.list
        change_flag = False

        for outer_index in range (len(list)-1 , 0 , -1):
            for index in range (len(list)-1 , len(list)-outer_index-1 , -1):

                current_element =  list[index]
                prev_element= list[index-1]

                print(f"Current {current_element} - Pre Element: {prev_element}")
                if (current_element<prev_element):
                    change_flag=True
                    print(f"CURRENT {current_element} is LOWER - PREV : {prev_element}")    
                    list[index]= prev_element
                    list[index-1]= current_element

            if(change_flag == False):
                return

        print (f"Final LIST {list}")


def main():
    unordered_list1 = [57,7,8,9,3,5,6,35,89,3]
    ordered_list1 = BubbleSortList(unordered_list1)
    ordered_list1.sort_list()


main()
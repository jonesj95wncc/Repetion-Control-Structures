# creating empty list
list1 = []

# Declare variables
num = 0
ave_list = 0

# Functions
def append_list(): 
    # ask the user how many number of elements to put in list
    num = int(input("Enter number of elements in list: "))
    
    # iterating till num to append elements in list
    for i in range(1, num + 1):
        ele= float(input("Enter elements: "))
        list1.append(ele)
    return list1

def calculations(list1):
    # Calculations for the required values
    total = sum(list1)
    ave_list = sum(list1)/len(list1) 
    interest_value1 = list1[0] + (list1[0]*.2)
    interest_value2 = list1[1] + (list1[1]*.2)
    interest_value3 = list1[2] + (list1[2]*.2)
    interest_value4 = list1[3] + (list1[3]*.2)
    interest_value5 = list1[4] + (list1[4]*.2)
        
    # print the required values
    print("Sum of the list is: ", round(total, 2))
    print("Average of the list is: ", round(ave_list, 2))
    print("Smallest element is:", min(list1))
    print("Biggest element is: ", max(list1))
    print("Interest at 20% for element 1 is: ", round(interest_value1, 2))
    print("Interest at 20% for element 2 is: ", round(interest_value2, 2))
    print("Interest at 20% for element 3 is: ", round(interest_value3, 2))
    print("Interest at 20% for element 4 is: ", round(interest_value4, 2))
    print("Interest at 20% for element 5 is: ", round(interest_value5, 2))

# Call the functions
append_list()
calculations(list1)

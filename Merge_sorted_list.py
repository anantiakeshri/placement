list1 = [1,2,4]
list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def mergeTwoLists(list1, list2):
        list3 = []

        for num in list1:
            list3.append(num)
            
        for num in list2:
            list3.append(num)
            
        list3.sort() 
        return list3
    
print(mergeTwoLists(list1, list2))
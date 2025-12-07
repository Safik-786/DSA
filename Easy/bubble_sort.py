
# def bubbleSort(n, list):
#     for i in range( 0, n):
#         for j in range(0, n-i):
#             if list[j]> list[j+1]:
#                 temp= list[j];
#                 list[j]= list[j+1];
#                 list[j+1]= temp




def bubbleSort(list):
    for i in range (0, len(list)-1):
        for j in range (0, len(list)-i-1):
            if list[j] >list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
                
 
list=[12, 3, 14, 9, 1, 64, 23]                
# bubbleSort(len(list)-1, list)   
bubbleSort( list)   
print(len(list))    
print(list)

print("Second Min= ", list[2-1])
print("Second Max= ", list[len(list) - 2] )


      


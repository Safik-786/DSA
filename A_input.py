# Case1= [1, 2, 3, 4]
def input_space_separated():
    arr=list(map(int, input().split("")))
    print(arr)
  
def input_array_format():
    arr= list(map(int, input().strip("[]").split(',')))
    return arr
def input_comma_separated():
    arr= list(map(int, input().split(',')))
    return arr
def arr_size_not_given():
    arr= []
    while True:
        # try:
        num= input().strip()
        if num == "":
            break
        arr.extend(map(int, num.strip("[]").split(',')))
        # except Exception as msg:
        #     print('Enter a valid Number.......')
        print(arr)



# input_array_format()
# input_array_format()
arr_size_not_given()


    
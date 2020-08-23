def two_sum_number(array,target_sum):
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1,len(array)):
            second_num = array[j]
            if first_num + second_num == target_sum:
                print(f"[{first_num},{second_num}]")
    print(" ")
    
array = [3,5,-4,8,11,1,-1,6,4,5,14]
target_sum = 10
print(two_sum_number(array,target_sum))

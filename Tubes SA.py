import timeit 

def sum(arr):
    start = timeit.default_timer()
    min1 = arr[0]
    min2 = arr[0]
    for val in arr:
        if val < min1:
            min2 = min1
            min1 = val
    stop = timeit.default_timer()
    execution_time = stop - start
    return min1 + min2, execution_time 



start = timeit.default_timer()
arr = [3,4,6,7,8,2,9]
min = arr[0] + arr[1]
for i in range(len(arr)-1):
    j = i+1
    while j < len(arr):
        if arr[i]+arr[j]<min:
            min = arr[i]+arr[j]
        j+=1
stop = timeit.default_timer()
execution_time = stop - start 

#main function 
print("Greedy :", (sum(arr)[0]))
print("Waktu Eksekusi: ", sum(arr)[1])
print("Brute Force :", (min))
print("Waktu Eksekusi: ",execution_time )
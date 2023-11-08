## bubblesort 
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [3,2,1,4,5,-1,0,-1,5]
print(bubblesort(arr))

def recur(n):
    
    if n>0:
        print(n)
        recur(n-1)


recur(10)
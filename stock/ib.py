# cube = lambda x: x**3# complete the lambda function 

# def fibonacci(n):
#     # return a list of fibonacci numbers
   
#     lis = [0,1]
#     if n == 0:
#         return []
#     if n == 1:
#         return [0]
#     else:
#         for i in range(n-2):
#             next_num = lis[-1]+lis[-2]
#             lis.append(next_num)
#         return lis
    



# if __name__ == '__main__':
#     n = int(input())
#     ans = list(map(cube,fibonacci(n)))
#     print(ans)


def findNumber(arr, k):
    # Write your code here
    for i in range(len(arr)):
        if i==k:
            return "YES"
    return "NO"

arr = [1,2,-2]
k = 6
print(findNumber(arr, k))

# for i in range(l,r):
#     print(i)

#print odd number
def oddNumbers(l, r):
    # Write your code here
    
    lis = []
    if l > 0 and r > 0:
        for i in range(l, r+1):
            # print(l,r,i)
            if i % 2!=0:
                lis.append(i)
        return lis
    
print(oddNumbers(2, 5))


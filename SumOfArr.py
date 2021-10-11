def simpleArraySum(ar):
    return sum(ar)
    
ar_len = int(input("Enter the number of elements in the list "))
ar = []
print("Enter the ",ar_len," elements ",sep='')
for i in range(ar_len):
    num = int(input())
    ar.append(num)

print(ar)
print("Sum of the array is ",simpleArraySum(ar))

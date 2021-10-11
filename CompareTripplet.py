def compareTriplets(a, b):
    # Write your code here
    score = [0,0]
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i]>b[i]:
                score[0] += 1
            elif a[i] < b[i]:
                score[1] += 1
            else:
                pass

    return score
            
a = [1,2,3]
b = [3,2,1]

print(compareTriplets(a, b))

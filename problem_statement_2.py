print("Enter the number of elements to be entered")
n = (int)(input())
l = list()
prefix = list()
for x in range(0,n):
    k = (int)(input())
    l.append(k)
print("Enter the period")
p = (int)(input())

prefix.append(l[0])

for x in range(1,n):
    prefix.append(l[x] + prefix[x-1])

moving_average = list()
moving_average.append(prefix[p-1]/p)

for x in range(p,n):
    moving_average.append((prefix[x]-prefix[x-p])/p)
print(moving_average)
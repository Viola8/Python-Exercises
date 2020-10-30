# Output the total number of distinct countrys with ADD method.

N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
print (len(countries))

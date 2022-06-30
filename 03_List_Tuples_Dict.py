l1=[1,2,3,4,5,6,7,8,9,['a','b','c','d']]
l3=[1,2,3,4,5,6,7,8,9,10]
print(l1[9])

l2=l1[9][1]
print(l2)

l1[9][1]="SAhil"
print(l1)

if 6 in l1:
    print("Yes 6 in the lis l1")
print(l1[6])
print(len(l1))
print(sum(l3))
i=9
while i < len(l1):
    print(l1[i])
    i=i+1
'''
dict = {
  "name": "SAhil",
  "branch": "Comps",
  "year": 2002
}
print(dict)
'''

#Result...
'''['a', 'b', 'c', 'd']
b
[1, 2, 3, 4, 5, 6, 7, 8, 9, ['a', 'SAhil', 'c', 'd']]
Yes 6 in the lis l1
7
10
55
['a', 'SAhil', 'c', 'd']'''
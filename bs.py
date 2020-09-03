f = dict()
f = {'urmum':[3, 4, 5], 'looloo':[4,5,6]}

print(f['urmum'])

average = sum(f['urmum']) / len(f['urmum'])

print(average)

for key in f:
    print(key)
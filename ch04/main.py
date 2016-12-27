x = 3
if x < 1:
    print(' < 1')
elif x < 5:
    print(' < 5')
else:
    print('else')

words = ['Python', 'Go', 'Java', 'Scala', 'Ruby']
for w in words[:]:
    if len(w) > 4:
        print(w)
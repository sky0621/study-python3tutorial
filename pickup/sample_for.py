words = ['dog', 'cat', 'mouse']
for w in words:
    print(w, len(w))

for w2 in words[:]:
    words.insert(0, w2)

print(words)

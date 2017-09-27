if __name__ == "__main__":
    words = ['dog', 'cat', 'mouse', 'rabbit', 'horse']
    for w in words:
        print(w)

    print()

    for w2 in words[:]:
        if len(w2) > 4:
            words.insert(0, w2)

    print(words)

    print()

    for rn in range(5, 10):
        print(rn)

    print()

    for rn2 in range(0, 10, 3):
        print(rn2)

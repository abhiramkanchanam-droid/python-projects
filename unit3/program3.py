text = input("Enter a sentence or paragraph: ")
words = text.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Text:", text)

print("\nWord Frequency Count:")

for key, value in frequency.items():
    print(key, "occurs", value, "times")
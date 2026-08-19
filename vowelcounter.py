text = input("write any sentence: ")
text = text.lower()

vowels = "aeiou"
count = 0

for letter in text:
    if letter in vowels:
        count += 1

print(f"total vocals: {count}")
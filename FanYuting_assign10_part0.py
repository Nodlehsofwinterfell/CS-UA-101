phrase = "The lazy dog jumped over the curious cat."

dictionary = {}

for char in phrase:
    if not char.isalpha():
        continue
    if char not in dictionary.keys():
        dictionary[char] = 1
    else:
        dictionary[char] += 1

keys = sorted(dictionary.keys(), key = lambda x: ord(x))
print("Report by letter, in ascending order by ASCII value:")
for key in keys:
    print(key, dictionary[key])
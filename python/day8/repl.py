sentence = "python is easy"
print(sentence)
words = sentence.split()
c = len(words)
print("number of words is ", c)
list = []
for word in words:
    list.append(word)
print(list)
string = " ".join(words)
print(string)
name="jasii"
print(name)
print(name.startswith("ja"))
print(name.endswith("ii"))
print(sentence.replace("easy", "awesome"))
print(sentence.find("eas"))
print("java" in sentence)

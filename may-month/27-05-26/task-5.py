'''
Find the position of the word "AI" in the sentence "Machine learning and AI are trending."
- Replace "AI" with "Artificial Intelligence" in the above sentence.
= Count how many times the word "data" appers in "data data mining and big data".
'''

sentence1 = "Machine learning and AI are trending"
sentence2 = "data data mining and big data"

sentence3 = sentence1.replace("AI", "Artificial-Intelligence")

print(sentence3)

print(sentence2.count("data"))
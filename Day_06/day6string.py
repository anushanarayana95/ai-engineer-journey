# Day 6 – String Cleaning

raw_name = "   Anusha Narayana   "

clean_name = raw_name.strip().upper()

print("Clean Name:", clean_name)

sentence = "Python is powerful"
words = sentence.split()

print("Words:", words)

new_sentence = sentence.replace("powerful", "amazing")
print("Updated sentence:", new_sentence)
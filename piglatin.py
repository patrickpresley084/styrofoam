# code to convert a sentence into piglatin
words = str(input("Input Sentence to convert into PigLatin:")).split()
j = ""
for  x in words:
  j = j+ x[1:] + x[0] + "ay" + " "
print (j)
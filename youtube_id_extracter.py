# python code to extract youtube ID from a given URL
# input1: https://youtu.be/w6iZdP1hYj8 
# output: w6iZdP1hYj8
# input2: https://www.youtube.com/watch?v=Np7y3DTj1rQ&ab_channel=PatrickPresley
# output = Np7y3DTj1rQ


url = input ('enter the youtube URL: ')
rev = url[::-1]
x = 0
x = url.find("=")
y = url.find("&")
i = rev.find("/")
if x != -1:
  id = url[x+1:y:]
  print (id)
else:
  j = rev[:i:]
  print (j[::-1])



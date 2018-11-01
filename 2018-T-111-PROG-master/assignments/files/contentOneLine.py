fp = open('test.txt', 'r')
line_str = ""

for line in fp:
  line = line.strip()
  line = line.replace(" ", "")
  line_str += line
  
print(line_str)
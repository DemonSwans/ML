import numpy as np

with open("liczby.txt",'w') as file:
   for i in range(1001):
      for x in range(1001):
         file.write(f'{i} {1} {x} {i + x}\n')
         file.write(f'{i} {0} {x} {i - x}\n')

with open("liczby.txt",'r') as file:
   data=[]
   lines = file.readlines()
   for line in lines:
      data.append(line.replace("\n","").split(" "))

data = np.array(data)


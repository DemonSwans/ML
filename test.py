import numpy as np

with open("liczby.txt",'w') as file:
   for i in range(101):
      for x in range(101):
         file.write(f'{i} {1} {0} {x} {i + x}\n')
         file.write(f'{i} {0} {1} {x} {i - x}\n')

with open("liczby.txt",'r') as file:
   data=[]
   lines = file.readlines()
   for line in lines:
      data.append(line.replace("\n","").split(" "))

data = np.array(data)


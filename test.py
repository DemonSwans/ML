import numpy as np
import random

with open("liczby.txt",'w') as file:
   for _ in range(1000):
      a = random.randint(0,400)
      b = random.randint(0,400)
      c = random.randint(0,400)
      d = random.randint(0,400)
      """
      file.write(f'{a} {0} {b} {a - b}\n')
      """
      file.write(f'{a} 1 {b} {a + b}\n')
      file.write(f'{c} 1 {d} {c + d}\n')
      file.write(f'{a} 0 {b} {a - b}\n')
      file.write(f'{c} 0 {d} {c - d}\n')
      """
      file.write(f'{b} 0 {a} {b - a}\n')
      file.write(f'{d} 0 {c} {d - c}\n')
      
      file.write(f'{a} {0} {c} {a - c}\n')
      file.write(f'{a} {1} {c} {a + c}\n')
      file.write(f'{a} {0} {d} {a - d}\n')
      file.write(f'{a} {1} {d} {a + d}\n')

      file.write(f'{b} {0} {a} {b - a}\n')
      file.write(f'{b} {1} {a} {b + a}\n')
      file.write(f'{b} {0} {c} {b - c}\n')
      file.write(f'{b} {1} {c} {b + c}\n')
      file.write(f'{b} {0} {d} {b - d}\n')
      file.write(f'{b} {1} {d} {b + d}\n')

      file.write(f'{c} {0} {b} {c - b}\n')
      file.write(f'{c} {1} {b} {c + b}\n')
      file.write(f'{c} {0} {a} {c - a}\n')
      file.write(f'{c} {1} {a} {c + a}\n')
      file.write(f'{c} {0} {d} {c - d}\n')
      file.write(f'{c} {1} {d} {c + d}\n')

      file.write(f'{d} {0} {b} {d - b}\n')
      file.write(f'{d} {1} {b} {d + b}\n')
      file.write(f'{d} {0} {c} {d - c}\n')
      file.write(f'{d} {1} {c} {d + c}\n')
      file.write(f'{d} {0} {a} {d - a}\n')
      file.write(f'{d} {1} {a} {d + a}\n')
   """
with open("liczby.txt",'r') as file:
   data=[]
   lines = file.readlines()
   for line in lines:
      data.append(line.replace("\n","").split(" "))

data = np.array(data)


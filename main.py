a=int(input ("Введіть а: "))
b=int(input ("Введіть b: "))
if b==0:
  print("Ділення на 0")

elif a < 0 or b < 0:
  print("Будь ласка, введіть додатні числа")

else:
  if a>b:
     x=(b*a+1)

  elif a==b:
    x=-10

  else:
     x=(a-5)/b
  print("Результат обчислення виразу x =" , x)





    
  

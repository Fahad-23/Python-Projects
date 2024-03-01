def div(num, num2):
   try:
        var = num/num2
        print(var)
        return var
   except ZeroDivisionError:
       e = print("You can't divide a number by zero!")
       return e
   except Exception as e:
       print(e)
       return e
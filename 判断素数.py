#import math要放在最上面，不然成为ugly code style
#int(math.sqrt(x)))变成整数才能算
#大牛链接：https://program-think.blogspot.com/2011/12/prime-algorithm-1.html?m=1
import math
x = int(input("Enter a number:"))
for i in range(3,int(math.sqrt(x))):
   if (x%i)==0:
           print(x,"is not a prime number")
           break
   else:
       print(x,"is a prime number")
else:
    print(x,"is not a prime number")

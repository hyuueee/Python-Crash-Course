#2.7版本中使用raw_input(),3.7版本中使用Input()来获取输入
#7-1
name=input('Tell me what brand is your favoriate?')
print('Let me see if I can find you a '+name.title()+'.')
#7-2
number=input('How many of you?')
if int(number)>8:#input输出的是String，为了与18比较，需要将str改成int(数字形)
    print('I am sorry that we do not have enough space.')
else:
    print('We have space for you.')
#7-3
number=input('Enter a number:')
if int(number)%10==0:
    print('这个数可以被10整除')
else:
    print('这个数不能被10整除')

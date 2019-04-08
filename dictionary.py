#chapter 6 Dictionary--{key:value,key:value}
#访问value
alien_0={'color':'green','point':5}
print(alien_0['color'])
print('You just earned '+str(alien_0['point'])+' points')
#添加key:value:dictionaryname[key]=value
print(alien_0)
alien_0['x_position']=0
print(alien_0)
#修改value：依次指定字典名、key以及new value
print('The alien is '+alien_0['color']+'.')
alien_0['color']='yellow'#注意yellow要加引号
print('The alien is now '+alien_0['color']+'.')
#删除key:value:del dictionaryname[key]
del alien_0['point']
print(alien_0)
#遍历字典的key:for key in dictionaryname: print(key)
for key in alien_0:
    print(key)
#遍历字典的value:for value in dictionaryname: print(value)
for value in alien_0.values():
    print(value)
#遍历字典的项：for item in dictionaryname: print(item)
for item in alien_0.items():
    print(item) #要打印啥先定义啥
#遍历字典的Key-value: for item,value in dictionaryname.items(): print(item,value)
for item,value in alien_0.items():
    print(item,value)
#exercise6_5
rivers={'nile':'egypt','Henghe':'india','changjiang':'china'}
for key,value in rivers.items(): #key和value中间应该用逗号断开;rivers后面要加items
    print('The '+key.title()+'runs through '+value.title()+'.')

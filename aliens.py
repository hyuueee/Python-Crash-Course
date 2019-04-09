#字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
print(aliens)
#使用range
aliens=[]
for alien_number in range(30):#创建30个外星人，range的作用是告诉python循环多少次
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)#append用于在列表末尾添加新的对象
for alien in aliens[:5]:#使用切片打印前5个
    print(alien)
print('...')
print('Total number of aliens: '+str(len(aliens)))#打印列表的长度
#修改
for alien in aliens[:3]:
    if alien['color']=='green':#两个等号是判断
        alien['color']='yellow'#一个等号是赋值
        alien['color']='mediem'
        alien['point']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15
for alien in aliens[0:5]:
    print(alien)
print('...')

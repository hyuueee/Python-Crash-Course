class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0 #新加入的变量

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的信息'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self,mileage): #方法二：设置变量函数
        '''将里程表读数设置为指定的值'''
        self.odometer_reading = mileage

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23 #方法一：直接访问属性修改值
my_new_car.read_odometer()

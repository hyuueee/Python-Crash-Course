class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        #初始化name和type
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name.title()+" and it's a "+self.cuisine_type+'restaurant.')

    def open_restaurant(self):
        print('The restaurant is open.')

restaurant=Restaurant('aq','sichuan')
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

liulishe=Restaurant('六厘舎','日本つけ麺')
yilan=Restaurant('一蘭','日本ラーメン')
soba=Restaurant('蕎麦処','日本そば麺')

liulishe.describe_restaurant()
yilan.describe_restaurant()
soba.describe_restaurant()

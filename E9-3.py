class User():
    def __init__(self,first_name,last_name):
        #初始化属性
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print('The first name is '+ self.first_name + 'and the last name is '+self.last_name)

    def greet_user(self):
        print('Nice to see you, '+ self.first_name + self.last_name)

user_a=User('Alice','Yang')
user_b=User('Bill','Han')
user_c=User('Charlie','Zhang')

user_a.describe_user()
user_b.describe_user()
user_c.describe_user()

user_a.greet_user()
user_b.greet_user()
user_c.greet_user()

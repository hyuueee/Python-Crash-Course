#定义一个名为Dog的类，Python中首字母大写的名称指定为类
class dog():
    """一次模拟小狗的简单尝试"""
#类中的函数成为方法_inti_
    def _init_(self,name,age_):
        """初始化属性name和age"""
        self.name=name
        self.age=age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """模拟小狗被命令式打滚"""
        print(self.name.title()+" rolled over!")
        

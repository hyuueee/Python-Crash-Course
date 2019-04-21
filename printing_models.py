#在函数中修改列表
#现有列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#创建新的空列表
completed_models = []
#模拟打印每一个设计
while unprinted_designs:
    current_design=unprinted_designs.pop()
    #每打印一个就放到current design中一个
    print('Printing model: ' + current_design)
    print(current_design) #现在current design中有的东西
    #将current design中的东西放到空的列表中
    completed_models.append(current_design)
    print(completed_models) #这个时候原来空的列表就全部包含了原来的列表中的元素
print('\nThe following models have been printed: ')
for completed_model in completed_models:
    print(completed_model)
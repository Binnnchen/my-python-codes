from collections import OrderedDict as od

language_dict=od()
language_dict['print']="打印语句"
language_dict['title()']="首字母大写"
language_dict['import']="导入模块"
language_dict['input']="输入字符"
language_dict['append']="列表添加元素"

for word,meaning in language_dict.items():
    print("\n"+word)
    print("\t"+meaning)


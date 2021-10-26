import src.consoleoptions as consoleoptions

dict = consoleoptions.get_dict()
for key, value in dict.items():
  print("key:", key, " value:", value, " valuetype:", type(value))

# check command
# python3 test.py value1="test" value2='test2' value3=test3 flagtest value4__int='43' value5__double='33' list__int=1,2,3

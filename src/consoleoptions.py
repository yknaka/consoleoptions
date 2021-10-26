# coding: UTF-8
import sys
# optionName="" もしくはoptionName=''もしくはoptionName=○○もしくはoptionNameで定義された入力オプションを検出して辞書化する


def __trim(string):
  if len(string) == 0:
    return ''
  elif string[0] == '\'' or string[0] == '\"':
    return string[1:-1]
  else:
    return string


def get_dict(args=sys.argv, dict={}):
  for arg in args:
    eqindex = arg.find('=')
    if eqindex == -1:
      dict[arg] = True
    else:
      value = __trim(arg[eqindex + 1:])
      if value.endswith("__int"):
        value = int(value)
      elif value.endswith("__double"):
        value = float(value)
      dict[arg[:eqindex]] = value
  return dict


def to_int(dictionary, optionName):
  if type(dictionary[optionName]) is not int:
    dictionary[optionName] = int(dictionary[optionName])

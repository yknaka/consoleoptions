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
      key = arg[:eqindex]
      value = __trim(arg[eqindex + 1:])
      if ',' in value:
        value = value.split(',')
        if key.endswith('__int'):
          value = [int(v) for v in value]
        elif key.endswith('__double'):
          value = [float(v) for v in value]
        elif key.endswith('__float'):
          value = [float(v) for v in value]
      else:
        if key.endswith('__int'):
          value = int(value)
        elif key.endswith('__double'):
          value = float(value)
        elif key.endswith('__float'):
          value = float(value)
      dict[key] = value
  return dict


def to_int(dictionary, optionName):
  if type(dictionary[optionName]) is not int:
    dictionary[optionName] = int(dictionary[optionName])

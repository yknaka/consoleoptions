# consoleoptions

# option rules
Writing the console command options with the following rules will create a option value dictionary.

## frag
- if the option key exists, 'True' value will set on the dictionary.
```
  dictionary[key] = True
```
For Example,
```
  % command.py optionfrag
```
Then,
```
  dictionary['optionfrag'] => True
  'optionfrag' in dictionary => True
```

## key-value
- The option key and the value are connected with '=' character, they will set as a key-value on the dictionary.
```
  dictionary[key] = value
```
For Example,
```
  % command.py optionkey='value'
```
or,
```
  % command.py optionkey="value"
```
or,
```
  % command.py optionkey=value
```

Then,
```
  dictionary['optionkey'] => value
  'optionkey' in dictionary => True
```

## key-value list
- The option key-value are connected with '=' character and the value is comma separated list, they will set as a key-value_list on the dictionary.
```
  dictionary[key] = [value1,value2,value3,...]
```
For Example,
```
  % command.py optionkey='value1,value2,value3'
```
or,
```
  % command.py optionkey="value1,value2,value3"
```
or,
```
  % command.py optionkey=value1,value2,value3
```

Then,
```
  dictionary['optionkey'] => [value1,value2,value3]
  'optionkey' in dictionary => True
  type(dictionary['optionkey']) => <class 'list'>
```
# methods

## get_dict
Parse space separated argument.

When the key ends with particular word, the paired value will be parsed using following rules automatically.

| word  | key-value | key-value_list |
| :---: | :---: | :---: |
| __int | int(value) | [int(value1), int(value2), ...] |
| __double | float(value) | [float(value1), float(value2), ...] |


Use 'dict' to set the default values.

## load_from_file
Parse options from file.

Use 'dict' to set the default values.

## load_from_json
Parse options from json format.

Use 'dict' to set the default values.
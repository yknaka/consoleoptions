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

# methods

## get_dict
Parse space separated argument.

When the key ends with particular word, the paired value will be parsed using following rules automatically.

| word  | parse as |
| :---: | :---: |
| __int | int(value) |
| __double | float(value) |

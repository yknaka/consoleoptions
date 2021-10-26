# consoleoptions

# option rules
Writing the console command options with the following rules will create a option value dictionary.


# methods

## get_dict
Parse space separated argument.

When the key ends with particular word, the paired value will be parsed using following rules automatically.

| word  | parse as |
| :---: | :---: |
| __int | int(value) |
| __double | float(value) |

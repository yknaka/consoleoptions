# get_console_options

## get_dict
Parse space separated argument.

when key ends with particular word, value is to be parsed using following rules.

| parse_key  | parse as |
| :---: | :---: |
| __int | int(value) |
| __double | float(value) |
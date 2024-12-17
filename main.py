# 5 Exclamation marks series #1: Remove an exclamation mark from the end of string
def remove_exclamation_mark(s):
    result = list(s)
    i = len(result) - 1
    while i >= 0 and result[i] == '!':
        del result[i]
        i -= 1
    return ''.join(result)

print(remove_exclamation_mark("Hi!"))
print(remove_exclamation_mark("Hi!!!"))
print(remove_exclamation_mark("!Hi"))
print(remove_exclamation_mark("!Hi!"))
print(remove_exclamation_mark("Hi! Hi!"))
print(remove_exclamation_mark("Hi"))

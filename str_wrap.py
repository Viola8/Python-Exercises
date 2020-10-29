string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"



for i in range(0, len(string), 4):
    print(string[i:i+4])


# or

import textwrap
def wrap(string, width):
    return textwrap.fill(string,width)
print(wrap('abcfefgtuirssxcfry',3))

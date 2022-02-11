# Special Argument-Matching Modes

# ver figura 06 en Drive

'''
Be careful not to confuse the special name=value syntax in a function header and a
function call; in the call it means a match-by-name keyword argument, while in the
header it specifies a default for an optional argument.
'''

# Keyword and Default Examples



# 1. Por defecto:

def f(a, b, c):
    print(a, b, c)

f(1, 2, 3)  #1 2 3
# 2. Keywords

f(c=3, b=2, a=1)    # 1 2 3

# left-to-right order of the arguments no longer matters when keywords are used 
# because arguments are matched by name, not by position

 
f(1, c=3, b=2)		# a gets 1 by position, b and c passed by name. 1 2 3

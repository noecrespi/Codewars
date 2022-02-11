# 5. Python 3.X Keyword-Only Arguments

# We can also use a * character by itself in the arguments list to indicate that a function
# does not accept a variable-length argument list but still expects all arguments following
# the * to be passed as keywords.
'''
def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
# 1 (2,) 3

kwonly(a=1, c=3)
# 1 () 3

kwonly(1, 2, 3, 4, c=5)

kwonly(1, 2, 3)
# TypeError: kwonly() missing 1 required keyword-only argument: 'c'
'''

# You can still use defaults for keyword-only arguments, even though they appear after
# the * in the function header

def kwonly(*, a, b='spam', c='ham'):
	print(a, b, c)

kwonly(a=1)
# 1 spam ham
kwonly(a=1, c=3)
# 1 spam 3
kwonly(a=1)
# 1 spam ham
kwonly(c=3, b=2, a=1)
# 1 2 3
kwonly(1, 2)
# TypeError: kwonly() takes 1 positional argument but 2 were given

'''

def kwonly(a, *, b, c='spam'):
    print(a, b, c)

kwonly(1, c='eggs')
# TypeError: kwonly() missing 1 required keyword-only argument: 'b'
'''
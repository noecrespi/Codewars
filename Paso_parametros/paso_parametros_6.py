# 4. Combining keywords and defaults

def func(spam, eggs, toast=0, ham=0):
	print((spam, eggs, toast, ham)) 	# First 2 required

func(1, 2)							# Output: (1, 2, 0, 0)
func(1, ham=1, eggs=0)				# Output: (1, 0, 0, 1)
func(spam=1, eggs=0)				# Output: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)		# Output: (3, 2, 1, 0)
func(1, 2, 3, 4) 					# Output: (1, 2, 3, 4)

# Notice again that when keyword arguments are used in the call, the order in which the
# arguments are listed doesn’t matter; Python matches by name, not by position. The
# caller must supply values for spam and eggs , but they can be matched by position or by name
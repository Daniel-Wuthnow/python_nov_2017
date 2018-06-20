def draw_stars(arr):
	star = "*"
	for x in arr:
		if isinstance(x,str):
			print (x[0]*len(x)).lower()
		else:
			print x*star
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])


# draw_stars([2,3,4,6,1])

# def just_stars(arr):
# 	star = '*'
# 	for x in arr:
# 		print x*star
# just_stars([2,4,22,6])

# y = 3
# x = isinstance(y,str)
# print x

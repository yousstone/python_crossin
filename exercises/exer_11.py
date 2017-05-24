
for n in range(1,201):
	sq = n * n
	str_sq = str(sq)
	str_sq_v = str_sq[::-1]
	
	if str_sq == str_sq_v:
		print n

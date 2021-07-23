number = 0
number_2 = 0
files = ["conf-available", "conf-enabled", "mods-available", "mods-enabled", "sites-available", "sites-enabled"]
while True:
	try:
		with open("extra") as extra:
					lines = extra.readlines()
					print(lines[number])
					number += 1
	except(IndexError):
		break
while True:
	try:
			with open(files[number_2]) as documents:
				lines = documents.readlines()
				apache2 = "/etc/apache2/"
				path = apache2 + files[number_2] + "/" + lines[number]
				number += 1
				print(path)
	except(IndexError):
		number = 0
		number_2 += 1
		continue

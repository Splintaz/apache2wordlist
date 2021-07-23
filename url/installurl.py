# https://github.com/Splintaz/apache2-wordlist
# Installs all the URLs inside the text file.
import urllib.request
import os

number = 0
while True:
	try:
		with open("url.txt") as urls:
			lines = urls.readlines()
			os.system(f"wget {lines[number]}")
			number += 1
			print("Finished!")
	except:
		break
# 1. Connect to domain via /etc/hosts/
# 2. exiftool *.png | grep Creator | awk '{print $3}' | sort -u > users.txt
# 3. crackmapexec ldap <INSERT-DOMAIN> -u ./users.txt -p <INSERT-PASSWORD>
# 4. Connect via smbclient

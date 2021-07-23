# https://github.com/Splintaz/apache2-wordlist
# Checks if the URL exists while changing the date, good for fuzzing images or archived files.
import requests
import webbrowser

day = 1
month = 6
year = 2019

def url_ok(url):
    r = requests.head(url)
    return r.status_code

while year < 2022:
    date = str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
    url = "http://127.0.0.1/" + date + ".png"
    url_status = url_ok(url)
    if url_status == 200:
      print(url)
    day += 1
    if day > 31:
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
print("Done!")

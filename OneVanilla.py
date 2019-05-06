from requests_html import HTMLSession
from sys import argv

if len(argv) != 2:

	print("Usage: clear;python3 OneVanilla.py OneVanilla.txt")

else:  # OneVanilla card balance checker

	with open(argv[1], "r") as cards:

		for card in cards:  

			cardNumber, expMonth, expYear, cvv = card.split(':')

			cvv = cvv.rpartition('\n')[0]  # make sure there is a \n ewline@eof 🐛

			c = cardNumber, expMonth, expYear, cvv  #;print(c)

			ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit" + \
			"/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

			with HTMLSession() as s:

				x = s.post("https://www.onevanilla.com/loginCard.html",
					headers={'User-Agent': ua},
					data={
						'cardNumber': cardNumber,
						'expMonth': expMonth,
						'expYear': expYear,
						'cvv': cvv
						},
					timeout=15)

				try: 

					b = x.html.find('div.SSaccountAmount', first=True).text

					print(b, c)

				except:

					if 'Request unsuccessful. Incapsula' in x.text:

						print("incap", c)

					else:
						
						print("error", c)

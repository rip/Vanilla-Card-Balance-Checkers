from requests_html import HTMLSession
from sys import argv

if len(argv) != 2:

	print("Usage: python3 VanillaGift.py VanillaGift.txt")

else:  # VanillaGift card balance checker

	for card in reversed(list(open(argv[1]))):

		cardNumber, expMonth, expYear, cvv = card.rstrip().split(':')

		c = cardNumber + ' ' + expMonth + ' ' + expYear + ' ' + cvv

		ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit" + \
			"/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

		with HTMLSession() as s:

			s.get('https://www.vanillagift.com/',
				headers={'User-Agent': ua},
				timeout=15)  # get incapsula cookie, bypasses rate limiting waf?

			x = s.post("https://www.vanillagift.com/loginCard",
				headers={'User-Agent': ua},
				data={
					'cardNumber': cardNumber,
					'expMonth': expMonth,
					'expYear': expYear,
					'cvv': cvv,
					'origin': 'homeLogin'  # this one isn't required...
					},  # ...but may help to look more nonchalant...
				timeout=15)

			try: 

				b = x.html.find('div.SSaccountAmount', first=True).text

				print(b, c)

			except: 

				print("$.err", c)
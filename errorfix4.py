domain = 'https://walshbr.gov/'
pages = ['about','blog','pedagogy','projects','cv']

urls = []

for thing in pages:
	url = domain + thing
	urls.append(url)

print(urls)

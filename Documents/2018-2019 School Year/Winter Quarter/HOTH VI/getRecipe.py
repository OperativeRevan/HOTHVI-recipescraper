from requests import get
from recipe_scrapers import scrape_me

def generateHTML(url, filename):
	scraper = scrape_me(url)
	if not (scraper.ingredients() and scraper.title() and scraper.instructions()):
		return
	html_str = """
	<h1> {0} </h1>
	<h3> List of Ingredients </h3>
	""" 
	html_str = html_str.format(scraper.title())
	html_str+= "<ul>"

	for i in range(len(scraper.ingredients())):
		html_str = html_str + "<li>" + scraper.ingredients()[i] + "</li>"
	html_str += "</ul>"

	html_str+= "<h3> Cooking Instructions </h3> <ol>"
	#for i in range(len(scraper.instructions())):
	#	html_str = html_str + "<li>" + scraper.instructions() + "</li>"
	#html_str += "</ul>"
	instructions = scraper.instructions().split('\n')
	for i in range(len(instructions)-1):
		html_str+= "<li>" + instructions[i] + "</li>"
	html_str+= """</ol>
	<hr>"""	

	html_file = open(filename, "a")
	html_file.write(html_str)
	html_file.close()

def generateRecipe(list_of_urls, title):
	title+=".html"
	html_str = """<head>
	<link rel="stylesheet" type="text/css" href="style.css"> <meta name= "author" content= "Insiya, Peter, Sydney">
	</head>
	"""
	html_file = open(title, "w")
	html_file.write(html_str)
	html_file.close()
	for i in range(len(list_of_urls)):
		generateHTML(list_of_urls[i], title)


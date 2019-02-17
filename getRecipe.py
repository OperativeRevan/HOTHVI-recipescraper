from requests import get
from bs4 import BeautifulSoup

response = get("https://www.allrecipes.com/recipe/246628/spaghetti-cacio-e-pepe/?internalSource=staff%20pick&referringId=95&referringContentType=Recipe%20Hub")
html_soup = BeautifulSoup(response.text, 'html.parser')
recipe_containers = html_soup.find_all(class_= 'recipe-directions__list--item')
print(len(recipe_containers))
for i in range(len(recipe_containers)):
	print(recipe_containers[i].text.split('.'))

def getTitle(url):
	response = get(url)
	html_soup = BeautifulSoup(response.text, 'html.parser')
	recipe_containers = html_soup.find('title')
	print(recipe_containers.text)

def getIngredients(url):	## URL must be from Allrecipes.com
	response = get(url)
	print (response.text[:500])
	html_soup = BeautifulSoup(response.text, 'html.parser')
	recipe_containers = html_soup.find_all(itemprop='recipeIngredient')
	for i in range(len(recipe_containers)):
		print(recipe_containers[i].text)



## Inspiration

In the age of the internet, it is not hard to find a pie recipe. It *is* hard to find the perfect pie recipe. Shephard's Pie, Raspberry Pie, Chicken Pie, Classic Grandma's Apple Pie: an average college student doesn't have time to google all the different recipes. (We always have time to make delicious pies, however)

We wanted these recipes all in one spot with consistent formatting. So we decided to compile these recipes in our own custom cookbooks. And who doesn't want a full size recipe book of just pies?

We're all hungry, type A college students, and it's hard to not get hangry when different websites show recipes in different layouts.

## What It Does

Scrape My Plate takes a search query (like "pie" or "chicken") and produces an HTML file with recipes scraped from over 30 different food websites. Using the Calibre e-book manager, users can make a neat, custom e-book of recipes for their personal use. 

Here's the [GitHub link](https://github.com/OperativeRevan/HOTHVI-recipescraper "Scrape My Plate")

Here's the [Figma presentation](https://www.figma.com/file/MxvJKX9gTQ7Q9jEDNgc86VAe/Scrape-My-Plate?node-id=0%3A1 "Scrape My Plate Demo")

## How We Built It

This project was built primarily with Python 3, with some HTML and CSS sprinkled in. We used [Google's Custom Search API](https://developers.google.com/custom-search/ "Google's Custom Search API") to search over 30 food websites for relevant recipes. Then, we wrote python script to process the API's output and start up the scrapers. We obtained [open source recipe-scrapers](https://github.com/hhursev/recipe-scrapers "recipe-scrapers") from GitHub. Finally, our python scripts produced an HTML file output that can be entered into Calibre to transform it into an e-book. The html script can also be viewed directly thanks to a CSS file built to make it a bit more eye-friendly. 

## Challenges

We faced a lot of technical difficulties with a team with little experience in dealing with them. Throughout the day, two of our team members left. One member had very little Python experience when we began, and all three members had close to zero experience with frontend development. It didn't help that we spent 2 hours trying to make a Google Chrome extension before learning there was a much more viable alternative. 

And of course, Python doesn't know where SSL certificates are located, so that's fun. 

## Accomplishments

Our program produces an HTML file with correct formatting. This output file is easily transformed into an e-book using Calibre.  

Scrape My Plate can also be incorporated into other projects with ease, as the HTML output can be used as inputs for other applications. 

## What We Learned

We learned how to work with Python libraries and APIs in Python. We also learned how to make HTML files using Python scripts. 

## What's Next

We want to add a scraped Google image of the relevant recipes to our title page and a table of contents. We also want to allow more user control of which recipes go into the outputted HTML file. Coding-wise, we want to make an HTML template so that modifying the Python scripts becomes much easier. We're also interested in pursuing other uses for the outputted HTML file. 

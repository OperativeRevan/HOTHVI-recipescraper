import pprint

from googleapiclient.discovery import build
import getRecipe


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  cook = input("What recipes would you like? ")
  title = input("What would you like your cookbook to be called? ")
  service = build("customsearch", "v1", developerKey="AIzaSyABbVbVlItXo-2e3OGupOBxb6cjWJD-PXE")

  res = service.cse().list(
      q= cook,
      cx='000786494415290461609:tcmpogpbf2m',
    ).execute()
  var =[item["link"] for item in res['items']]
  getRecipe.generateRecipe(var, title)

if __name__ == '__main__':
  main()
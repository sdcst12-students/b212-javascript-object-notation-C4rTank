
import requests
r = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
print (r.json())

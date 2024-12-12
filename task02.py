#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
data = req.text
decoded = json.loads(data)


x = 0
y = 6
z = 1


print("--------------------------------------------------------")
for items, dict in decoded.items():
    #print(items)
    pass
    for inner_items in dict:
        #print(inner_items)
        pass
        for idk in inner_items:
            print(f"{idk} : {inner_items[idk]}")
            x = 1 + x
            if x == y or x == 12 or x == 18 or x == 24:
                print("--------------------------------------------------------")


#DONE




             
             





# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains

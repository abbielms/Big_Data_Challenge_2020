"""
This is another example aka tutorial on how to use APIs
This time, let's have a look at the API called 'Open Notify'
here is the link: http://open-notify.org/

If we make a correct call to the API interface, this API
gives access to data about the international space NASA station! :)

The best thing about it is that it DOES NOT require authentication,
which means we do not need to obtain any API keys, but simply need to
make a call to the API endpoint to get  data back. Let's hve a go!
"""
import requests # we need to import the package that would allow us to establish connections with APIs
from pprint import pprint as pp  # importing pprint library to be able to get data json or dict output in a more readable format

# EXAMPLE ONE - simple call to an API to get some data back.

endpoint1 = 'http://api.open-notify.org/astros.json'  # this endpoint returns data about astronauts currently in space
response = requests.get(endpoint1) # making a call to the API
print(response.status_code)  # make sure that your connection status code is 200, which means success!
data = response.json()  # lets see what data about people in space we get back from the API response
pp(data)

# let's extract data from the response and write it to a file
# we need section 'people' from json, which is a list of dict, so...
# we also need to extract name from each dict item in that list

with open('astranouts.txt', 'w') as text_file:
    for item in data['people']:
        text_file.write(item['name'] + '\n') # added new line character, so each name appears on a new line.




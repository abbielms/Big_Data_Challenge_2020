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

# EXAMPLE TWO - make call to an API and provide payload (some required parameters to get data back)
endpoint2 = 'http://api.open-notify.org/iss-pass.json' # this endpoint tells us the next times that the international space station will pass over a **given location** on the earth

# As input the API expects a latitude/longitude pair for the location of our interst
# Let's make a dictionary with these parameters, and then include them into our call to the API
payload = { # these are coordinates for London
    'lat': 51.507,
    'lon': 0.1278
}
# payload = { # these are coordinates for New York
#     'lat': 40.71,
#     'lon': -74,
# }
response = requests.get(endpoint2, params=payload)
print(response.status_code)  # make sure that your connection status code is 200, which means success!
data = response.json()
pp(data)
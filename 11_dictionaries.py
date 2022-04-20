>>> # user_id = 209
>>> # message = "D5 E5 C5 C4 G4"
>>> # language = "English"
>>> # datetime = "20230215T124231Z"
>>> # location = (44.590533, -104.715556)
>>> post = {"user_id":209, "message": "D5 E5 C5 C4 G4", "language": "English"," datetime":"20230215T124231Z", "location": (44.590533, -104.715556)}
>>> post
{'user_id': 209, 'message': 'D5 E5 C5 C4 G4', 'language': 'English', ' datetime': '20230215T124231Z', 'location': (44.590533, -104.715556)}

>>> post2=dict(message="SS Cotopaxi", language="English")
>>> print(post2)
{'message': 'SS Cotopaxi', 'language': 'English'}
>>> post2["user_id"] = 209
>>> post2["datetime"] = "19771116T093001Z"
>>> post2
{'message': 'SS Cotopaxi', 'language': 'English', 'user_id': 209, 'datetime': '19771116T093001Z'}
D5 E5 C5 C4 G4
>>> print(post2["location"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'location'
>>> if location in post2:
	print(post2["location"])
    else:
	print("The post does nor contain a location value.")
>>> try:
	print(post2["location"])
    except KeyError:
	print("The post does not have a location.")

>>> loc = post2.get("location", None)
>>> print(loc)
None

>>> for key in post.keys():
...     value = post[key]
...     print(key, "=", value)
... 
user_id = 209
message = D5 E5 C5 C4 G4
language = English
 datetime = 20230215T124231Z
location = (44.590533, -104.715556)

>>> for key, value in post.items():
...     print(key, "=", value)
... 
user_id = 209
message = D5 E5 C5 C4 G4
language = English
 datetime = 20230215T124231Z
location = (44.590533, -104.715556)
>>> 

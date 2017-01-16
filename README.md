# Gender Representativity in Tech
App where you can lookup for women or [Non-binary gender](http://nonbinary.org/wiki/Nonbinary_gender) people to help you with that technical issue ;)

###Requirements:
- A running MongoDB
- Python 3.5

###Install:
```
$ pip install -r requirements.txt
```

###Run:
```
$ python app.py
```
 Then open the application at [localhost:5000](http://localhost:5000).

####Register a person:
[/add](http://localhost:5000/add)

####List everyone:
[/list](http://localhost:5000/list)

####Filter by a topic:
/list/{topic}

ex: [/list/ruby](http://localhost:5000/list/ruby)

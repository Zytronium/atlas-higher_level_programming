# Python - Classes and Objects

---
This project is all about python classes.

Classes are something I'm already pretty familiar with from when I did
mobile app development, but I actually never fully understood them.

Classes are kind of hard for me to explain at the time of writing this, so I might
add that later. 

An object is just an instance of a class. (instance meaning an individual thing,
or a single occurrence, rather than the entire class itself)

For example, if I have 4 cars of the same make and model at my car dealership,
that make and model would be the class, and each individual car would be
an object, each likely with its own different properties, like color or
previous owner, which would be the object/instance attributes. And the things
that are the same for all of them, like it's design, name, manufacturer, etc.,
are the class attributes. Now lets say one of them has an engine modification,
that might be a protected object/instance attribute (though, that's a poor example),
and a more secret or personal attribute that nobody but the car owner can touch
might be something like what music is being played, or its destination, which
would be private instance attributes.

A public attribute can be accessed pretty much anywhere, and has no special
naming convention. 

A protected attribute implies it should not be accessed, and should start
with "_". (i.e. "_engine_mod")

A private attribute cannot be accessed by anything but the owner of the attribute.
It should start with "__". (i.e. "__destination")

```python
class ToyotaCamry07:
    # (public) class attributes
    manufacturer = "Toyota"
    model_name = "Camry"
    make_year = 2007
    def __init__(self, vin, color, owner, fuel = 100.0, engine_mods = None, destination = None):
        # instance attributes
        self.__vin = vin
        self.color = color
        self._owner = owner
        self._fuel = fuel  # percent of full tank, NOT gallons
        self._engine_mods = engine_mods
        self.__destination = destination

    # it would be a good idea to specify the types and/or raise exceptions to enforce types
    # property getters and setters would also be a good idea
```

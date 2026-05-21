# Video Notes

Object - instance of a specific class

**init** - called every time a class is instantiated, assigns attributes to new instance

self - need to pass the actual instance itself as an attribute so we know which instance we're accessing

To inherit, pass in the parent class to the child class as an attribute

- super().**init**(arg): inherit certain attributes from the parent class

You can put variables that are specific to the class, not the instance and place them outside the **init** method

class method(pass in cls as an attribute) - class methods are called on classes, not instances, and are denoted by @classmethod.

abstract method - abstract methods are denoted by @abstractmethod, and are passed to the child classes to each implement their own version of that method

static method - defines a method under a class but does not belong to an object/instance

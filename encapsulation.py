#Protected is prefixed with a single underscore.
#It doesn’t actually change the behavior of anything though. You could still
#modify your methods and properties within a class
#It acts more as a warning to other developers and basically states that
#“this is protected - don't use outside of this class”

class Protected:
   def __init__(self):
       self._protectedVar=0

obj = Protected()
obj._prtoectedVar=34
print(obj._protectedVar)

#private is denoted with a double underscore prefix it is harder to access but can be done.
class Protected:
   def __init__(self):
       self.__privateVar=12

   def getPrivate(self):
     print(self.__privateVar)

   def setPrivate(self,private):
      self.privateVar=private
#obj gets the data of the private variable but then we also set the privateVar a new value.
#We then ask for that to be retrieved. It takes a bit more coding, but this ensures that private can not be changed unless it is on purpose.       

obj=Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

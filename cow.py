class Cow:
   def __init__(self, name: str):
       self.__image = None
       self.__name = name


   def get_name(self):
       return self.__name


   def get_image(self):
       return self.__image


   def set_image(self, image: str):
       self.__image = image
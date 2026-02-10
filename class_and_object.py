# OOP - object oriented program
# class is a blue print of all we want to do.
# object is an instance of the class
'''
class Car:
    def __init__(self, color="blue", maker="toyota",brand="camry",year="2025"):
        self.color=color
        self.maker=maker
        self.brand=brand
        self.year=year
        

    def use_wiper(self,timing:int=3):
        if self.year=="2025" and timing == 3:
            print(f"wiper speed is limited to {timing}")
        elif self.year =="2026" and timing >3:
            print(f"wiper speed in {self.year} is more superb")

car_1= Car("silver",brand="benz")
car_1.year="2025"
print(car_1.color)
car_1.use_wiper()

car_2=Car("white", "golf","jaguar", "1999")
car_2.year="2026"
print(car_2.color)
car_2.use_wiper(5)

class Animal:
    def __init__(self, name:str, age:int, colour:str, sex:str):
        self.name=name
        self.age=age
        self.colour=colour
        self.sex=sex

    def cat_sound(self):
        print(f"{self.name} usually says meow")
    
    def dog_sound(self):
        print(f"{self.name} usually says gbo gbo")

    def goat_sound(self):
        print(f"{self.name} usuallu says mehhhhh")

cat=Animal("lucy", 4,"black", "female")
cat.cat_sound()
dog=Animal("jaja", 9, "brown", "male")
dog.dog_sound()
goat=Animal("alake", 22, "white and black", "female")
goat.goat_sound()

class Wild(Animal):
    pass

wild=Wild("lion", 90, "chocolate", "male")
wild.cat_sound
'''
book_list = ["alaroye, tales by moonlight, joy, jigawa, scratch, python training"]
class Book:
    def __init__(self):
        self.books =[]
    
    def add_book(self, book_name:str):
        self.books.append(book_name)
        print(f"{book_name} has been added to the list ")
        self.book_update()

    def remove_book(self, book_name:str):
        self.books.remove(book_name)
        print(f"{book_name} has been removed from the list ")
        self.book_update()

    def book_update(self):
        print(f"we have {len(self.books)} books left in the list ")

    def add_books(self, book_names:list): 
        for item in book_names:
            self.books.append(item)
    
    def remove_books(self,book_names:list):
        for item in book_names:
            self.books.remove(item)
    
    def update_books(self, book_names:list):
        query=input("Are you adding or removing book? ")
        if query =="add":
            self.books.append(book_names)
            print(f"{book_names} has been added to the list")
            self.book_update()
        else:
            self.books.remove(book_names)
            print(f"{book_names} has been removed from the list ")
            self.book_update()
            

library=Book()
library.add_book("alaroye")
library.add_book("tales by moonlight")
library.add_book("joy")
library.add_book("jigawa")
library.remove_book("jigawa")


  


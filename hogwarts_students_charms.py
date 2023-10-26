class Student: 
     def __init__(self, name, house, patronus):
          self.name = name
          self.house = house
          self.patronus = patronus

          self.patronus_emoji = self.charm()

     def __str__(self):
        return f"{self.name} from {self.house} has a {self.patronus_emoji} patronus."
     
     @classmethod
     def get(cls):
          name = input("Name: ")
          house = input("House: ")
          patronus = input("Patronus: ")
          
          return cls(name, house, patronus)
     
     @property
     def name(self):
          return self._name
     
     @name.setter
     def name(self, name):
          if not name:
               raise ValueError("Missing name")
          
          self._name = name
          
     @property #getter
     def house(self):
          return self._house
     
     @house.setter #setter
     def house(self, house):
          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
               raise ValueError('Invalid house')

          self._house = house
     
     def charm(self):
         match self.patronus:
              case "Stag":
                   return "🦌"
              case "Otter":
                   return "🦦"
              case "Jack Russel Terrier":
                   return "🐕"
              case _:
                   return "👻"

def main():
    student = Student.get()
    print(student)
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():
#         name= input("Name: ")
#         house= input("House: ")
#         patronus = input("Patronus: ")
    
#         return Student(name, house, patronus)
        
        # name= input("Name: ") 
        # house= input("House: ")
        # return {"name": name, "house": house}
    # name = input("Name: ")
    # house = input("House: ")
    # return [name, house]

if __name__ == "__main__":
    main()
# import pandas as pd
# # from fbprophet import Prophet
# import plotly as pl
# from skimage import color

# # def hello():
# #     print("Hello World")

# # if __name__ == "__main__":
# #     hello()

# class Hat:

#     def hat(self, name, house):
#         self.name = name
#         self.house = house


#         print(f"{self.name} from {self.house}")
    
#     @classmethod
#     def hello(cls):
#         print("Hello World")
#         return "Hello World"
    
#     ## setter
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, value):
#         self._name = value

# class Red:
#     def colors(self, color):
#         self.color = color
#         print(self.color)

# class stu:
#     ## inherit Hat

#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#         self.hat = Hat()
#         self.red = Red()

#     super().__init__(name, house)
#     self.hat.hat(name, house)
#     self.red.colors(color)


    


# hat = Hat()

# hat.hat("ace","Rat")
# Hat.hello()


# d = {"a":1, "b":2}
# li = [1,2,3,4,4,5]

# val = list(map(lambda x: x*2,li))

## fillter
# val = list(filter(lambda x: x%2==0,li))

# ## yield 
# val = (x**2 for x in li)
# val = list(val)

# print(val)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("person __init__ being called")

#     def __str__(self):
#         print(self.name, self.age)
#         print("person __str__ being called")


# class student(person):
#     def __init__(self, name, age, grade):
#         print("Hey I'm here...!")
#         super().__init__(name, age)
       
#         print("student __init__ being called")
#         self.grade = grade
    
#     def __str__(self):
#         print(self.name, self.age, self.grade)
#         print("student __str__ being called")


# stu = student("ace", 22, "A")

# stu.__str__()
    
    

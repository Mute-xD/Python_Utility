# # import numpy
# import os
##############################################
# d = {"a": 3, "b": 4, "c": 5}
# for a, b in d.items():
#     print("keys", a, "value", b)
# for a in d.keys():
#     print("keys", a)
# d2 = {"a": [1, 2, 3], "b": (1, 2, 3), "c": {"wow": 1}}
# print(d2["c"]["wow"])
# d2["a"] = [4, 5, 6]
##############################################
#
# def add(a1, b1):
#     c = a1 + b1
#     return c
#
#
# print(add(1, 2))
# print(os.getcwd())  # Python 目录
#
#############################################
# class Human:
#     name = "unknown"
#     age = 100
#
#     def __init__(self, name="wow", age=18):
#         self.name = name
#         self.age = age
#         print("Human init")
#
#     def report(self):
#         print("name is ", self.name, self.age)
#
#     def add(self, a1, b1):
#         print("result is ", a1 + b1)
#
#
# class Student(Human):
#     def __init__(self, score=0):
#         super().__init__()
#         self.score = score
#         print("student init")
#
#     def show_score(self):
#         print("Score is ", self.score)
#
#     def add(self, a1, b1):
#         print("result may not ", a1 + b1)
#
#
# stud1 = Student()
# stud1.add(1, 2)
####################################################################

# fuck = "hello world"
# myFile = open("what_the_fuck.txt", "w")
# myFile.write(fuck)
# myFile.close()
# with open("file_2.txt", "r") as file2:
#     for line in file2:
#         line.rstrip()
#         print(line)
# try:
#     file = open("wow", "r")
# except Exception as e:
#     print(e)
#######################################################################
import json
aDict = {"name": "mute", "number": 2018365509}

with open("wow.json", "w") as file:
    json.dump(aDict, file)
with open("wow.json") as file:
    wow = json.load(file)
print(wow)

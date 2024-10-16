# Luke Jackson
# UWYO COSC 1010
# 10/15/24
# HW 01
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student and their scores
# in different subjects.
#
# Student Data:
#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.
#Solution
students = [
  {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
  {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
  {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
  {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]

Students_Averages = {}


for student in students:
   Student_total_score = 0
   Student_average_score = 0
   for key, value in student["scores"].items():
      Student_total_score += value
      Student_average_score = Student_total_score / 3
      Students_Averages[student["name"]] = Student_average_score
   
for key, value in Students_Averages.items():
   if value > 80:
      print(f"{key}'s score is greater than 80!!")

# Section A MCQs:-
# answer 1 :- (b)
# answer 2 :- (c)
# answer 3 :- (b)
# answer 4 :- (c)
# answer 5 :- (b)
# answer 6 :-(c)
# answer 7 :-(c) 
# answer 8 :-(a)
# answer 9 :-(b)
# answer 10 :-(b)




# Section B Python Programming:-


#question 11 


# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def display(self):
#         print("Name:", self.__name)
#         print("Marks:", self.__marks)

# s = Student("Sahil", 89)
# s.display()


#question 12 


# try:
#     with open("students.txt", "r") as file:
#         data = file.read()

#         lines = data.splitlines()
#         words = data.split()

#         print("Total Lines:", len(lines))
#         print("Total Words:", len(words))

# except FileNotFoundError:
#     print("Error: students.txt file not found!")


# Section C  SQL :-

# question 13:-

# SELECT
#     s.student_name,
#     s.city,
#     c.course_name,
#     r.subject,
#     r.marks
# FROM students s
# INNER JOIN courses c
#     ON s.course_id = c.course_id
# LEFT JOIN results r
#     ON s.student_id = r.student_id;

#question 14 :-

# SELECT
#     c.course_name,
#     COUNT(DISTINCT s.student_id) AS total_students,
#     AVG(r.marks) AS average_marks
# FROM courses c
# INNER JOIN students s
#     ON c.course_id = s.course_id
# INNER JOIN results r
#     ON s.student_id = r.student_id
# GROUP BY c.course_id, c.course_name
# HAVING AVG(r.marks) > 70;

#section D DSA:-

# question 16:-

# def constant_difference(arr):
#     if len(arr) < 2:
#         return True

#     diff = arr[1] - arr[0]

#     for i in range(1, len(arr) - 1):
#         if arr[i + 1] - arr[i] != diff:
#             return False

#     return True


# numbers = [2, 4, 6, 8, 10, 12]

# print(constant_difference(numbers))

# question 20:-

# def max_sum(arr, k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i-k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


# arr = [3, 1, 4, 2, 5, 1, 6]
# k = 3

# print("Maximum Sum:", max_sum(arr, k))

# time complexity is O(n)


#question 19 :-

# def frequency_count(arr):
#     freq = {}

#     for num in arr:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1

#     most_frequent = max(freq, key=freq.get)

#     print("Frequency Count:", freq)
#     print("Most Frequent Number:", most_frequent)
#     print("Frequency:", freq[most_frequent])


# arr = [4, 2, 4, 3, 2, 4, 1]

# frequency_count(arr)

# question 17:-

# def max_sum(arr, k):
#     window_sum = sum(arr[:k])
#     maximum = window_sum

#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i-k]
#         maximum = max(maximum, window_sum)

#     return maximum


# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# print("Maximum Sum:", max_sum(arr, k))
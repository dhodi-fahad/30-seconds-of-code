# ------- wrong -----
# def sort_people(the_list_of_people):
#     the_list = the_list_of_people
#     final_list = []
#     position_of_person_to_check = 1
#     person_to_check = the_list[position_of_person_to_check - 1]
#     for i in range(the_list):
#         while position_of_person_to_check < len(the_list):
#             if person_to_check < the_list[position_of_person_to_check]:
#                 pass
#             elif person_to_check == the_list[position_of_person_to_check]:
#                 person_to_check = the_list[position_of_person_to_check]
#             else:
#                 person_to_check = the_list[position_of_person_to_check]
#
#             position_of_person_to_check = position_of_person_to_check + 1
#         largest_person = person_to_check
#         final_list.append(largest_person)
#         the_list = [x for x in the_list if x != largest_person]
#     return final_list


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'{self.firstname} {self.lastname}, {self.age}'

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


def sort_people(people):
    return sorted(people)


person1 = Person("John", "Doe", 25)
person2 = Person("Jane", "Doe", 30)
person3 = Person("Bob", "Smith", 20)

people = [person1, person2, person3]
sorted_people = sort_people(people)
print(sorted_people)


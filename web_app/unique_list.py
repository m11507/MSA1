def main():
    person1 = {"name": "Sam", "age": 17}
    person2 = {"name": "Frank", "age": 18}
    person3 = {"name": "Sam", "age": 16}
    person4 = {"name": "Cyd", "age" : 17}

    person_list = []
    person_list.append(person1)
    person_list.append(person2)
    person_list.append(person3)
    person_list.append(person4)

    unique_names = []

    for name in person_list:
        if (name["name"] not in unique_names):
            unique_names.append(name["name"])



main()
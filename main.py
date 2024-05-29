#Output Exercises

#Exercise 1
print ("Welcome to Programming Analysis!")

#Exercice 2
top_programmer = "Ada Lovelace"
print ("The top programmer is", top_programmer)

#Exercice 3
language_name = "Python"
version = 3.9
print(f"{language_name} has version {version}.")

#Exercice 4
programmer_name = "Ada Lovelace"
lines_of_code = 1000
print("{} has written {} lines of code" .format(programmer_name, lines_of_code))

#Exercice 5
top_programming_languages = ["Python", "Javascript", "Java", "C#"]
print(top_programming_languages)

#Exercice 6
language_creators = {
    "Python": "Guido van Rossum",
    "JavaScript": "Brendan Eich",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}
print(language_creators)

#Exercice 7
programmer_stats = {
    "name": "Kevin De Coder",
    "team": "Code City",
    "projects": 10,
    "contributions": 18
}
print(f"{programmer_stats['name']} from {programmer_stats['team']} has completed {programmer_stats['projects']} projects and provided {programmer_stats['contributions']} contributions"
      )

#Modifying Strings - Examples - Data

#1 - Concatenation

person1 = "Alice Johnson"
occupation1 = "Software Engineer"

person2 = "Bob Smith"
occupation2 = "Graphic Designer"

person3 = "Charlie Brown"
occupation3 = "Data Analyst"

result1 = person1 + " - " + occupation1
result2 = person2 + " - " + occupation2
result3 = person3 + " - " + occupation3

print(result1)
print(result2)
print(result3)

#2 - Slicing

person_info = "Emma Watson, Actress"

first_name = person_info[:4]
last_name = person_info[5:11]
occupation = person_info[13:]

print(first_name)
print(last_name)
print(occupation)

#3 - Replacing

company_info = "John Doe works for Microsoft."

new_company_name = company_info.replace("Microsoft", "Google")

print(new_company_name)

#4 - Formatting

person_name = "Jane Smith"
activity1 = "hiking"
activity2 = "painting"

formatted_string = f"{person_name} enjoys {activity1} and {activity2}"
print(formatted_string)

#5 - Upper Lower Cases

city_name = "New York City"

upper_case_city_name = city_name.upper()
lower_case_city_name = city_name.lower()

print(upper_case_city_name)
print(lower_case_city_name)


#6 - Splitting, Joining, Stripping

person_data = "  Emily Davis, 35, Architect  "

split_data = person_data.strip().split(', ')
joined_data = '|'.join(split_data)

print(joined_data)
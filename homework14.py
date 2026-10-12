
grades = {
    "shawaiz": 90,
    "ali": 65,
    "eesa": 45,
    "haziq": 89,
    "waaiz": 90
}
total = 0
for name in grades:
    total = total + grades[name]
average = total / len(grades)
print("class average:", average)
top_name = ""
top_score = 0
for name in grades:
    if grades[name] > top_score:
        top_name = name
        top_score = grades[name]
print("Highest score:", top_name, top_score)
lookup = input("look up student: ")
print("scores:", grades.get(lookup, "shawaiz:90,ali:65,eesa:45,haziq:89,waaiz:90"))

with open("data.txt", "w", encoding="utf-8") as file:
        file.write("|{:^65}|{:^65}|{:^65}|\n".format('Module', 'Question', 'Answer').replace(' ', '_'))
with open("data.csv", "w", encoding="utf-8") as file:
        file.write("")
print("Done")

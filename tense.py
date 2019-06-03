import os
import random

sub = ["Please", "I", "We", "You", "He", "She", "They", "Tom", "Alice", "My grandma", "Mr King", "The Smiths", "Those girls", "All of the students"]
obj = ["(read) books", "(have) a big dinner", "(do) homework", "(turn on/off) TV", "(take) a bath", "(take) a bus", "(go) camping"]
time = ["this evening", "tomorrow", "later this week", "on June 19", "the day after tomorrow", "now", "at 7pm", ",when Mike feels good", ", while Amy is playing Piano", "in two days", "after washing hands", ", when I was young", "yesterday", "on Mondays", "every night", "always", "before mum goes back home", "in 2009"]
blank = "_________________"
dot = "."


sub_len = len(sub)
obj_len = len(obj)
time_len = len(time)
print("")
print("            ===========================")
print("            Dynamic Time Sense Practice")
print("            ===========================")
print("")

for i in range(1, 11):
    print(i, end=":    ")
    str = random.choice(sub)
    print(str, end=" ")
    print(blank, end=" ")
    str = random.choice(obj)
    print(str, end=" ")
    str = random.choice(time)
    print(str, end=" ")
    print(dot)
    print(" ")

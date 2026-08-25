# colors = ["red", "blue", "green", "blue"]
#
# Replace all "blue" with "skyblue" and print the updated list.
colors = ["red", "blue", "green", "blue"]
for i in colors:
    if "blue" in colors:
        print(i.replace("blue","skyblue"))
    else:
        print(i)
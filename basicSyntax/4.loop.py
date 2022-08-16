def greetToFriends (friends):
    for friend in friends:
        if friend["level"] != "학생":
            break
        else:
            print(f"Hi {friend['name']}")
            #print("Hi" + friend["name"])


classMates = [{ "name": "채민", "level" : "학생"},{"name" : "준서", "level" : "학생"},{"name" : "잎새", "level" : "선생"}, {"name" : "준서", "level" : "학생"}]

greetToFriends(classMates)
#print(classMates[0]["name"])
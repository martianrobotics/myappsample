RegisteredUsers = ["John","Tom","Admin","Harry","Peterson"]
AttemptedUsers= ["Thomas","Tim","Samantha","Sandy","Susan","Tom","Admin","Harry","Peterson","Jasper"]
new_attempted_users = AttemptedUsers.copy()

for i in AttemptedUsers:
    if i not in RegisteredUsers:
        print("\n" + i +", You are not welcome here!!")
        new_attempted_users.remove(i)
    elif i == "Admin":
        print ("\nWelcome Admin!!")
    else:
        print ('\n' + i +', Welcome normal users, ' + i)

print("\n")
AttemptedUsers = new_attempted_users
print (AttemptedUsers)
print (new_attempted_users)
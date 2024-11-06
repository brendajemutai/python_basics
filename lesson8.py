#dictionary
#list[],tuple(),dictionary{}
#key,value
student={"name":"Brenda","id": 1234,"age": 23, "gender":"f"}
print(student["name"]) #key
print(student)

student["weight"]=61 #add
print(student)

#set---only one existence per item,unordered
people={"Jane","Billy","Kevo","Said","Jane"}
print(people)
people.add("Willy")
print(people)
print(len(people))
people.discard("Kevo")
print(people)

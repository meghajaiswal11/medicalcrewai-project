print("hi")
print("This is AI Agent Workshop")

name = "megha"
age = "19"

symptomlist = [{
    "name": "cough",
    "severity": "mild",
    "duration": "2 days",
    "priority": 1
}
{
    "name": "Fever",
    "severity": "high",
    "duration": "5 day",
    "priority": 2
}, {
    "name": "headache",
    "severity": "low",
    "duration": "1 days",
    "priority": 3
}]

print("Hi")
print(name)
# print(symptomlist)
#print(symptomlist[0])

for  symptom in symptomlist:
     if (symptom["priority"] == 1):
         print(symptom["name"]) 
         print(symptom["priority"])



symptom = input("What symptom your having ?")
print(symptom)

if symptom == "cough":
    print("take xyz medicine")
    print("this")
    print("that")
elif symptom == "Fever":
    print("visit doctor")

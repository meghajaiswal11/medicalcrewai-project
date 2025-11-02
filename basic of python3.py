def greet():
    print("hi")
    print("This is AI Agent Workshop")

def takeInput():
    userInput = input("Enter your symptom:")
    print( userInput)
    return userInput

class Agent:
    def __init__(self, name):
        self.name = name
        
    def giveAdvice(self ,symptom):
       if symptom == "cough":
        print("take xyz medicine")
        print("this")
        print("that")
       elif symptom == "Fever":
        print("visit doctor")
       else: 
        print("you are thinking too much!")


greet()

name = "megha"
age = "19"

symptomlist = [{
    "name": "cough",
    "severity": "mild",
    "duration": "2 days",
    "priority": 1
},
{
    "name": "Fever",
    "severity": "high",
    "duration": "1 day",
    "priority": 2
}, {
    "name": "headache",
    "severity": "low",
    "duration": "1 days",
    "priority": 2
}]

print("Hi")
print(name)
# print(symptomlist)
# print(symptomlist[0])

#for  symptom in symptomlist:
#     if (symptom["priority"] == 2):
#         print(symptom["name"]) 
#         print(symptom["priority"])
       
symptom = takeInput()

agent = Agent("HealthBot1.0")
agent.giveAdvice(symptom)


print("Thank you for using our bot")

def greet():
  print("hi")
  print("This is AI Agent Workshop")

def takeInput():
  userInput = input("Enter your symptom:")
  print( userInput)
  return userInput

class  chatGpt_LLM:
  def __init__(self, model_name):
      self.model_name = model_name

  def generateResponse(self, prompt):
      #call openai api get get response based on the prompt
      #openai url
      #openai key
      #make http call
      return "This is a generated response based on the prompt: " + self.model_name 
  
  class Gemini_LLM:
    def __init__(self, model_name):
        self.model_name = model_name
      
  def generateResponse(self, prompt):
      #call gemini api get get response based on the prompt
      #gemini url
      #gemini key
      #make http call
      return "This is a dummy response from: " + self.model_name 

class  Practo_Tool:
   def __init__(self, name):
       self.name = name

   def useTool(self, input):
      #api Url
      #api key
      #http call
      print("Using tool " + self.name + " with input: " + input)

class  Agent:
  def __init__(self, name , llm , tool):
      self.name = name
      self.llm = llm
      self.tool = tool
      
  def giveAdvice(self ,symptom):
      #llm = ChatGpt_LLM("gpt-4")
      response =  llm.generateResponse("provide advice for symptom: " + symptom)
      print("Advice for " + symptom + ": " + response)

  def takeAction (self, input):
         tool.useTool(input)

  def giveAdviceAndTakeAction(self ,symptom):
      self.giveAdvice(symptom)
      self.giveAdvice(symptom)

class AutoAgent:
   def __init__(self, name, llm, tool):
      self.name = name
      self.llm = llm
      self.tool = tool

   def decideToUseTool(safe, response):
      #logic to decide whether to use tool based on response
       if "visit doctor" in response:
           return True
           return False

   def excute(self, symptom):
          response = llm.generateResponse("Provide advice for the symptom:" + symptom)
          print("Advice for " + symptom + ":" + response)
          if (decideToUseTool(response)):
             tool.useTool(symptom)
          else:
             print("NO action needed")
      

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

# print("Hi")
# print(name)
# print(symptomlist)
# print(symptomlist[0])

#for symptom in symptomlist:
#     if (symptom["priority"] == 2):
#         print(symptom["name"])
#         print(symptom["priority"])

symptom = takeInput()

llm = chatGpt_LLM("gpt-4")
tool = Practo_Tool("PractoAPI")
agent = Agent("HealthBot1.0" , llm , tool)
agent.giveAdvice(symptom)


print("Thank you for using our bot")
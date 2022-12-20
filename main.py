import json

goblins = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
rabbits = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
cybers = [2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9]
neos = [3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9]
turtles = [4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9]

grand = 5.0
a = "Alpha"
b = "Beta"
rc = "Release Candidate"
f = "Release"

file = open("config.json","r")
json = json.loads(file.read())
codename = "N/A"
major = "N/A"
minor = "N/A"
patch = "N/A"
na = "N/A"
editorver = ""
p = "."
done = None
num1 = 2022.11
num2 = None
num3 = None

# rabbit cyber neo ultra
latest = {"editorVer": {
    "major": "2022",
    "minor": "1",
    "ln": "1",
    "patch": "f1"
  }}



if not done:
  if json["editorVer"]["ln"]:
    num2 = float(json["editorVer"]["major"]+p+json["editorVer"]["minor"]+json["editorVer"]["ln"])
  elif json["editorVer"]["minor"]:
    num2 = float(json["editorVer"]["major"]+p+json["editorVer"]["minor"])
  else:
    num2 = float(json["editorVer"]["major"])
  num3 = round(num1 - num2,1)

if not done:
  if num3 < round(num1 - num1):
    print("Too high version!")
    exit(1)

if num3 in goblins:
  codename = "Goblin"

elif num3 in rabbits:
  codename = "Rabbit"

elif num3 in cybers:
  codename = "Cyber"

elif num3 in neos:
  codename = "Neo"

elif num3 in turtles:
  codename = "Turtle"

elif num3 == grand:
  codename = "Grand"

  
try:
  if not done:
    if json["editorVer"]["patch"]:
      done = True
      if "f" in json["editorVer"]["patch"]:
        editorver = "Unity "+f+" "+json["editorVer"]["major"]+p+json["editorVer"]["minor"]+p+json["editorVer"]["ln"]+json["editorVer"]["patch"]+" "+"("+codename+" "+str(num3)+")"
      elif "rc" in json["editorVer"]["patch"]:
        editorver = "Unity "+rc+" "+json["editorVer"]["major"]+p+json["editorVer"]["minor"]+p+json["editorVer"]["ln"]+json["editorVer"]["patch"]+" "+"("+codename+" "+str(num3)+")"
      elif "b" in json["editorVer"]["patch"]:
        editorver = "Unity "+b+" "+json["editorVer"]["major"]+p+json["editorVer"]["minor"]+p+json["editorVer"]["ln"]+json["editorVer"]["patch"]+" "+"("+codename+" "+str(num3)+")"
      elif "a" in json["editorVer"]["patch"]:
        editorver = "Unity "+a+" "+json["editorVer"]["major"]+p+json["editorVer"]["minor"]+p+json["editorVer"]["ln"]+json["editorVer"]["patch"]+" "+"("+codename+" "+str(num3)+")"
except KeyError:
  pass
    


if not done:
  try:
    if json["editorVer"]["minor"]:
      done = True
      editorver = "Unity "+f+" "+json["editorVer"]["major"]+p+json["editorVer"]["minor"]+p+"0f1"+" "+"("+codename+" "+str(num3)+")"
  except KeyError:
    pass

if not done:
  if json["editorVer"]["major"]:
    editorver = "Unity "+f+" "+json["editorVer"]["major"]+p+"0"+p+"0f1"+" "+"("+codename+" "+str(num3)+")"

print(editorver)

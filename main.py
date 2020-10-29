import json
from time import sleep as tsleep
from sys import exit as scriptstop

health = 20

def store(file, key, val, read=False):
  with open(file, 'r') as v:
    x = json.load(v)
  if read is not False:
    return x[key]
  else:
    x[key] = val
    with open(file, 'r') as v:
      json.dump(x, v, indent=4)

class Profile:
  def __init__(self, name, profnumber):
    self.name = name
    if profnumber == 1:
      profilenum = '.prof1.json'
    elif profnumber == 2:
      profilenum = '.prof2.json'
    store(profilenum, 'name', self.name)
    soter(profilenum, 'first', '0')

  def internalgetprof(self, profnumber):
    if profnumber == 1:
      return '.prof1.json'
    elif profnumber == 2:
      return '.prof2.json'
  def getname(self, profnumber):
    proffile = Profile.internalgetprof(profnumber)
    return store(proffile, 'name', read=True)
    
def first(profnum):
  print("Welcome to Chilled_Bird's fun text game!")
  tsleep(0.5)
  name = input("What is your name? ")
  if len(name) > 0:
    pass
  else:
    return 0
  print(f"Hi {name}!")
  if profnum == 1:
    global profile1
    profile1 = Profile(name, 1)
  elif profnum == 2:
    global profile2
    profile2 = Profile(name, 2)

def startup():
  if store('.prof1.json', 'first', read=True) == '1':
    rval = first(1)
    if rval == 0:
      print("Ok...\nExiting")
      scriptstop()
  else:
    pass

def main():
  pass
  
# Does nothing as of the first commit
main()

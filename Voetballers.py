scorer1 = str('Ruud van Gullit')
scorer2 = str("Marco van Basten")
goal_1 = 32
goal_2 = 54
print(str(scorer1) , "scoorde na de" , str(goal_1) + "ste", "minuut een doelpunt."'\n' + 
      str(scorer2) , "scoorde na de" , str(goal_2) + "ste", "minuut een doelpunt.")

player = "Sergey Gotsmanov"
deling = player.find(" ")
print("Space is at:\t",deling)

first_name = player[slice(deling)]
print("Voornaam:\t",first_name)

#hieronder wordt de achternaam opgelijst.
#Is er een manier waarop dit met SLICE kan?

last_name = player[(deling+1):99]
print("Achternaam:\t",last_name)

#hieronder wordt de achternama geteld.

last_name_len = len(last_name)
print("Len Lastname:\t",last_name_len)

#hieronder wordt de verkorte naam weergegeven
initial = player[slice (1)]
print("Full name:\t",initial + ".",last_name)

#geef weer de voornaam in getallen
#print de voornaam in aantal keer voornaam met uitroepteken

first_name_len = len(first_name)
print("Len Firstname:\t",first_name_len)
chant = (first_name+"!"+" ") * first_name_len
print(chant)

if chant[-1]!=" ":
    print("Great Chant!")

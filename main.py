zombieWeakness = "0"
weapons = ["Holy Water", "Chainsaw", "Shotgun", "Beer Bottle", "Knife", "Fists"]
print("You are in a zombie apocalypse and need weapons for protection")
print("We have an armory with weapons already, do you want to use one of these or pick your own?")
print(weapons)
choice = (int(input("Type 1 for one of our weapons or 2 for your own: ")))


if choice == 1:
  choice2 = (int(input("Which one do you want to use?(Enter a number for the item, 0-5) ")))
  if choice2 == int(zombieWeakness):
    print('You Did It!! You Beat The Zombies!!')
  else:
    print("The Zombies Got you!! The Weakness Was Holy Water!!")
  
elif choice == 2:
  choice3 = input("Enter a weapon you want to use: ")
  weapons.append(choice3)
  print("This is your new weapon list")
  print(weapons)
  choice2 = (int(input("Which one do you want to use?(Enter a number for the item, 0-6) ")))
  if choice2 == int(zombieWeakness):
    print('You Did It!! You Beat The Zombies!!')
  else:
    print("The Zombies Got you!! The Weakness Was Holy Water!!")

  

    


  
  
  
  
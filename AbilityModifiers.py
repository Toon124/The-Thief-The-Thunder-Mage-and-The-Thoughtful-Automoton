from TheDice import D20

def ability_mod(stat):
  if stat == 1:
    ability_mod = -5
  if stat < 1 and stat < 4:
    ability_mod = -4
  if stat > 3 and stat < 6:
    ability_mod = -3
  if stat > 5 and stat < 8:
    ability_mod = -2
  if stat > 7 and stat < 10:
    ability_mod = -1
  if stat > 9 and stat < 12:
    ability_mod = 0
  if stat > 11 and stat < 14:
    ability_mod = 1
  if stat > 13 and stat < 16:
    ability_mod = 2
  if stat > 15 and stat < 18:
    ability_mod = 3
  if stat > 17 and stat < 20:
    ability_mod = 4
  else:
    ability_mod = 5
  return ability_mod

def initiative(mod):
  init = D20() + mod
  return init
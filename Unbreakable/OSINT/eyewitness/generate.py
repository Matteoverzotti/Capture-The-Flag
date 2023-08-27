from hashlib import sha256

locations = open('locations.txt').read().split()

for loc in locations:
  v = '///'+loc
  print(v)

  if len(loc) == 0 or loc[0] == '#':
    continue
  
  m = sha256()
  m.update(v.encode())
  print(f'CTF{{{m.digest().hex()}}}')
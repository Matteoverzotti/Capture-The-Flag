from pwn import *
import base64
import re

context.log_level = 'debug'
TIMEOUT = 0.2

def tower(n, source, destination, auxiliary):
    if n == 1:
       yield source, destination
       return
    yield from tower(n - 1, source, auxiliary, destination)
    yield source, destination
    yield from tower(n - 1, auxiliary, destination, source)

io = remote("34.159.187.220", 32625)

current_round = None
moves = None

while True:
  text = io.clean(timeout=TIMEOUT).decode()
  lines = [line.strip("\n") for line in re.compile(r"\n+").split(text) if line.strip() != ">"]

  print(lines)

  decoded_lines = []

  for line in lines:
    candidates = []
    try:
        decoded = base64.a85decode(line).decode()
        candidates.append(decoded)
    except:
        ...
    try:
      decoded = base64.b64decode(line).decode()
      candidates.append(decoded)
    except:
        ...
    try:
      decoded = bytes.fromhex(line).decode()
      candidates.append(decoded)
    except:
        ...
    try:
      decoded = bytes.fromhex(format(int(line), 'x')).decode()
      candidates.append(decoded)
    except:
        ...
    decoded = candidates[0].strip("\n")
    # print(decoded)
    decoded_lines.append(decoded)

  flag_lines = [line for line in decoded_lines if '[encoded]' in line]
  if flag_lines:
        encoded_flag = flag_lines[0].split("[encoded] flag: ")[1]
        print(encoded_flag.encode())
        flag = base64.b32decode(encoded_flag)
        print(flag)
        break

  round_lines = [line for line in decoded_lines if 'Round' in line]
  if round_lines:
      round_no = int(round_lines[0].split('#')[1])
      print(f"round {round_no}")
      if current_round is None or current_round != round_no:
          round_no = current_round
          rings_no = int([line for line in decoded_lines if 'Tower #1' in   line][0].split('Tower #1: ')[1].split(' ')[0])
          print(f"{rings_no} rings")
          moves = list(tower(rings_no, 1, 3, 2))
  move = moves.pop(0)
  io.sendline(f"Move the top disk of tower {move[0]} to tower {move[1]}".encode())
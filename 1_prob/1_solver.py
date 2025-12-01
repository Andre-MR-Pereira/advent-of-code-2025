INITIAL_POS = 50
terms = []

filename = "input"

with open(f"./{filename}.txt") as f:
  for line in f:
    line = line.strip('\n')
    if line[0] == 'R':
      terms.append({"number":int(line.split('R')[1]),"positive_sum":True})
    else:
      terms.append({"number":int(line.split('L')[1]),"positive_sum":False})
f.close()

current_pos = INITIAL_POS
password = 0
for term in terms:
    # print(f"------{term}-------")
    rotation_positions = term["number"] % 100
    current_pos = current_pos + rotation_positions if term["positive_sum"] else current_pos - rotation_positions
    if current_pos < 0:
        current_pos = 100 + current_pos
    elif current_pos > 100:
        current_pos = current_pos % 100
    current_pos = current_pos if current_pos != 100 else 0
    if current_pos == 0:
        password+=1
    # print(f"{current_pos} and pass {password}")

print(password)
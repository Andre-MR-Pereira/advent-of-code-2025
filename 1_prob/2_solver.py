import argparse

INITIAL_POS = 50
terms = []

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", required=False, default="input")

args = parser.parse_args()
filename = args.file

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
    full_rotation_clicks = term["number"] // 100
    rotation_positions = term["number"] % 100
    # print(f"{full_rotation_clicks} | {rotation_positions}")
    
    if term["positive_sum"]:
      current_pos = current_pos + rotation_positions
    else:
      if current_pos == 0:
        full_rotation_clicks -=1
      current_pos = current_pos - rotation_positions
    if current_pos < 0:
      full_rotation_clicks +=1
      current_pos = 100 + current_pos
    elif current_pos > 100:
      full_rotation_clicks +=1
      current_pos = current_pos % 100
    current_pos = current_pos if current_pos != 100 else 0
    if current_pos == 0:
      password +=1
    # print(f"{full_rotation_clicks} | {rotation_positions}")
    
    password+=full_rotation_clicks
    # print(f"{current_pos} and pass {password}")

print(password)
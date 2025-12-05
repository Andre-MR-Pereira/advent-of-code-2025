import argparse

def max_jolts(bank):
  digits = []
  starting_idx = 0
  for idx in range(11):
    digit = max(bank[starting_idx:-12+(idx+1)])
    starting_idx = bank[starting_idx:-12+(idx+1)].index(digit)+starting_idx+1
    digits.append(digit)
  digits.append(max(bank[starting_idx:]))
  return ''.join(str(digit) for digit in digits)

banks = []

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", required=False, default="input")

args = parser.parse_args()
filename = args.file

with open(f"./{filename}.txt") as f:
  for line in f:
    banks.append(list(map(int,line.strip('\n'))))
f.close()

cumulative_joltage = 0
for bank in banks:
  cumulative_joltage += int(max_jolts(bank))

print(cumulative_joltage)
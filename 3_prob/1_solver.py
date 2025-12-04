import argparse

def max_two_jolts(bank):
  first_digit_idx = bank.index(max(bank[:-1]))
  second_digit_idx = bank.index(max(bank[first_digit_idx+1:]))
  return f"{bank[first_digit_idx]}{bank[second_digit_idx]}"

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
  cumulative_joltage += int(max_two_jolts(bank))

print(cumulative_joltage)
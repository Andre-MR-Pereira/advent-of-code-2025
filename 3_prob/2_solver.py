import argparse

def max_jolts(bank):
  digits_idx = []
  mutable_bank = bank
  for idx in range(12):
    print(mutable_bank[:-12+idx])
    index = mutable_bank.index(max(mutable_bank[:-12+idx]))
    digits_idx.append(mutable_bank.index(max(mutable_bank[:-12+idx])))
    mutable_bank = mutable_bank[index+1:]
    if idx != 0:
      digits_idx[idx] += digits_idx[idx-1]+1
    print(f"{idx} | {digits_idx}")
  print("Final")
  for i, n in enumerate(digits_idx):
    print(f"{i}-{n}: {bank[i]}")
  return ''.join(str(bank[digit]) for digit in digits_idx)

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
  print(bank)
  print(int(max_jolts(bank)))
  # cumulative_joltage += int(max_two_jolts(bank))

print(cumulative_joltage)
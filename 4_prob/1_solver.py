import argparse

papers = []

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", required=False, default="input")

args = parser.parse_args()
filename = args.file

with open(f"./{filename}.txt") as f:
  for line in f:
    papers.append([1 if char=='@' else 0 for char in line.strip('\n')])
f.close()

number_row = len(papers)
number_columns = len(papers[0])
counter = 0
for i, row in enumerate(papers):
  compute_upper = True
  compute_lower = True
  for j, cell in enumerate(papers[i]):
    if cell == 1:
        if i == 0 :
            compute_upper = False
        elif i == number_row-1:
            compute_lower = False
        
        j_lower_limit = j-1
        j_upper_limit = j+2
        if j == 0:
            j_lower_limit = j
        elif j == number_columns-1:
            j_upper_limit = j+1
        
        upper_square_row = sum(papers[i-1][j_lower_limit:j_upper_limit]) if compute_upper else 0
        middle_square_row = sum(papers[i][j_lower_limit:j_upper_limit]) - cell
        lower_square_row = sum(papers[i+1][j_lower_limit:j_upper_limit]) if compute_lower else 0
        if upper_square_row + middle_square_row + lower_square_row < 4:
            counter += 1

print(counter)
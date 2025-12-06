import argparse

def merge_intervals(intervals):
    # Sort the input array by lower bound
    intervals = sorted(intervals,key= lambda entry: entry[0])
    # Initialize support variables
    result = []
    current_interval_index = 1
    current_lower_bound = intervals[0][0]
    current_upper_bound = intervals[0][1]
    # Iterate over the intervals
    while current_interval_index < len(intervals):
        # Update bounds
        merge_lower_bound = intervals[current_interval_index][0]
        merge_upper_bound = intervals[current_interval_index][1]
        #print(current_lower_bound,current_upper_bound,merge_lower_bound,merge_upper_bound)
        if merge_lower_bound > current_upper_bound: # New interval has been found
            #print(f"Storing {current_lower_bound} {current_upper_bound}")
            # Store the merged interval
            result.append([current_lower_bound,current_upper_bound])
            # Update the intervals current_upper_bound
            current_lower_bound = merge_lower_bound
            current_upper_bound = merge_upper_bound
        elif current_lower_bound <= merge_lower_bound and merge_lower_bound <= current_upper_bound: # Check merging possibility
            # Define the new intervals
            current_lower_bound = current_lower_bound
            current_upper_bound = current_upper_bound if current_upper_bound > merge_upper_bound else merge_upper_bound
        
        # Parse next available interval
        current_interval_index += 1
    
    if [current_lower_bound,current_upper_bound] not in result:
        # Store the final interval
        result.append([current_lower_bound,current_upper_bound])
    # Feed output
    return result

intervals = []
food_ids = []

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", required=False, default="input")

args = parser.parse_args()
filename = args.file

with open(f"./{filename}.txt") as f:
  collect_ids = False
  for line in f:
    if line == '\n':
       collect_ids = True
    else:
        if collect_ids:
            food_ids.append(int(line.strip('\n')))
        else:
            bounds = line.strip('\n').split('-')
            intervals.append([int(bounds[0]),int(bounds[1])])
f.close()

intervals = merge_intervals(intervals)
valid_ids = 0
for bounds in intervals:
    valid_ids += bounds[1] - bounds[0] + 1

print(valid_ids)
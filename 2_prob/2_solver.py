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

def isRepeatedSequence(number):
    str_num = str(number)
    size_number = len(str_num)
    if size_number == 1:
        return 0
    elif size_number == 2:
        return number if str_num[0] == str_num[1] else 0
    else:
        window_sizes = range(size_number//2)
        for window_size in window_sizes:
            pointer = 0
            matcher = str_num[0:(window_size+1)]
            invalid = True
            while pointer < size_number:
                current = str_num[pointer:pointer+(window_size+1)]
                if current != matcher:
                    invalid = False
                    break
                pointer += (window_size+1)
            if invalid and pointer + (window_size+1) + 1 >= size_number:
                return number
        return 0

ranges = []

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", required=False, default="input")

args = parser.parse_args()
filename = args.file

with open(f"./{filename}.txt") as f:
  for line in f:
    ranges = [[int(interval.split('-')[0]),int(interval.split('-')[1])] for interval in line.split(',')]
    break
f.close()

parsed_interval_ranges = merge_intervals(ranges)
count = 0
for interval in parsed_interval_ranges:
   for i in range(interval[1]-interval[0]+1):
      count += isRepeatedSequence(interval[0]+i)
      
print(count)
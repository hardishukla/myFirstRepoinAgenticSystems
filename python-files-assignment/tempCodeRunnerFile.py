input_file_name = "numbers.txt"
log_file_name = "results.log"

with open(input_file_name, "r") as file:
    print("File opened successfully")

    numbers_list = []
    for line in file:
        line = line.strip()
        if line:                      # Skip empty lines
            numbers_list.append(int(line))

total_numbers = len(numbers_list)
total_sum = sum(numbers_list)
average = total_sum / total_numbers if total_numbers else 0

print(f"Read {total_numbers} numbers")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print("Processing completed")

with open(log_file_name, "a") as log:
    log.write("---- New Run ----\n")
    log.write("File opened successfully\n")
    log.write(f"Read {total_numbers} numbers\n")
    log.write(f"Sum: {total_sum}\n")
    log.write(f"Average: {average}\n")
    log.write("Processing completed\n\n")

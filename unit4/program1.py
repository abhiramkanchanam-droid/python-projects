# Create a log file
file = open("log.txt", "w")

file.write("System started\n")
file.write("User logged in\n")
file.write("File opened successfully\n")
file.write("System stopped\n")

file.close()

# Read the log file
file = open("log.txt", "r")

print("----- LOG FILE CONTENTS -----")

for line in file:
    print(line, end="")

file.close()
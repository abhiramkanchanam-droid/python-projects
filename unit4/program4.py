import json

# Sample log data
logs = [
    {"level": "INFO", "message": "System started"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "INFO", "message": "User logged in"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "ERROR", "message": "Database error"},
    {"level": "INFO", "message": "System stopped"}
]

# Store logs in JSON file
with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

# Read JSON file
with open("logs.json", "r") as file:
    data = json.load(file)

# Count log types
info = 0
error = 0
warning = 0

for log in data:
    if log["level"] == "INFO":
        info += 1

    elif log["level"] == "ERROR":
        error += 1

    elif log["level"] == "WARNING":
        warning += 1

# Display report
print("--- LOG ANALYSIS REPORT ---")
print("Total Logs:", len(data))
print("INFO Logs:", info)
print("ERROR Logs:", error)
print("WARNING Logs:", warning)
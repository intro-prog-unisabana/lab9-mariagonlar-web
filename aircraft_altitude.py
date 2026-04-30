from aircraft import Aircraft

model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

    if command == "X":
        break

    parts = command.split()

    if len(parts) == 2:
        action = parts[0]
        feet = int(parts[1])

        if action == "A":
            aircraft.climb(feet)  
        elif action == "D":
            aircraft.descend(feet)

print(f"Final altitude: {aircraft.altitude} feet")
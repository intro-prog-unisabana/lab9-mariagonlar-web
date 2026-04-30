from aircraft import Aircraft

model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

    if command == "X":
        break

    parts = command.split()

    if len(parts) < 2:
        continue  

    action = parts[0]

    try:
        feet = int(parts[1])
    except:
        continue  

    if action == "A":
        aircraft.ascend(feet)
    elif action == "D":
        aircraft.descend(feet)

print(f"Final altitude: {aircraft.altitude} feet")
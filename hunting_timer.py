
#!/usr/bin/env python


# Get input from user
location = input("Enter the hunt location: ")
pokemon_type = input("Enter the pokemon type: ")
hunt_time = input("Enter the hunt time in the format HH:MM:SS: ")
money_per_minute = float(input("Enter how much money you make per minute: "))

# Calculate total money earned
hours, minutes, seconds = [int(x) for x in hunt_time.split(":")]
total_minutes = hours * 60 + minutes + seconds / 60
total_money = total_minutes * money_per_minute

# Print results
print("\nHunt Location: {}".format(location))
print("Pokemon Type: {}".format(pokemon_type))
print("Hunt Time: {} hours, {} minutes, {} seconds".format(hours, minutes, seconds))
print("Money per minute: {:.2f}".format(money_per_minute))
print("Total Money: {:.2f}".format(total_money))

# Predict earnings for additional time
additional_time = input("\nEnter additional time in the format HH:MM:SS: ")
add_hours, add_minutes, add_seconds = [int(x) for x in additional_time.split(":")]
add_minutes += add_hours * 60
add_seconds += add_minutes * 60
add_money = add_minutes * money_per_minute + add_seconds / 60 * money_per_minute
print("Predicted earnings with additional time: {:.2f}".format(total_money + add_money))


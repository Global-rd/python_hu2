# Get user input, so Sarah can go on a holiday! 
city = input("Enter the city: ").strip().title()
rent = int(input("Enter the monthly rent in USD: "))

# Decision 
match city:
    case "Chicago":
        can_move = True  # No rent limit, she loves it!
    case "Washington":
        can_move = False  # She hates it, never moving there.
    case "New York" | "San Francisco":
        can_move = rent < 4000  # Only if rent is under 4000 USD
    case _:
        can_move = rent <= 3000  # Any other city: max 3000 USD rent

# Print the result
print(f"Sarah {'can' if can_move else 'cannot'} move to {city} with a rent of {rent} USD.")
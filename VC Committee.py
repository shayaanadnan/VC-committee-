# Input number of members
num_members = int(input("Enter the number of members: "))

# Input names of members and amount contributed
members = []
contributions = []
for i in range(num_members):
    name = input(f"Enter the name of member {i+1}: ")
    contribution = float(input(f"Enter the amount contributed by {name}: "))
    members.append((i+1, name, contribution))

# Calculate the total amount contributed
total_contributed = sum(member[2] for member in members)

# Print the list of members with numbers
print("\nList of members with numbers:")
for member in members:
    print(f"{member[0]}. {member[1]}")

# Print the total amount contributed
print(f"\nTotal amount contributed: {total_contributed}")

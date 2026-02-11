def calculate_average(scores):
    """Return the average of a list of integers."""
    if len(scores) == 0:   # Avoid division by zero
        return 0
    return sum(scores) / len(scores)


def has_admin_access(roles):
    """Return True if user has admin role, else False."""
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 90, 85],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 60, 75],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [95, 88, 92],
            "roles": {"admin"}
        }
    ]

    for user in users:
        avg_score = calculate_average(user["scores"])
        admin_status = has_admin_access(user["roles"])

        print("Name:", user["name"])
        print("Average Score:", avg_score)
        print("Admin Access:", admin_status)
        print()  # Blank line for readability


# Run program
main()

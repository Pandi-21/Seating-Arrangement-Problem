# Problem:
# Given N guests and their two preferred neighbors,
# find a valid circular seating arrangement where each guest sits
# next to both of their preferred neighbors.
# If it's not possible, state that clearly.

# solution:
# Use backtracking to try to arrange guests one by one,
# making sure each new guest satisfies the neighbor preferences.
# At the end, also check if the first and last guests are happy neighbors
# because it is a circular table.

def seating(guests):
    def is_valid(seat, guest):
        # Check if the previous guest and guest are mutual neighbors
        if len(seat) == 0:
            return True
        prev_guest = seat[-1]
        return (guest in guests[prev_guest]) and (prev_guest in guests[guest])

    def backtrack(seat, remaining):
        if not remaining:
            # Check circular condition first and last must be neighbors
            return (seat[0] in guests[seat[-1]]) and (seat[-1] in guests[seat[0]])
        
        for guest in list(remaining):
            if is_valid(seat, guest):
                seat.append(guest)
                remaining.remove(guest)
                if backtrack(seat, remaining):
                    return True
                # Backtrack
                seat.pop()
                remaining.add(guest)
        return False

    seat = []
    if backtrack(seat, set(guests.keys())):
        return seat
    else:
        return "No valid seating neighbors arrangement possible."

guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = seating(guests)
print(result)

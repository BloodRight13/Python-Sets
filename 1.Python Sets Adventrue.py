# Task 1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_routes = our_routes.intersection(competitor_routes)
print(f"We use these same routes as out competitors: {same_routes}\n")

different_routes = our_routes.difference(competitor_routes)
print(f"However we have these routes that our competitors don't: {different_routes}\n")

None_shared_routes = our_routes.symmetric_difference(competitor_routes)
print(f"Routes neither airline shares: {None_shared_routes}\n")

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dictionary
travel_log = {
   # "France": "Paris", "Lille", "Dijon"   X wrong
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# nesting a dictionary in a dictionary
travel_log1 = {
   # "France": "Paris", "Lille", "Dijon"   X wrong
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# nesting dictionary in a list
travel_log2 = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5,
     },
]
print(travel_log2)
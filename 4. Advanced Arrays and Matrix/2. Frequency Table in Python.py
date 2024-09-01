# *** USING A DICTIONARY ***

def frequency_table_dict(data):
    table = {}
    for item in data:
        if item in table:
            table[item] += 1
        else:
            table[item] = 1
    return table


data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 7, 8, 8, 8]
frequency = frequency_table_dict(data)
print(frequency)  # Output : {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 1, 7: 2, 8: 3}

# *** USING Collections.Counter ***
# Counter is a dictionary subclass specifically designed for counting hashable objects
# from collections import Counter
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 7, 8, 8, 8]
# frequency = Counter(data)
# print(frequency) # Output :- Counter({5: 5, 4: 4, 3: 3, 8: 3, 2: 2, 7: 2, 1: 1, 6: 1})

# def most_popular_station(train_routes):
#     """
#     Finds the most popular station from a list of train routes.
#
#     Args:
#       train_routes: A list of lists, where each inner list represents the stations a train passes through.
#
#     Returns:
#       A tuple containing:
#         - The most popular station(s).
#         - The maximum number of trains passing through a station.
#     """
#     station_counts = {}
#     for route in train_routes:
#         for station in route:
#             if station in station_counts:
#                 station_counts[station] += 1
#             else:
#                 station_counts[station] = 1  # Initialize if not present
#
#     max_trains = max(station_counts.values())
#     most_popular = [station for station, count in station_counts.items() if count == max_trains]
#     return most_popular, max_trains
#
#
# train_routes = [
#     ['S1', 'S2', 'S3'],
#     ['S2', 'S4'],
#     ['S1', 'S2', 'S4'],
#     ['S3', 'S4']
# ]
#
# most_popular, max_count = most_popular_station(train_routes)
# print(f"The most popular station(s) are: {most_popular} with {max_count} trains.")

# This is a sample Python script.

cities=["Amsterdam", "Paris", "Bucharest", "Dublin", "Lisbon", "Madrid", "Bordeaux", "London", "Glasgow", "Lyon", "Barcelona", "Milan", "Rome", "Palermo", "Vienna", "Munich", "Berlin", "Prague", "Copenhagen", "Stockholm", "Helsinki", "Oslo", "Warsaw", "Budapest", "Belgrad", "Sofia", "Athens"]
print(len(cities))
rows = 12
cols = 3
cities_connections=[["Oslo-Helsinki", "Rome-Milan", "Madrid-Barcelona"], ["Helsinki-Stockholm", "Milan-Budapest", "Madrid-Lisbon"], ["Oslo-Stockholm", "Vienna-Budapest", "Lisbon-London"], ["Stockholm-Copenhagen", "Vienna-Munich", "Barcelona-Lyon","Copenhagen-"]]
cities_dist = [[0 for _ in range(cols)] for _ in range(rows)]


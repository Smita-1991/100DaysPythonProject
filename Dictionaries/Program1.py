colours={
    "Apple":"Red",
    "Pear":"Green",
    "Orange":"Orange",
    "flowers":["rose","jasmin","marigold"]
}

for key in colours:
    print(key)
    print(colours[key])

travel_Log={
    "France": {
        "citiesVisited":["Paris","Little","Dijon"],
        "totalVisits" : 12
    },
    "Germany": {
        "citiesVisited":["Berlin","Hamburg","stutgart"],
        "totalVisits" : 21
    }
}

print(travel_Log["France"]["totalVisits"])
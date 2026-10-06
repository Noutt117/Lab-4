from classes1 import Team, Driver

# your code here
teams = {}

with open("f1_points.csv", "r") as file:
    file.readline()

    for line in file:
        data = line.strip().split(",")

        driver_name = data[0]
        team_name = data[1]
        points = int(data[2])

        if team_name not in teams:
            teams[team_name] = Team(team_name)

        driver = Driver(driver_name, points)
        teams[team_name].add_driver(driver)

teams = list(teams.values())

for team in sorted(teams):
    print(team)

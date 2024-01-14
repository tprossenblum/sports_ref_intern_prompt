import json

# open json file and store data
f = open('sport_ref.json')
data = json.load(f)

# store the teams to loop through later
teams = list(data.keys())

# initialize the header and column string
header = ' |---|'
rows = ''
# loop through the teams and create header and team in row
# ^5 and ^3 are used for spacing
for i in range(len(teams)):
    header = header + f'{teams[i]:^5}|'
    rows = rows + f'\n |{teams[i]:^3}|'
    # nested loop to get results from the teams
    for j in range(len(teams)):
        # if on the same step we skip as it would be against own team
        if i == j:
            rows += " --- |"
        # if valid data retrieve appropriate W column and print
        else:
            rows += f" {data[teams[i]][teams[j]]['W']:^3} |"

# print header and columns to display data
print(header, end='')
print(rows)




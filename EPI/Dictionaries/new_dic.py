
# Classic dictionary creation
fif_team = {'Abidjan': 'Asec Mimosa',
            'Bouake': 'Bouake FC',
            'Seguela':'AS Denguele',
            'San Pedro': 'Wack FC',
            'Bingerville': 'ES Bingerville'}

print(fif_team)

# Create a dictionary using built in function
fif_team2 = dict([('Abidjan', 'Asec Mimosa'),
                  ('Bouake', 'BFC'),
                  ('Seguela','AS Denguele'),
                  ('San Pedro','Wack FC')])
print(fif_team2)

# Accessing Dictionaries values
a = fif_team['Abidjan']
print(a)

# Adding entry to an existing dictionary
fif_team['korhogo'] = 'CO Korhogo'
print(fif_team)

# Update an entry
fif_team['Bouake'] = 'Pakano Fc'
print(fif_team)

# Delete an entry
del fif_team['Bingerville']
print(fif_team)

# Building a Dictionary Incrementally
check_list = {}

check_list['fname'] = 'Zoumanan'
check_list['lname'] = 'Tokos'
check_list['Age'] = '55'
check_list['Spouse'] = 'Adrienne'
check_list['Children'] = ['Paul', 'Pierre', 'Dan']
print(check_list)
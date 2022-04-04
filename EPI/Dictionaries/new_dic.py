
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

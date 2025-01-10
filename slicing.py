#STRING METHOD
first_name = 'taylor'
last_name = 'swift'
note = 'award: Spotify 2024 Global Top Artist'

#String Method: 'capilitalize'
    #Variable Creation for first, last, and award elements 
first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
award_location = note.find('award: ')
award_text = note[7:] #slicing with slice notation

#Print statements 
print(first_name_cap)
print(last_name_cap)
print(award_location)
print(award_text)
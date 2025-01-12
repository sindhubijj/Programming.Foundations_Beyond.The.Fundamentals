#CHALLENGE #4
def plant_recommendation(care):
    if care == 'low': #'==' is needed for comparison 
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')

plant_recommendation('low') 
plant_recommendation('medium')
plant_recommendation('high')

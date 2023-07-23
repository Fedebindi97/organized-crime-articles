countries = {'US':['US','United States','USA','the States','EE.UU.','EEUU','Estados Unidos'],
             'Colombia':['Colombia'],
             'Mexico':['Mexico'],
             'Peru':['Peru'],
             'Venezuela':['Venezuela'],
             'Brazil':['Brazil','Brasil']}


gangs = {'Sinaloa Cartel':['Sinaloa Cartel','Cartel de Sinaloa','CDS','Cartel del Pacifico'],
         'Jalisco Cartel':['Cartel de Jalisco Nueva Generación','CJNG','Los Mata Zetas'],
         'Golfo Cartel':['Cartel del Golfo','CDG'],
         'Norest Cartel':['Cartel del Noreste','CDN']}

drugs = {'cocaine': ['cocaine','coca'],
        'eroine':['eroine','eroina']}

for key,value in dict_to_check.items():
    df[f'contains_{key}'] = df.text.apply(lambda text: any([unidecode(element.lower()) in unidecode(text.lower()) for element in value]))
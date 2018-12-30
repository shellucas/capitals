#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random
# order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals_europe = {
    'Albania':	'Tirana',
    'Andorra':	'Andorra la Vella',
    'Armenia':	'Yerevan',
    'Austria':	'Vienna',
    'Azerbaijan':	'Baku',
    'Belarus':	'Minsk',
    'Belgium':	'Brussels',
    'Bosnia and Herzegovina':	'Sarajevo',
    'Bulgaria':	'Sofia',
    'Croatia':	'Zagreb',
    'Cyprus':	'Nicosia',
    'Czech Republic':	'Prague',
    'Denmark':	'Copenhagen',
    'Estonia':	'Tallinn',
    'Finland':	'Helsinki',
    'France':	'Paris',
    'Georgia':	'Tbilisi',
    'Germany':	'Berlin',
    'Greece':	'Athens',
    'Hungary':	'Budapest',
    'Iceland':	'Reykjavik',
    'Ireland':	'Dublin',
    'Italy':	'Rome',
    'Kazakhstan':	'Astana',
    'Kosovo':	'Pristina',
    'Country':	'Capital city',
    'Latvia':	'Riga',
    'Liechtenstein':	'Vaduz',
    'Lithuania':	'Vilnius',
    'Luxembourg':	'Luxembourg (city)',
    'Macedonia (FYROM)':	'Skopje',
    'Malta':	'Valletta',
    'Moldova':	'Chisinau',
    'Monaco':	'Monaco',
    'Montenegro':	'Podgorica',
    'Netherlands':	'Amsterdam',
    'Norway':	'Oslo',
    'Poland':	'Warsaw',
    'Portugal':	'Lisbon',
    'Romania':	'Bucharest',
    'Russia':	'Moscow',
    'San Marino':	'San Marino',
    'Serbia':	'Belgrade',
    'Slovakia':	'Bratislava',
    'Slovenia':	'Ljubljana',
    'Spain':	'Madrid',
    'Sweden':	'Stockholm',
    'Switzerland':	'Bern',
    'Turkey':	'Ankara',
    'Ukraine':	'Kiev',
    'United Kingdom':	'London',
    'Vatican City (Holy See)':	'Vatican City'
}

# Generate 35 quiz files.
for quizNum in range(20):

    #TODO: Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quiz + 1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    

    #TODO: Shuffle the order of countries

    #TODO: Loop through all countries making a question for each



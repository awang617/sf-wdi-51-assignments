import random

## an array of state dictionaries

states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]


test_states = [
{
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}
]

def add_keys(lyst): 
    for dictionary in lyst: 
        dictionary['correct'] = 0
        dictionary['wrong'] = 0

def game_scorce(lyst):
    for dictionary in lyst:
        dictionary['game_correct'] = 0
        dictionary['game_wrong'] = 0

def tally_score(lyst):
    total_correct = 0
    total_wrong = 0
    for state in lyst:
        total_correct += state['game_correct']
        total_wrong += state['game_wrong']
    print('You got', total_correct, 'correct.')
    print('You got', total_wrong, 'wrong.')

def end_game(state_list, games):
    end = input('Would you like to play again? (yes/no) ')
    if end.lower().strip() == 'yes':
        play(state_list, games)
    else: 
        print('Goodbye!')

def play(state_list, counter):
    counter += 1
    game_scorce(state_list)
    shuffled_test = random.sample(state_list, len(state_list))
    for state in shuffled_test:
        print(state['name'])
        prompt = input('What is the capital? ')
        if prompt == state['capital']:
            state['correct'] += 1
            state['game_correct'] += 1
            print('correct')
        else:
            state['wrong'] += 1
            state['game_wrong'] +=1
            print('wrong')
        print('This was answered correctly', state['correct'], 'out of', counter, 'times.')
    tally_score(state_list)
    end_game(state_list, counter)

print('Welcome to the game!')
game_counter = 0
add_keys(test_states)
add_keys(states)
play(states, game_counter)
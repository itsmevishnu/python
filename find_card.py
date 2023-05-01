cards = [1,4,5,6,8,9,12] #input
query = 5 #input
output = 2 #output

def locate_card(cards, query):
    
    position = 0
    
    while(position<len(cards)):
        if cards[position] == query:
            return position
        position += 1
    return -1

#test cases
tests = []
test = {
    'input': {
        'cards': [1,4,5,6,8,9,12],
        'query': 5
    }, 
    'output': 2 
}

tests.append(test)
tests.append(
    {
        'input': {
            'cards': [1,4,5,6,8,9,12],
            'query': 1
        }, 
        'output': 0 
    }
)

tests.append(
    {
        'input': {
            'cards': [1,4,5,6,8,9,12],
            'query': 12
        }, 
        'output': 6
    }
)
tests.append(
    {
        'input': {
            'cards': [1],
            'query': 1
        }, 
        'output': 0
    }
)
tests.append(
    {
        'input': {
            'cards': [1,4,5],
            'query': 3
        }, 
        'output': -1
    }
)
tests.append(
    {
        'input': {
            'cards': [1,1,4,4,5],
            'query': 4 
        }, 
        'output': 2
    },
    tests.append(
    {
        'input': {
            'cards': [],
            'query': 4 
        }, 
        'output': -1
    }
)

for test in tests:
    result = locate_card(test['input']['cards'], test['input']['query'])
    if (result == test['output']):
        print("Test passed")
    else:
        print("Test failed")
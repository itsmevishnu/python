cards = [1,4,5,6,8,9,12] #input
query = 6 #input

output = 3


def binary_search(cards, query):
    low = 0
    high = len(cards)
    while(low<=high):
        mid = (low + high)//2
        if(cards[mid]== query):
            return mid
        elif cards[mid]<query:
            low = mid+1
        else:
            high = mid -1
    return -1




test = {
    'input': {
        'cards': [1,4,5,6,8,9,12],
        'query': 6
    },
    'output': 3
}

result = binary_search(test['input']['cards'], test['input']['query'])

print(result == output)
cards = [-1,0,3,5,9,12] #input
query = 9 #input

output = 4


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
        'cards': [-1,0,3,5,9,12],
        'query': 9
    },
    'output': 4
}

result = binary_search(test['input']['cards'], test['input']['query'])
print(result)
print(result == output)
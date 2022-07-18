# Binary Search
# Assuming list is sorted in ascending order

def check_repeats(cards, query, mid):

    mid_card = cards[mid]
    if mid_card == query:
        if (mid - 1) > 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_card < query:
        return 'right'
    else:
        return 'left'


def binary_search(cards, query):
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = len(cards) // 2
        mid_card = cards[mid]
        result = check_repeats(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'right':
            lo = mid + 1
        elif result == 'left':
            hi = mid - 1
    return -1

# Generic Binary Search

def binarysearch(lo, hi, condition):

    while lo <=hi:
        mid = lo + hi // 2
        result = condition(mid)
        if result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1
        else:
            return mid
    else:
        return -1

def locate_cards (cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid>0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'right'
        else:
            return 'left'
    return (binarysearch(0, len(cards) - 1, condition))
        

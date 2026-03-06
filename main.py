import sys

def fifo(k, requests):
    '''
    First In, First Out

    Comments
    --------
    First item is the item that has been in the cache for the longest
    '''
    cache = []
    miss_count = 0
    for r in requests:
        if r not in cache:
            miss_count += 1
            if len(cache) < k:
                cache.append(r)
            else:
                del cache[0]
                cache.append(r)
    return miss_count


def lru(k, requests):
    '''
    Least Recently Used

    Comments
    --------
    First item is the item whose most recent access time is the longest
    If there is a hit, remove the item and append to the end of the cache list
    Last item is the item whose most recent access time is the shortest
    '''
    cache = []
    miss_count = 0
    for r in requests:
        if r not in cache:
            miss_count += 1
            if len(cache) < k:
                cache.append(r)
            else:
                del cache[0]
                cache.append(r)
        else:
            cache.remove(r)
            cache.append(r)
    return miss_count


def optff(k, m, requests):
    '''
    Belady’s Farthest-in-Future, optimal offline

    Comments
    --------
    Iterate through items in the cache, evict first item NOT found in request list OR evict item with the largest index in the request list
    When looking for index in the request list, only record the index of the first request for the item
    '''
    cache = []
    miss_count = 0
    for i in range(m):
        if requests[i] not in cache:
            miss_count += 1
            if len(cache) < k:
                cache.append(requests[i])
            else:
                max_index = 0
                remove_index = -1
                remaining_requests = requests[i:]
                for cache_index in range(k):
                    item = cache[cache_index]
                    if item not in remaining_requests:
                        remove_index = cache_index
                        break
                    else:
                        if remaining_requests.index(item) > max_index:
                            max_index = remaining_requests.index(item)
                            remove_index = cache_index
                cache.pop(remove_index)
                cache.append(requests[i])
    return miss_count


def main():
    input_file = sys.argv[1]

    # Read input file
    with open(input_file, 'r') as file:
        # First line contains k = cache size and m = number of requests
        k, m = file.readline().split()
        k = int(k)
        m = int(m)
        
        # Second line contains m number of requests which is a sequence of integer IDs
        str_requests = file.readline().split()
        requests = [int(r) for r in str_requests]

    # Run cache eviction policies on requests list
    print(f'FIFO  : {fifo(k, requests)}')
    print(f'LRU   : {lru(k, requests)}')
    print(f'OPTFF : {optff(k, m, requests)}')
    

if __name__ == '__main__':
    main()
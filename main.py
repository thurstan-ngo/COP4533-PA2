import sys

def fifo(k, requests):
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


if __name__ == '__main__':
    main()
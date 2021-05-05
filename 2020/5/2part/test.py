
def missing_elements(L, start, end):
    print(f'L: {L} start: {start} end: {end}')
    if end - start <= 1: 
        if L[end] - L[start] > 1:
            yield from range(L[start] + 1, L[end])
        return

    index = start + (end - start) // 2
    print(f'index: {index}')
    # is the lower half consecutive?
    consecutive_low =  L[index] == L[start] + (index - start)
    print(f'clow: {consecutive_low}')
    if not consecutive_low:
        yield from missing_elements(L, start, index)

    # is the upper part consecutive?
    consecutive_high =  L[index] == L[end] - (end - index)
    print(f'chigh: {consecutive_high}')
    if not consecutive_high:
        yield from missing_elements(L, index, end)


def main():
    L = [10,11,13,14,15,16,17,18,20]
    print(list(missing_elements(L,0,len(L)-1)))
    L = range(10, 21)
    print(list(missing_elements(L,0,len(L)-1)))


main()

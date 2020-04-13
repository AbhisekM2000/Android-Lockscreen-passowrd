import math

# Size of grid
N_GRID_X = 3
N_GRID_Y = 4

# Number of dots used
N_DOTS = 12

# Mutable variable
COUNT = [0]

def recursive_enumerate(available, prev, n_dots):

    '''
    available: The available positions
    prev: The previous position taken
    n_dots: Number of dots that should be taken
    '''
    # Checks if pattern has been found
    if len(available) == N_GRID_X*N_GRID_Y - n_dots:
        COUNT[0] += 1
        return

    # For each dot to try next
    for a in available:

        # Make a copy since lists are mutable
        copy = available.copy()

        # If no previous dot (first dot)
        if prev == -1:
            copy.remove(a)
            recursive_enumerate(copy, a, n_dots)
            continue

        # If previous dot exists:

        gcd = math.gcd(a[0] - prev[0], a[1] - prev[1])
        diff = ((a[0] - prev[0])//gcd, (a[1] - prev[1])//gcd)

        to_remove = []
        for i in range(1,gcd+1):
            middle = (prev[0] + diff[0]*i, prev[1] + diff[1]*i)
            if middle in copy:
                to_remove.append(middle)

        if len(to_remove) > 1:
            continue

        copy.remove(to_remove[0]) 
        recursive_enumerate(copy, a, n_dots)

available = [(i,j) for i in range(N_GRID_X) for j in range(N_GRID_Y)]
prev = -1
recursive_enumerate(available, prev, N_DOTS)

print("COUNT =", COUNT[0])

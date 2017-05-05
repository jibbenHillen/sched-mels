# in minutes
PEAK_START = 30
PEAK_SCALE = 45
PEAK_END = 90
PEAK_ARR = 1
BASE_ARR = 10
ARR_INTERVAL = 2

# in minutes
OPEN_TIME = 360

# average waiting
RENEGE_RATE = 0.6 * 60

SIZE_TO_SEATED = { # in hours
        2 : (1.1, 0.15),
        3 : (1.2, 0.2),
        4 : (1.25, 0.23),
        5 : (1.4, 0.24),
        6 : (1.6, 0.28),
        7 : (1.65, 0.3),
        8 : (2, 0.35),
}


ARRIVAL_TO_SIZE = {
        0 : 0.0,
        1 : 0.0,
        2 : 0.24,
        3 : 0.46,
        4 : 0.75,
        5 : 0.85,
        6 : 0.97,
        7 : 0.98,
        8 : 1.0,
}

TABLES = [
    [0, 4, [1,3], 0],
    [1, 4, [0,2,4], 0],
    [2, 4, [1,5], 0],
    [3, 2, [0,4], 0],
    [4, 2, [1,3,5], 0],
    [5, 2, [2,4], 0],
    [6, 4, [3, 8, 9], 0],
    [7, 4, [8, 10,5], 0],
    [8, 2, [6, 7, 9, 10], 0],
    [9, 4, [6, 8], 0],
    [10, 4, [7, 8], 0],
    [11, 4, [12], 1],
    [12, 2, [11, 13], 1],
    [13, 2, [12, 14], 1],
    [14, 4, [13, 15], 1],
    [15, 2, [14, 16], 1],
    [16, 2, [15,17], 1],
    [17, 2, [16,18], 1],
    [18, 4, [17, 19], 1],
    [19, 2, [18, 20], 1],
    [20, 2, [19,21], 1],
    [21, 4, [20], 1],
    [22, 4, [23, 24], 2],
    [23, 4, [22, 25], 2],
    [24, 4, [22, 25], 2],
    [25, 4, [23, 24], 2],
    [26, 2, [29, 24], 2],
    [27, 4, [28], 2],
    [28, 4, [27], 2],
    [29, 2, [26, 30], 2],
    [30, 4, [29], 2],
    [31, 12, [], 2],
    [32, 6, [], 3],
    [33, 6, [], 3],
    [34, 4, [35,37], 3],
    [35, 4, [34, 36, 38], 3],
    [36, 4, [35,39], 3],
    [37, 4, [34,38], 3],
    [38, 4, [35,37], 3],
    [39, 2, [36], 3]
]

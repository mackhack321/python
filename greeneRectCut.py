def cutit(h,w):
    dirs = ((1,0),(-1,0),(0,-1),(0,1))
    if h & 1: h,w = w,h
    if h & 1: return 0
    if w == 1: return 1
    count = 0

    next = [w+1, -w-1, -1, 1]
    blen = (h+1) * (w+1) - 1
    grid = [False] * (blen + 1)
cutit(3,4)

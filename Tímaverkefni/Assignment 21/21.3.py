def check_bricks(small_bricks, big_bricks, goal):
    return  ((small_bricks + big_bricks*5) >= goal) and (goal%5 <= small_bricks)
import math
def find_next_square(sq):
    if math.sqrt(sq).is_integer():
        return (sq**0.5+1)**2
    else : return -1
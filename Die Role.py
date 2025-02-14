import math

def die_roll_probability(Y, W):
    max_value = max(Y, W)
    favorable = 6 - max_value + 1
    gcd_value = math.gcd(favorable, 6)  
    print(f"{favorable // gcd_value}/{6 // gcd_value}")


Y, W = map(int, input().split())

die_roll_probability(Y, W)

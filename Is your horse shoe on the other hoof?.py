def minimum_horseshoes_to_buy(s1, s2, s3, s4):
    horseshoes = {s1, s2, s3, s4}
    return 4 - len(horseshoes)


s1, s2, s3, s4 = map(int, input().split())


print(minimum_horseshoes_to_buy(s1, s2, s3, s4))

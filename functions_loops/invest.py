def invest(amt, rate, time):
    print('principal amount: ${}'.format(amt))
    print('annual rate of return: {}'.format(rate))
    for i in range(1, time + 1):
        amt = amt * (1 + rate)
        print('year {}: ${}'.format(i, amt))


invest(100, .05, 8)
invest(2000, .025, 5)

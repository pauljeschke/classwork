def calc(speed):
    from math import ceil
    if speed <= 70:
        print("Ok")
        return
    points = ceil((speed - 70.0)/5.0)
    print(f"Congrats: You've earned {points} demerit point{'s' if points > 1 else ''}. {'Ease off the lead foot next time.' if points < 12 else ''}")
    if points >= 12:
        print("Ok Speedster, license suspended.")
speed = 160
calc(speed)
def task16():
    n = int(input())
    places = [0] * n
    seat = list(map(int, input().split()))
    for guest_number, place in enumerate(seat, start=1):
        places[place - 1] = guest_number

    print(*places)
task16()

cards = [str(i) for i in range(1, int(input()) + 1)]
shuffle_indices = tuple(map(int, input().split()))

for index in shuffle_indices:
    if index == 0:
        continue

    first_half = cards[:index]
    second_half = cards[index:]
    cards = []

    while first_half or second_half:
        if not first_half:
            cards += second_half
            break

        if not second_half:
            cards += first_half
            break

        cards.append(first_half.pop(0))
        cards.append(second_half.pop(0))

print(" ".join(cards))
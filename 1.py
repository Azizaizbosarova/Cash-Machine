def cash_machine(actions):
    player1_coins = 3
    player2_coins = 3
    results = []

    for p1_action, p2_action in actions:
        if p1_action == "share" and p2_action == "share":
            player1_coins += 2
            player2_coins += 2
        elif p1_action == "share" and p2_action == "steal":
            player1_coins -= 1
            player2_coins += 3
        elif p1_action == "steal" and p2_action == "share":
            player1_coins += 3
            player2_coins -= 1
        elif p1_action == "steal" and p2_action == "steal":
            pass
        results.append((player1_coins, player2_coins))

    return results
inputs = [
    ["share", "share"],
    ["steal", "share"],
    ["steal", "steal"],
    ["share", "steal"],
]
outputs = cash_machine(inputs)
for round_result in outputs:
    print(round_result)

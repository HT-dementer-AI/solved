# python은 한줄을 그냥 input으로 받을수 있음
while True:
    value = input()

    if value == '#':
        break

    alpa, sentence = value[0], value[1:].lower()

    alpaCount = sentence.count(alpa)

    print(alpa, alpaCount)

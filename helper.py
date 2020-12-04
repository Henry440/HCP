

def inp(msg, values):

    for i in range(len(values)):
        values[i] = str(values[i])

    score = ""
    while not(score in values):
        print(msg)
        score = str(input("> "))
    return score


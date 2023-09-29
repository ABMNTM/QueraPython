def fruits(touple_of_fruits:tuple) -> dict :
    goodFruits = {}
    for fruit in touple_of_fruits:
        if fruit['shape'] == 'sphere':
            if 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
                if fruit['name'] in goodFruits.keys():
                    goodFruits[fruit['name']] += 1
                else:
                    goodFruits[fruit['name']] = 1
    return goodFruits
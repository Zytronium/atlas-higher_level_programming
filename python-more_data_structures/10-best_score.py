#!/usr/bin/python3
def best_score(a_dictionary):
    hi_score = 0
    hi_score_key = None
    for key, value in a_dictionary.items():
        if value > hi_score:
            hi_score = value
            hi_score_key = key
    return hi_score_key

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
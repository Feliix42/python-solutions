# task 8


import sys
import json

# for saving the stats
stats = {}


def save_stats():
    '''
    Dumps the gathered stats to a JSON file
    '''
    with open('stats.json', 'w') as f:
        json.dump(stats, f, indent=4)
    print('Speichern erfolgreich :)')


def statistic(filename='res/loremipsum.txt'):
    '''
    Takes a file as input and counts, how often a word occurs, which is stored
    in the dict called `stats`. If no filename is given, the loremipsum file
    will be counted.
    '''
    with open(filename, 'r')as f:
        for line in f:
            line = line.split(' ')
            for word in line:
                if word in stats:
                    stats[word] += 1
                else:
                    stats[word] = 1


def print_stats():
    '''
    Prints the gathered text statistics to the console by iterating over
    the `stats` dict.
    '''
    for key in stats:
        print('The word "{word}" is {num} times in the text.'.format(word=key, num=stats[key]))


def main():
    # check if there are filenames specified during script call
    if len(sys.argv) > 1:
        # if so, the script iterates over the indices of the arguments
        for i in range(len(sys.argv)):  # ==> take every indice from [0, 1]
            # ignore the scriptname as input
            if i != 0:
                statistic(sys.argv[i])
    else:
        # standard case if no filename is given as argument
        statistic()
    # print_stats()
    save_stats()

if __name__ == '__main__':
    main()

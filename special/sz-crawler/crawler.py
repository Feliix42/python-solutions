#!/usr/bin/env python3

from urllib.request import urlopen
import re
from itertools import chain
from model import *
import database


titleregex = re.compile(r'<title>(.+)\s*</title>', re.DOTALL)
# for absolute links
absolutere = re.compile(
    r'(https?://([\w\.-]*\.)?sz-online\.de)([/\w/-]*\.html)')
# for relative links
relativere = re.compile(r'href=\"(/[/\w/-]*\.html)\"')


def search():
    '''
    Crawls through the web sites of the SZ Online, gets every link and article
    and saves them as model for the database.
    '''

    # initialize the queue with the first webpage to visit.
    queue = [('http://www.sz-online.de', '')]
    # initialize an empty result dict
    results = {}

    # iterate over the queue until it's empty
    while len(queue) > 0:
        # pop the first web page from the queue
        target = queue.pop()
        # unpack the address
        # address format: ('http://www.domain.de', '/path/to/file.html')
        domain, path = target

        try:
            # open the webpage, get the contents
            page = urlopen(domain + path).read().decode('utf-8')

            # get the page title
            title = titleregex.search(page).group(1)
            # remove incorrect characters - just to be sure...
            title = title.replace('\n', '')
            title = title.replace('\t', '')

            # this is needed because we do not want to do a Carriage return
            title = title.replace('\r', '')
            # print(title)

            # add the page to the results
            results[target] = title

            # gather all available new targets, create an iterable of tuples
            targets1 = map(lambda a: a.group(1, 3), absolutere.finditer(page))
            # the domain of the SZ Online is being added, if it was addressed
            # relatively
            targets2 = map(lambda a: (domain, a.group(1)),
                           relativere.finditer(page))

            # chain chains two+ iterables to one iterable
            for l in chain(targets1, targets2):
                if l not in results:
                    # add all available pages to the results dict to avoid
                    # duplicates in the queue
                    results[l] = None
                    queue.append(l)
        except UnicodeDecodeError:
            # continue if script encounters a nasty unicode character
            continue

    # return a list of models for the database
    return [Pages(title=results[key], url=key[0] + key[1]) for key in results]


def main():
    resultlist = search()
    database.database(resultlist)
    database.listall()


if __name__ == '__main__':
    main()

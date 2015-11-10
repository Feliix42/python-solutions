# task 12

import time
# Step 2


def time_teller(function):
    def inner(a="%Y/%m/%d:%H:%M"):
        return "Now it is {date}".format(date=function(a))
    return inner


@time_teller
def get_time(timeformat):
    timestr = time.strftime(timeformat)
    return timestr


def main():
    print(get_time())
    print(get_time("%H:%M"))
    print(get_time("%H h and %M min"))

if __name__ == '__main__':
    main()

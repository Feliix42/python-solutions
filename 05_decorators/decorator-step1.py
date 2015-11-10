# task 12

import time
# Step 1


def time_teller(function):
    '''
    The time_teller function acts as an wrapper around
    the function (the parameter)
    '''
    def inner():
        strvalues = function()
        return "It is {date}. Since {hour} hours and {minutes} \
minutes.".format(date=strvalues[0], hour=strvalues[1], minutes=strvalues[2])
    return inner


@time_teller  # This is the decorator
def get_time():
    '''
    This function gets the time an put it into a list to return it.
    '''
    timestr = time.strftime("%Y/%m/%d:%H:%M")
    timelist = timestr.split(':')
    '''
    You also could have used the following to create the same list:

    timelist.append(time.strftime("%Y/%m/%d"))
    timelist.append(time.strftime("%H"))
    timelist.append(time.strftime("%M"))
    '''
    return timelist


def main():
    print(get_time())

if __name__ == '__main__':
    main()

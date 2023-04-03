import math

#---------------------------------------------------------------------------#
#-----------------------CHECK IF THE NUMBER IS PRIME------------------------#
#---------------------------------------------------------------------------#


def prime_check(x):

    for ele in range(3, (int(x**.5)+1), 2):
        if x % ele == 0:
            return False

    return True

#---------------------------------------------------------------------------#
#-----------------------FIND ALL PRIMES UP TO GIVEN NUMBER------------------#
#---------------------------------------------------------------------------#


def find_primes(lo, hi):

    result = []

    if lo % 2 == 0:
        new_low = lo + 1

        for ele in range(new_low, hi, 2):
            if prime_check(ele):
                result.append(ele)
    else:

        for ele in range(lo, hi, 2):
            if prime_check(ele):
                result.append(ele)

    return result

#---------------------------------------------------------------------------#
#-----------------------RESTART PROGRAM WITH NEW NUMBER---------------------#
#---------------------------------------------------------------------------#


def again():

    result = input('Exit or continue?')

#---------------------------------------------------------------------------#
#-----------------------DIFFERENCE OF ALL SUB PRIMES------------------------#
#---------------------------------------------------------------------------#


def prime_list_difference(theList):

    result = []

    for ele in range(len(theList)-1):
        result.append(theList[ele+1] - theList[ele])

    return result
#---------------------------------------------------------------------------#
#-----------------------TEMP FOR FINDING PATTERNS 1-------------------------#
#---------------------------------------------------------------------------#


def diff_index_list(theList):

    cond_list = []
    ele_list = []
    slist = list(set(theList))

    for ele in slist:
        cond = theList.index(ele)
        cond_list.append(cond)
        ele_list.append(ele)

    result_s = sorted(list(zip(ele_list, cond_list)))
    result = list(zip(ele_list, cond_list))

    return result, result_s


def split_diff_list(theList, ilist):

    result = []

    for element, index in ilist:
        # if index == 0:
        #   continue
        # else:
        result.append(theList[:index+1])
    '''
    print('LENGTH OF SPLITZ: ')
    print(len(result))
    '''
    return result


def myfunc(theList, setindex):

    result = [()]
    counter = 0

    for ele in setindex:
        for ele2 in theList:
            if ele in ele2:
                count = ele2.count(ele)
                result.append((ele, count))
                counter += 1

    return result

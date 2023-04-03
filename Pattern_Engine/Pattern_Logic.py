


from Generator_Engine.Generator_Logic import find_primes,myfunc,prime_list_difference,diff_index_list, split_diff_list, myfunc
   

#---------------------------------------------------------------------------#
#-----------------------FIND PYRAMATIC PRIME PATTERNS-----------------------#
#---------------------------------------------------------------------------#

def pyramatic_prime_structures(d_list,theList):

        length = range(len(d_list))

        apex_prime_list = []
        pyramatic_structure_count = 0
        base_of_apex_list = []

        for num in length:
            try:
                if d_list[num] == 2:
                    if d_list[num+1] == 4:
                        if d_list[num+2] == 2:
                            pyramatic_structure_count += 1
                            apex_prime_list.append((theList[num+1],theList[num+2]))
                            base_of_apex_list.append((theList[num],theList[num+3]))
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            except IndexError:
                break
        
        return(apex_prime_list,base_of_apex_list,pyramatic_structure_count)


#---------------------------------------------------------------------------#
#--------------------FIND INVERSE PYRAMATIC STRUCTURES----------------------#
#---------------------------------------------------------------------------#

def reverse_pyramatic_structures(d_list,theList):

    length = range(len(d_list))

    wing_prime_list = []
    inverse_pyramid_prime_count = 0
    inverse_base_prime_list = []

    for num in length:
        try:
            if d_list[num] == 4:
                if d_list[num+1] == 2:
                    if d_list[num+2] == 4:
                        inverse_pyramid_prime_count += 1
                        wing_prime_list.append((theList[num+1],theList[num+3]))
                        inverse_base_prime_list.append(theList[num+2])
                    else:
                        continue
                else:
                    continue
            else:
                continue
        except IndexError:
            break

    return(inverse_base_prime_list,wing_prime_list,inverse_pyramid_prime_count)


#---------------------------------------------------------------------------#
#--------------------FIND CONSECUTIVE DIFFERENTIALS-------------------------#
#---------------------------------------------------------------------------#

def consecutive_diff_generator(d_list,theList):

    length = range(len(d_list))

    duplicate_diff_prime_list = []
    ternary_diff_prime_list = []
    quaternary_diff_prime_list = []
    pentad_diff_prime_list = []

    duplicate_prime_list = []
    ternary_prime_list = []
    quaternary_prime_list = []
    pentad_prime_list = []

    duplicates = 0
    ternaries = 0
    quaternaries = 0
    pentads = 0
    

    for num in length:
        
    #Duplicates
        try:
            for num in range(len(d_list)):
                if d_list[num] == d_list[num+1]:
                    duplicate_diff_prime_list.append((d_list[num],d_list[num+1]))
                    duplicate_prime_list.append((theList[num],theList[num+1],theList[num+2]))
                    duplicates += 1

                else:
                    continue

                #Triplets
                if d_list[num+1] == d_list[num+2]:
                    ternary_diff_prime_list.append((d_list[num],d_list[num+1],d_list[num+2]))
                    ternary_prime_list.append((theList[num],theList[num+1],theList[num+2],theList[num+3]))
                    ternaries += 1

                else:
                    continue

                #Quaternaries
                if d_list[num+2] == d_list[num+3]:
                    quaternary_diff_prime_list.append((d_list[num],d_list[num+1],d_list[num+2],d_list[num+3]))
                    quaternary_prime_list.append((theList[num],theList[num+1],theList[num+2],theList[num+3],theList[num+4]))
                    quaternaries += 1

                else:
                    continue

                #Pentads
                if d_list[num+ 3] == d_list[num+4]:
                    pentad_diff_prime_list.append((d_list[num],d_list[num+1],d_list[num+2],d_list[num+3],d_list[num+4]))
                    pentad_prime_list.append((theList[num],theList[num+1],theList[num+2],theList[num+3],theList[num+4],theList[num+5]))
                    pentads += 1

                else:
                    continue

        except IndexError:
            break

    return(duplicate_diff_prime_list,duplicate_prime_list,duplicates,ternary_diff_prime_list,ternary_prime_list,ternaries,quaternary_diff_prime_list,quaternary_prime_list,quaternaries,pentad_diff_prime_list,pentad_prime_list,pentads)




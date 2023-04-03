

from Generator_Engine.Generator_Logic import find_primes, myfunc, prime_list_difference, diff_index_list, split_diff_list, myfunc
from Pattern_Engine.Pattern_Logic import pyramatic_prime_structures, reverse_pyramatic_structures, consecutive_diff_generator
from os import *
import subprocess
import sys


#number = int(input('What number do you want to process?'))
starting_number = int(input('Enter a number you want to begin with: '))
ending_number = int(input('Enter the number you want to end with: '))
go_list = find_primes(starting_number, ending_number)
diff_list = prime_list_difference(go_list)
diff_set_list = sorted(list(set(diff_list)))
unsorted_diff_index_list, sorted_diff_index_list = diff_index_list(diff_list)
index_count1 = split_diff_list(diff_list, sorted_diff_index_list)
index_count2 = myfunc(index_count1, diff_set_list)
#twinz,quadz = twin_quad_primes(diff_list)
apex_primes, base_of_apexes, pyramatic_structures = pyramatic_prime_structures(
    diff_list, go_list)
inverse_base_primes, inverse_wing_primes, reverse_pyramatic_prime_structures = reverse_pyramatic_structures(
    diff_list, go_list)

duplicate_diff_prime_list, duplicate_prime_list, duplicates, ternary_diff_prime_list, ternary_prime_list, ternaries, quaternary_diff_prime_list, quaternary_prime_list, quaternaries, pentad_diff_prime_list, pentad_prime_list, pentads = consecutive_diff_generator(
    diff_list, go_list)


print('List of all primes under your chosen number: \n')
print(go_list)

print('\nDifference between each prime: ')
print(diff_list)
print('\nSet list of differences: ')
print(diff_set_list)

print('\n')

print('\nOrganic index of each unique element in differential list.')
print('             (Unique Element, Index Position)               ')
print(unsorted_diff_index_list)
print('\nSorted index of each unique element in differential list.')
print('             (Unique Element, Index Position)               ')
print(sorted_diff_index_list)
print('\nNumber of differential occurences before higher differential introduced: ')
print(index_count2)

print('\n')

print('\nNumber of Pyramatic Prime Structures: ')
print(pyramatic_structures)
print('\nNumber of Inverse Pyramatic Prime Structures: ')
print(reverse_pyramatic_prime_structures)

print('\n')

print('\nApex Primes: ')
print(apex_primes)
print('\nApex Supporting Primes: ')
print(base_of_apexes)

print('\n')

print('\nInverse Base Primes: ')
print(inverse_base_primes)
print('\nInverse Wing Primes: ')
print(inverse_wing_primes)


print('\nAll primes with 2 consecutive differentials: ')
print('\nDuplicate Prime List: ')
print(duplicate_prime_list)
print('\nDuplicate Differential List: ')
print(duplicate_diff_prime_list)
print('\nTotal: ')
print(duplicates)

print('\n')

print('\nAll primes with 3 consecutive differentials: ')
print('\nTernary Prime List: ')
print(ternary_prime_list)
print('\nTernary Differential List: ')
print(ternary_diff_prime_list)
print('\nTotal: ')
print(ternaries)

print('\n')

print('\nAll primes with 4 consecutive differentials: ')
print('\nQuaternary Prime List: ')
print(quaternary_prime_list)
print('\nQuaternary Differential List: ')
print(quaternary_diff_prime_list)
print('\nTotal: ')
print(quaternaries)

print('\n')

print('\nAll primes with 5 consecutive differentials: ')
print('\nPentad Prime List: ')
print(pentad_prime_list)
print('\nPentad Differential List: ')
print(pentad_diff_prime_list)
print('\nTotal: ')
print(pentads)


terminate_prog = input('Type EXIT to terminate program')

if terminate_prog.lower().startswith('e'):
    print('Bye')


#print('\nNumber of Twin primes: ')
# print(twinz)
#print('\nNumber of quadratic primes: ')
# print(quadz)

import itertools
import numpy as   np
import pandas as pd




class Start_scan:
    def __init__(self):
        self.num_dig = int(input("please enter max number of digits (N) until which you want your search to be done"))
        if self.num_dig<= 5:
            raise Exception("You have entered no. less than 5, there is no famiy of 8 primes that exist for digits small than 5. Enter a valid number and rerun the program")
        self.rep_by = ['0','1','2','3','4','5','6','7','8','9']
        self.lowerLimit = 5     #
        self.prime_family_limit = 8
        ans =     input('press any key to start ')
        print("scanning")
        self.its_main()


    def gen_primes(another_obj, n):            # not using self here as first argument as we want to isolate objects of this function
        '''
       #         This code is an implementation of https://stackoverflow.com/a/33356284 (rwh_primes2 -fastest way of calculating prime numbers in python3 )
       #         : issues/bugs  solved  - extended range of n
       #              > earlier n> 6  >>> now n can be any whole number
       #
       #         :param n:   any whole number upto which prime numbers are to be searched
       #         :return:    function returns list of all prime numbers between 0 to n
       #         '''
        izip = itertools.zip_longest
        chain = itertools.chain.from_iterable
        compress = itertools.compress
        try:
            if n > 6:
                n = n + 1
            zero = bytearray([False])
            size = n // 3 + (n % 6 == 2)
            sieve = bytearray([True]) * size
            sieve[0] = False
            for i in range(int(n ** 0.5) // 3 + 1):
                if sieve[i]:
                    k = 3 * i + 1 | 1
                    start = (k * k + 4 * k - 2 * k * (i & 1)) // 3
                    sieve[(k * k) // 3::2 * k] = zero * ((size - (k * k) // 3 - 1) // (2 * k) + 1)
                    sieve[start::2 * k] = zero * ((size - start - 1) // (2 * k) + 1)

            if n == 2:
                another_obj.ans = [2]
            elif n == 3:
                another_obj.ans = [2, 3]
            elif n == 5:
                another_obj.ans = [2, 3, 5]
            else:
                another_obj.ans = [2, 3]

            poss = chain(izip(*[range(i, n, 6) for i in (1, 5)]))
            another_obj.ans.extend(compress(poss, sieve))
            return another_obj.ans
        except IndexError:                                                  # if n is 0 or 1 it gives out an empty list
            return []

    def check_prime(self , number):                                         #uses gen_primes for checking if a number is prime or not
            try:
                ind = list(self.cropped_arr).index(number)
            except ValueError:
                return False
            else:
                return True


    def scan_number(self, num_to_rep, digit_to_rep_with):
        temp_arr = [num_to_rep]
        count =1
        if len(num_to_rep) >self.lowerLimit:                                             # making sure that entered number is not less than 4 digit number
            for dig in self.rep_by:
                new_no = num_to_rep.replace(digit_to_rep_with,dig)
                if  new_no != num_to_rep and (not(int(new_no[-1])%2)) and (not(new_no[-1] == 0) ) :
                    # CONDITIONS CHECKED HERE
                      #IF LAST DIGIT OF NEW NUMBER IS 0,2,4,6,8
                      #IF replaced number is not equal to old number
                    if self.check_prime(int(new_no)):
                        temp_arr.append(new_no)
                        count +=1


            if count >= self.prime_family_limit:
                print('result found', temp_arr)
                return(temp_arr)

    def its_main(self):
        max_list = (10 ** self.num_dig) - 1
        all_primes = np.array(self.gen_primes(max_list))                                    # getting list of all prime numbers till given N
        self.cropped_arr = all_primes[all_primes >= (10 ** (self.lowerLimit -1))]           #using numpy vectorisation to crop numbers that have digits less than 4
        primes_sig = pd.DataFrame(self.cropped_arr, dtype=np.str)

        for each_element in primes_sig[0]:
            for dummy in [self.scan_number(each_element, x) for x in self.rep_by if each_element.count(x) >= 2 ]:

                if dummy:
                    exit(0)



new_search_obj = Start_scan()


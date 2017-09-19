#This program is based upon a basic python project provided by
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import time

def nice_day():
    print('Have a nice day outside!!!!!')
def good_day():
    print('Have a good day inside!!!!!')



def main():
    outside_answer = input('Do you want to go outside?')
    if(outside_answer != 'yes' and outside_answer != 'no'):
        print('You must answer either "yes" or "no"')
        #invalid operation
    else:
        if(outside_answer == 'yes'):
            raining_answer = input('Is it raining?')
            if (raining_answer != 'yes' and raining_answer != 'no'):
                print('You must answer either "yes" or "no"')
                # invalid operation
            else:
                if (raining_answer == 'no'):
                    nice_day()
                else:
                    umbrella_answer = input('Do you have an umbrella?')
                    if (umbrella_answer != 'yes' and umbrella_answer != 'no'):
                        print('You must answer either "yes" or "no"')
                        # invalid operation
                    elif(umbrella_answer == 'yes'):
                        nice_day()
                    else:
                        print('Wait a while! Maybe it will stop!')
                        time.sleep (10)
                        raining_answer = input('Is it still raining?')
                        if (outside_answer != 'yes' and outside_answer != 'no'):
                            print('You must answer either "yes" or "no"')
                        # invalid operation
                        if (raining_answer == 'no'):
                            nice_day()
                        else:
                            print('You may have to wait until tomorrow')






        else:
            good_day()

main()



'''
One day you decide to arrange all your cats in a giant circle.
Initially, none of your cats have any hats on.
You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
In The first round, you stop at every cat, placing a hat on each one.
In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.
Optional: Make a function that can calculate hats with any amount of rounds and cats.
Here you should write an algorithm, and after that, try to make pseudo code. Only after that start to work. The code is simple here, but you might struggle with the algorithm.
 Therefore don`t try to write a code from the first attempt. Don't forget to calculate the complexity of your algorithm.
'''

'''
Pseudo_code
start rounds 100 times
    start round
        for every cat check  if cat_number % round number == 0  
            if True change cat_in_hat status
            if False go to next cat
    finish round
    start next round till final

'''
rounds = 100
cats_list = []
cats = 100

def change_cat_in_hat_status(i: bool) -> bool:
#function get variable, check it and change bool value
#complexity O(1)
    if i:
        i = False
    else:
        i = True
    return i

def create_cats_list(cats_quantity: int):
#function get quantity of cats and create list of cat's in start state(no hat)
#complexity worst case O(n)
    for i in range(cats_quantity):
        cats_list.append(False)


def cats_conundrum(cats: int, rounds: int):
#function get cats qunatity and number of rounds 
#complexity O(n^2)
    create_cats_list(cats)
    for round in range(1, rounds+1):
        for cat_index, cat in enumerate(cats_list):
            if cat_index % round == 0:
                cats_list[cat_index] = change_cat_in_hat_status(cat)


def get_cat_state(number: int) -> bool:
#function get number of cat and return it's state
#complexity O(n)
    return cats_list[number]


def get_cats_in_hat() -> tuple:
#function return tuple of indexes of cats in hats
#complexity O(n)
    cats_in_hat = ()
    for cat_index, cat in enumerate(cats_list):
        if cat:
            cats_in_hat += (cat_index),
    return cats_in_hat

#Total complexity of all function O(n^2) + O(1) + O(n) +O(n) = O(n^2)
cats_conundrum(cats, 100)


check_cat = 2
print(f'Cat nuber {check_cat} in hat is: {get_cat_state(check_cat)}')

print('List of cats in hats after all rounds:',get_cats_in_hat())
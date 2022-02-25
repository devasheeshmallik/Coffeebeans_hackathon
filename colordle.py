"""import random

def check_color(c,g):
    count = 0
    pos =[]
    for i in c:
        for j in g:
            if i != j:
                g.remove(j)
    return g

if __name__ == "__main__":
    U = [ 'R', 'G', 'B', 'Y', 'W', 'V', 'O', 'P' ]
    n = int(input("n : "))
    c = random.choices(U,k = 4) 
    g = list(input("g : "))
    print("c ",c)
    while n > 0:
        if c == g:
            print("You Win!")
        else:
            g = check_color(c,g)

            fix_g(g,U)
        print()
        
        n-=1
    
    
    else:
        print("You loss!")
        """
import random
import itertools
colors = ( 'R', 'G', 'B', 'Y', 'W', 'V', 'O', 'P')

# ONE FUNCTION REQUIRED
def EvaluateCode(guess, secret_code):
    key = []
    for i in range(0, 4):
        for j in range(0, 4):
            if guess[i] == secret_code[j]:
                key += [i] if i == j else [j]    
    return key

# MAIN CODE
# choose secret code
secret_code = random.sample(colors, 4)
#print ('(shh - secret code is: ', secret_code, ')\n', sep='')
# create the full list of permutations
full_code_list = list(itertools.permutations(colors, 4))
n = int(input("n : "))
guess = list(input("g : "))
n=-1
while n> 0:
    n-=1
    key = EvaluateCode(guess, secret_code)
    # make a random guess
    guess = random.choice(full_code_list)
    print ('guess:', guess)
    # evaluate the guess and get the key
    
    #print ('key:', key)
    if key == ['B','B','B','B']:
        break
    # remove codes from the code list that don't match the key
    full_code_list2 = []
    for i in range(0, len(full_code_list)):
        if EvaluateCode(guess, full_code_list[i]) == key:
            full_code_list2 += [full_code_list[i]]
    full_code_list = full_code_list2
    #print ('N remaining: ', len(full_code_list), '\n', full_code_list, '\n', sep='')
print ('\nMATCHed')
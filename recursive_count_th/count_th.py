'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    main = len(word)
    sub = len('th')

    if(main == 0 or main < sub):
        return 0
    
    if(word[0 : sub] == 'th'):
        return count_th(word[sub - 1:]) + 1

    return count_th(word[sub - 1:])
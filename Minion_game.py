# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
string = input()
string_length = len(string)
vowels = "a,e,i,o,u"

player1 = 0
player2 = 0

for i in range(string_length):
    if string[i] in vowels:
        player1 += string_length - i
    else:
        player2 +=string_length - i

if player1 > player2:
    print("Kevin", player1)
elif player1 < player2:
    print("Stuart", player2)
else:
    print("Draw")  # Output Stuart 12 for 'banana'

# or with function:

def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")

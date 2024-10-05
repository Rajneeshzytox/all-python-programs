# String:  Count Vowel and Cosonent 

str1 = 'abcde  fgh i jklmn2  @@  %^&6575758 opq rstuvwxyz'

# ------------------- loop
def countVowelAndConsonent(s:str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel_in_str = []
    consonent_in_str = [] 
    
    for i in s:
        if not i.isalpha():
            continue
        elif(i in vowel):
            vowel_in_str.append(i)
        else:
            consonent_in_str.append(i)
    
    print(vowel_in_str)
    print(consonent_in_str)
    return len(vowel_in_str), len(consonent_in_str)

a,b = countVowelAndConsonent(str1)

print(f"there are {a} vowels and {b} consonents in\n{str1}")



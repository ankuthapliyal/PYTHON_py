# def average(a , b):
#     avrageval = a+b /2
#     print(avrageval)

# average(5,10)
# average(44,55)
# average(87 ,48)

# function with default argument

# def defargu(a = 10, b = 20):
#     average = (a + b) / 2
#     print(average)

# defargu()

# return statement
# def multiply(x):
#     return x**2

# print(multiply(4))


def countVowConso(userInput):
    vowels  = "aeiouAEIOU"

    countVowel = 0
    countConsonante = 0

    for eachchar in userInput:
        if(eachchar.isalpha()):
            if(eachchar in vowels):
                countVowel += 1
            else:
                countConsonante += 1

    return countVowel, countConsonante


vowels, consonants = countVowConso("anku thapliyal")
print("Nomber of vowels and consonants is : ",vowels, consonants)
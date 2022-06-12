from dataclasses import replace


def main():
    while True:


        word = str(input("Enter a word: ")).lower()
        anagram = str(input("Enter the Anagram: ")).lower()
            

        word = word.replace(" ", "")
        anagram = anagram.replace(" ", "")

        a = sorted(word)
        b = sorted(anagram)

        if a == b:
            print(True)
        else:
            print(False)
        again = input(" Would you like to check for another word? [Yes/No]").lower()
        if again != "yes":
            break
    print("Thanks for Using the Anagram Checker")

main()
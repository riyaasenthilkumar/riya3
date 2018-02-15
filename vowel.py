string=raw_input("Enter the string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='0' or i=='u'):
        print(i,"is a vowel")
    else:
        print(i,"is a constant")

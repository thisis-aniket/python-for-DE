# 2. Write a program to fill in a letter template given below with name and date.

letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''

new_letter = letter.replace("<|Name|>", "Aniket").replace("<|Date|>", "18 November")

print(new_letter)
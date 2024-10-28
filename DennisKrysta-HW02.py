# Krysta Dennis
# UWYO COSC 1010
# 28OCT2024
# HW 02
# Lab Section: 12
# Sources, people worked with, help given to: 
# your
# comments
# here

m_code = {
"A" : ".-" , "B":"-...", "C":"-.-.", "D":"-..", "E":".","F":"..-.","G":"--.",
"H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
"P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--",
"X":"-..-","Y":"-.--","Z":"--..", " ": " "}


user_input = input("Enter a phrase to be repeated back in morse code:")

def code_to_mores(input_string):
    new_code = ""
    for input in input_string.upper():
        new_code = new_code + " "+ m_code[input]
    return new_code
print(code_to_mores(user_input))
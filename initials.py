def get_initials(fullname):
    ##asignment for INITIALS
    
    name_list = fullname.split()
    initial_letter = ""
    for name in name_list:
        initial_letter = initial_letter + name[0]
    initial_letter=initial_letter.upper()
    answer="The initials of '{fullname}' are {initial_letter}"
    formated_answer=answer.format(fullname=fullname,initial_letter=initial_letter)
    return formated_answer
def main():
    #fullname = "Edga allen bruce last samba"
    fullname=input("What is your full name: ")
    print(get_initials(fullname))
    
if __name__ == '__main__':
    main()
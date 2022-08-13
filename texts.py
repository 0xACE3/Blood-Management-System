from colored.Fore import Fore
# main text to appear in the beginning
main_text = "\n" + f"{Fore.CYAN}+ {Fore.YELLOW} MAIN {Fore.CYAN} +{Fore.RESET}".center(120, "-") + "\n"

# menu text to choose options from
menu_text = f"""\n{Fore.GREEN}To Insert a new data, Input "1".

{Fore.WHITE}To Display all the stored data, Input "2".

{Fore.RED}To Delete from the current data, Input "3".

{Fore.LIGHT_CYAN}To Update the existing data, Input"4".{Fore.WHITE}

{Fore.LIGHT_RED}Enter 'q' to exit the program.{Fore.RESET}"""

# note for option 1
option_oneNote = f"""\n{Fore.LIGHT_RED}Note: The file must be in the same directory as this program. 
If the filename does not exist, a new file with the given name is created.\n"""

filename_text = f"\n{Fore.YELLOW}Enter the filename you want to append data to :{Fore.RESET} "

main_else_text = f"{Fore.RED}Sorry, wrong input! :)"

# texts for inputs
name_text = f"\n\n{Fore.WHITE}Enter full name: "
blood_type_text = f"{Fore.LIGHT_RED}Enter Blood Group: "
age_text = f"{Fore.LIGHT_MAGENTA}Enter age (between 18 and 60): "
gender_text = f"{Fore.LIGHT_YELLOW}Enter Gender: "
phoneNo_text = f"{Fore.LIGHT_GRAY}Enter phone number: "

# texts for except block
perm_error_text = f"\n{Fore.RED}Please close the file for new data to be appended!{Fore.RESET}"
assert_err_text = f"\n{Fore.RED}Oops! Something wrong with input!{Fore.RESET}"

# texts for wrong inputs
add_else_text = f"{Fore.LIGHT_RED}Sorry, I don't recognise the input! {Fore.YELLOW}:|{Fore.RESET}"

# texts for update data
row_text = f"{Fore.WHITE}Enter row number: "
fieldname_text = f"{Fore.CYAN}Enter the exact Field Name: "
replacement_text = f"{Fore.GREEN}Enter the text you want to replace with:{Fore.RESET} "

# delete_row text
value_text = f"{Fore.WHITE}Enter the value of the field name from the expected delete row:{Fore.RESET} "


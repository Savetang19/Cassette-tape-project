from stage import Stage
from turtle import Screen

st = Stage()
screen = Screen()
file_name = st.init_screen()

while True:
    st.print_all_menu(file_name)
    # Ask if the user wants to continue or not.
    con = screen.textinput("Do you want to continue or exit?",
                           "If exit enter 'e', If continue enter any key.")
    if con.lower() == "e":
        break

from stage import Stage

st = Stage()
st.init_screen()
while True:
    st.print_all_menu()
    # Ask if the user wants to continue or not.
    con = st.screen.textinput("Do you want to continue or exit?",
                              "If exit enter 'e', If continue enter any key.")
    if con.lower() == "e":
        break

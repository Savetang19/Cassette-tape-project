from cassette import CassetteTape
from data import CollectionData
from turtle import Turtle, Screen
import os


class Stage:
    def __init__(self):
        """ Initialize new stage for the program.
        """
        self.printer = Turtle()
        self.screen = Screen()

    def init_screen(self):
        """ Display welcome screen for the program.
        """
        p = self.printer
        sc = self.screen
        sc.title("Cassette tapes collection.")
        sc.screensize(600, 600)
        sc.bgcolor("#D3F3FF")
        sc.delay(100)
        p.penup()
        p.goto(0, 10)
        p.shape("circle")
        p.shapesize(0.1)
        p.write("Welcome to cassette tapes collection.", True, "Center",
                ("Consolas", 25, "normal"))

    def select_menu(self):
        """ This class is used for print all of the menus that the program can
        provide so that the user may select what they want to do and return it.

        :return: The menus that the user has selected.
        :rtype: str
        """
        tape = Turtle()  # Create new turtle as "tape" for print the picture.
        p = self.printer
        sc = self.screen
        sc.clear()
        sc.addshape("tape.gif")
        tape.shape("tape.gif")
        tape.penup()
        tape.goto(0, -100)
        # Print all menus, line by line.
        p.goto(-205, 210)
        p.write("Please select your choice.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 180)
        p.write("1. Inset new tape.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 150)
        p.write("2. Search tape from collection.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 120)
        p.write("3. Delete tape from collection.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 90)
        p.write("4. Show all cassette tapes in collection.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 60)
        p.write("5. Find song from cassette tapes.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 30)
        p.write("6. Show all song in cassette tape.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 0)
        p.write("7. Open cassette tape on youtube.", True, "left",
                ("Consolas", 18, "normal"))
        # Ask about the menus that the user would like to select.
        choice = sc.textinput("Select your choice", "1, 2, 3, 4, 5, 6 or 7")
        return choice

    def print_all_menu(self):
        """ This class is used to print all of the processes that the user has
        selected from the menus.
        """
        choice = self.select_menu()
        tape = Turtle()
        p = self.printer
        sc = self.screen
        sc.clear()
        sc.addshape("tape.gif")
        tape.shape("tape.gif")
        tape.penup()
        # Assign 'db' as the database for a collection.
        db = CollectionData("tape_collection")
        if choice == "1":
            # Ask user to input about the new cassette tape's information.
            tape_name = sc.textinput("Insert new tape",
                                     "Please input tape name: ")
            band = sc.textinput("Insert new tape", "Please input band: ")
            # Create new cassette tape as CassetteTape object.
            cassette_tape = CassetteTape(tape_name, band, db)
            price = sc.numinput("Insert new tape", "Please input price: ")
            side_a = sc.textinput("Insert new tape",
                                  "Please input song from side A: ex. "
                                  "song1,song2,song3 ")
            side_b = sc.textinput("Insert new tape",
                                  "Please input song from side B: ex. "
                                  "song1,song2,song3 ")
            url = sc.textinput("Insert new tape",
                               "Please input youtube url link(optional): "
                               "ex.https://www.youtube.com/watch?v=4RY3q8vyU4w")
            cassette_tape.price = price
            cassette_tape.sidea += side_a.lower().split(',')
            cassette_tape.sideb += side_b.lower().split(',')
            cassette_tape.url = url
            db.insert(cassette_tape)
            tape.goto(0, -40)
            p.goto(0, 80)
            p.write("Insert completed.", True, "Center",
                    ("Consolas", 20, "normal"))
        elif choice == "2":
            # Ask user for the name of the cassette tape they want to search.
            tape_name = sc.textinput("Search tape from collection",
                                     "Please input tape name: ")
            text = db.search(tape_name)
            tape.goto(0, -40)
            p.goto(0, 80)
            p.write(text, True, "Center", ("Consolas", 20, "normal"))
        elif choice == "3":
            # Ask user for the name of the cassette tape they want to search.
            tape_name = sc.textinput("Delete tape from collection",
                                     "Please input tape name: ")
            text = db.delete(tape_name)
            tape.goto(0, -40)
            p.goto(0, 80)
            p.write(text, True, "Center", ("Consolas", 20, "normal"))
        elif choice == "4":
            # Show all the name of the cassette tapes in collection.
            all_tape = db.all_tape()
            if type(all_tape) == list:
                tape.goto(-180, 0)
                p.goto(0, 225)
                p.write(f"All cassette tapes: ", True, "left",
                        ("Consolas", 20, "normal"))
                y = 200  # Assign 'y' as y coordinates for print out the results.
                for num in range(len(all_tape)):
                    p.goto(20, y)
                    p.write(f"{num + 1}. {all_tape[num]}", True, "left",
                            ("Consolas", 18, "normal"))
                    y -= 25
            else:
                tape.goto(0, -40)
                p.goto(0, 80)
                p.write(f"{all_tape}", True, "center",
                        ("Consolas", 20, "normal"))
        elif choice == "5":
            # Ask user to input name of the song they want to search.
            song_name = sc.textinput("Find song from cassette tapes.",
                                     "Please input song name: ")
            text = db.search_song(song_name)
            tape.goto(0, -80)
            p.goto(0, 40)
            p.write(f"song name: {song_name}\n{text}", True, "Center",
                    ("Consolas", 20, "normal"))
        elif choice == "6":
            # Ask user for the name of the cassette tape they want to know.
            tape_name = sc.textinput("Show all song in cassette tape.",
                                     "Please input tape name: ")
            result = db.all_song_in_tape(tape_name)
            # Check if 'result' is list, print all the song name line by line.
            if type(result) == list:
                tape.goto(0, -150)
                y_a = 200
                y_b = 200
                p.goto(-275, 225)
                p.write("Side A: ", True, "left", ("Consolas", 20, "normal"))
                p.goto(5, 225)
                p.write("Side B: ", True, "left", ("Consolas", 20, "normal"))
                for song in result[0]:
                    p.goto(-265, y_a)
                    p.write(f"{song}".capitalize(), True, "left",
                            ("Consolas", 18, "normal"))
                    y_a -= 25
                for song in result[1]:
                    p.goto(25, y_b)
                    p.write(f"{song}".capitalize(), True, "left",
                            ("Consolas", 18, "normal"))
                    y_b -= 25
            # If 'result' is a string just print it out for the user.
            else:
                tape.goto(0, -80)
                p.goto(0, 40)
                p.write(f"{result}", True, "center",
                        ("Consolas", 18, "normal"))
        elif choice == "7":
            # Ask user for the name of the cassette tape they want to open.
            tape_name = sc.textinput("Search tape from collection",
                                     "Please input tape name: ")
            url = db.url_open(tape_name)
            # Check if the 'url' is the link for open or not.
            if url == "":
                tape.goto(0, -80)
                p.goto(0, 40)
                p.write("There is no link for this cassette tape", True,
                        "center", ("Consolas", 18, "normal"))
            # If 'url' is a string that got from except error, print this line.
            elif url.startswith("No"):
                tape.goto(0, -80)
                p.goto(0, 40)
                p.write(f"{url}", True, "center", ("Consolas", 18, "normal"))
            else:
                os.system(f"open \"\" {url}")  # Open youtube via url.

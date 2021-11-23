from cassette import CassetteTape
from data import CollectionData
from turtle import Turtle, Screen


class Stage:
    def __init__(self):
        self.printer = Turtle()
        self.screen = Screen()

    def init_screen(self):
        p = self.printer
        sc = self.screen
        sc.title("Cassette tapes collection.")
        sc.screensize(600, 600)
        sc.delay(100)
        p.penup()
        p.goto(0, 10)
        p.shape("circle")
        p.shapesize(0.1)
        p.write("Welcome to cassette tapes collection.", True, "Center",
                ("Consolas", 20, "normal"))

    def print_all_menu(self):
        tape = Turtle()
        p = self.printer
        sc = self.screen
        sc.clear()
        sc.register_shape("tape.gif")
        tape.shape("tape.gif")
        tape.penup()
        tape.goto(0, -100)
        p.goto(-205, 175)
        p.write("Please select your choice.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 150)
        p.write("1. Inset new tape.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 125)
        p.write("2. Search tape from collection.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 100)
        p.write("3. Delete tape from collection.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 75)
        p.write("4. Show all cassette tapes in collection.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 50)
        p.write("5. Find song from cassette tapes.", True, "left",
                ("Consolas", 18, "normal"))
        p.goto(-190, 25)
        p.write("6. Show all song in cassette tape.", True, "left",
                ("Consolas", 18, "normal"))
        choice = sc.textinput("Select your choice", "1, 2, 3, 4, 5 or 6")
        return choice

    def select_menu(self):
        choice = self.print_all_menu()
        tape = Turtle()
        p = self.printer
        sc = self.screen
        sc.clear()
        sc.register_shape("tape.gif")
        tape.shape("tape.gif")
        tape.penup()
        db = CollectionData("tape_collection")
        if choice == "1":
            tape_name = sc.textinput("Insert new tape",
                                     "Please input tape name: ")
            band = sc.textinput("Insert new tape", "Please input band: ")
            cassette_tape = CassetteTape(tape_name, band, db)
            price = sc.numinput("Insert new tape", "Please input price: ")
            side_a = sc.textinput("Insert new tape",
                                  "Please input song from side A: ex. song1,song2,song3 ")
            side_b = sc.textinput("Insert new tape",
                                  "Please input song from side B: ex. song1,song2,song3 ")
            cassette_tape.price = price
            cassette_tape.sidea += side_a.lower().split(',')
            cassette_tape.sideb += side_b.lower().split(',')
            db.insert(cassette_tape)
            tape.goto(0, -40)
            p.goto(0, 80)
            p.write("Insert completed.", True, "Center",
                    ("Consolas", 20, "normal"))
        elif choice == "2":
            tape_name = sc.textinput("Search tape from collection",
                                     "Please input tape name: ")
            text = db.search(tape_name)
            tape.goto(0, -40)
            p.goto(0, 80)
            p.write(text, True, "Center", ("Consolas", 20, "normal"))
        elif choice == "3":
            tape_name = sc.textinput("Delete tape from collection",
                                     "Please input tape name: ")
            text = db.delete(tape_name)
            tape.goto(0, -40)
            p.goto(0, 80)
            p.write(text, True, "Center", ("Consolas", 20, "normal"))
        elif choice == "4":
            tape.goto(-180, 0)
            p.goto(0, 225)
            p.write(f"All cassette tapes: ", True, "left",
                    ("Consolas", 20, "normal"))
            y = 200
            all_tape = db.all_tape()
            for num in range(len(all_tape)):
                p.goto(20, y)
                p.write(f"{num + 1}. {all_tape[num]}", True, "left",
                        ("Consolas", 18, "normal"))
                y -= 25
        elif choice == "5":
            song_name = sc.textinput("Find song from cassette tapes.",
                                     "Please input song name: ")
            text = db.search_song(song_name)
            tape.goto(0, -80)
            p.goto(0, 40)
            p.write(f"song name: {song_name}\n{text}", True, "Center",
                    ("Consolas", 20, "normal"))
        elif choice == "6":
            tape_name = sc.textinput("Show all song in cassette tape.",
                                     "Please input tape name: ")
            result = db.all_song_in_tape(tape_name)
            if type(result) == list:
                tape.goto(0, -150)
                y_A = 200
                y_B = 200
                p.goto(-275, 225)
                p.write("Side A: ", True, "left", ("Consolas", 20, "normal"))
                p.goto(5, 225)
                p.write("Side B: ", True, "left", ("Consolas", 20, "normal"))
                for song_a in result[0]:
                    p.goto(-265, y_A)
                    p.write(f"{song_a}", True, "left",
                            ("Consolas", 18, "normal"))
                    y_A -= 25
                for song_b in result[1]:
                    p.goto(25, y_B)
                    p.write(f"{song_b}", True, "left",
                            ("Consolas", 18, "normal"))
                    y_B -= 25
            else:
                tape.goto(0, -80)
                p.goto(0, 40)
                p.write(f"{result}", True, "center",
                        ("Consolas", 18, "normal"))

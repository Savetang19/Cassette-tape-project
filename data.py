import json


class CollectionData:
    """ This class used to read and write a file as a json file in order to
    access data from cassette tapes in collection.

    Attributes
    ----------
    name : str
        Name of the collection's file.

    Methods
    -------
    insert(cassette_tape: CassetteTape):
        Insert new cassette tape data to the database.
    search(tape_name: str):
        Search and return data of cassette tape.
    delete(tape_name: str):
        Delete cassette tape data from the database.
    all_tape():
        Return names of all cassette tapes from the database.
    search_song(song_name: str):
        Search and return data of song.
    all_song_in_tape(tape_name: str):
        Find and return all song from the cassette tape.
    url_open(tape_name: str):
        Find and return youtube link of the cassette tape.
    """

    def __init__(self, name):
        """ Initialize new database for the program.

        :param name: name of the collection's file.
        :type name: str
        """
        self.name = name

    def __repr__(self):
        """ Create a string representation of the database.

        :return: A string representation.
        :rtype: str
        """
        return f"CollectionData(name={self.name})"

    def insert(self, cassette_tape):
        """ Insert new cassette tape data to the database by using
        'cassette_tape' as '.json' file.

        :param cassette_tape: New cassette tape to insert.
        :type cassette_tape: CassetteTape
        """
        new_tape = {
            cassette_tape.name: {
                "band": cassette_tape.band,
                "side_A": cassette_tape.sidea,
                "side_B": cassette_tape.sideb,
                "price": cassette_tape.price,
                "link": cassette_tape.url
            }
        }
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
        except FileNotFoundError:
            with open(f"{self.name}.json", "w") as data_file:
                json.dump(new_tape, data_file, indent=4)
        else:
            collection.update(new_tape)
            with open(f"{self.name}.json", "w") as data_file:
                json.dump(collection, data_file, indent=4)

    def search(self, tape_name):
        """ Search and return data of cassette tape by using tape_name.

        :param tape_name: Name of the cassette tape.
        :type tape_name: str
        :return: The result of the data search.
        :rtype: str
        """
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            return f"Name: {tape_name}\nBand: {collection[tape_name]['band']}" \
                   f"\nprice: {collection[tape_name]['price']} Baht."
        except KeyError:
            return f"No cassette tape name: {tape_name} in collection."
        except FileNotFoundError:
            return "No collection data."

    def delete(self, tape_name):
        """ Delete cassette tape data from the database by using tape_name.

        :param tape_name: Name of the cassette tape.
        :type tape_name: str
        :return: The result of the data delete.
        :rtype: str
        """
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            del collection[tape_name]
            with open(f"{self.name}.json", "w") as data_file:
                json.dump(collection, data_file, indent=4)
            return "Delete completed."
        except KeyError:
            return f"No cassette tape name: {tape_name} in collection."
        except FileNotFoundError:
            return "No collection data."

    def all_tape(self):
        """ Return names of all cassette tapes from the database.

        :return: All tapes name or string if no collection data.
        :rtype: list or str
        """
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            all_name = [name for name in collection.keys()]
            return all_name
        except FileNotFoundError:
            return "No collection data."

    def search_song(self, song_name):
        """ Search and return data of song by using song_name.

        :param song_name: Name of the song.
        :type song_name: str
        :return: The result of the data search.
        :rtype: str
        """
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            tape_name = "not in any cassette tape"
            for tape in collection:
                if song_name.lower() in collection[tape]["side_A"]:
                    tape_name = f"tape name: {tape} on side A"
                elif song_name.lower() in collection[tape]["side_B"]:
                    tape_name = f"tape name: {tape} on side B"
            return tape_name
        except FileNotFoundError:
            return "No collection data."

    def all_song_in_tape(self, tape_name):
        """ Find and return all song from the cassette tape by using tape_name.

        :param tape_name: Name of the cassette tape.
        :type tape_name: str
        :return: All song from cassette tape or string if no collection data.
        :rtype: list or str
        """
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            song = []
            song += [[song_a for song_a in collection[tape_name]["side_A"]]]
            song += [[song_b for song_b in collection[tape_name]["side_B"]]]
            return song
        except KeyError:
            return f"No cassette tape name: {tape_name} in collection."
        except FileNotFoundError:
            return "No collection data."

    def url_open(self, tape_name):
        """ Find and return youtube link of the cassette tape by using
        tape_name.

        :param tape_name: Name of the cassette tape.
        :type tape_name: str
        :return: Result from find the url.
        :rtype: str
        """
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            return collection[tape_name]["link"]
        except KeyError:
            return f"No cassette tape name: {tape_name} in collection."
        except FileNotFoundError:
            return "No collection data."

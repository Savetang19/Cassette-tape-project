import json


class CollectionData:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"CollectionData(name={self.name})"

    def insert(self, cassette_tape):
        new_tape = {
            cassette_tape.name: {
                "band": cassette_tape.band,
                "side_A": cassette_tape.sidea,
                "side_B": cassette_tape.sideb,
                "price": cassette_tape.price
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
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            return f"Name: {tape_name}\nBand: {collection[tape_name]['band']}" \
                   f"\nprice: {collection[tape_name]['price']} Baht."
        except KeyError:
            return f"No cassette tape name: {tape_name} in collection."
        except FileNotFoundError:
            return "No collection's data."

    def delete(self, tape_name):
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
            return "No collection's data."

    def all_tape(self):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            all_name = [name for name in collection.keys()]
            return all_name
        except FileNotFoundError:
            return "No collection's data."

    def search_song(self, song_name):
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
            return "No collection's data."

    def all_song_in_tape(self, tape_name):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                collection = json.load(data_file)
            all_song = []
            all_song += [
                [song_a for song_a in collection[tape_name]["side_A"]]]
            all_song += [
                [song_b for song_b in collection[tape_name]["side_B"]]]
            return all_song
        except KeyError:
            return f"No cassette tape name: {tape_name} in collection."
        except FileNotFoundError:
            return "No collection's data."

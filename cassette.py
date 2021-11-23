from data import CollectionData


class CassetteTape:
    def __init__(self, name, band, db):
        self.name = name
        self.band = band
        self.db = db
        self.sidea = []
        self.sideb = []
        self.price = 0
        db.insert(self)

    def __repr__(self):
        return f'Cassette tape Name: "{self.name}"\nBand: "{self.band}"\n' \
               f'price: {self.price} Baht'

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.name = name

    @property
    def band(self):
        return self.band

    @band.setter
    def band(self, band):
        if not isinstance(band, str):
            raise TypeError("Band must be a string.")
        self.band = band

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            TypeError("Price must be a string.")
        if price < 0:
            raise ValueError("Price must greater or equal to zero.")
        self.price = price

    @property
    def db(self):
        return self.db

    @db.setter
    def db(self, db):
        if not isinstance(db, CollectionData):
            raise TypeError("bd must be a CollectionData object.")
        self.db = db

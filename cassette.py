from data import CollectionData


class CassetteTape:
    """ This class used to initialize new cassette tape.

    Attributes
    ----------
    name: str
        Name of the cassette tape.
    band: str
        Band's name of the cassette tape.
    db: CollectionData
        The database of the cassette tape collection.
    """

    def __init__(self, name, band, db):
        """ Initialize new cassette tape.

        :param name: Name of the cassette tape.
        :type name: str
        :param band: Band's name of the cassette tape.
        :type band: str
        :param db: The database of the cassette tape collection.
        :type db: CollectionData
        """
        self.name = name
        self.band = band
        self.db = db
        self.sidea = []
        self.sideb = []
        self.price = 0
        self.url = ""
        db.insert(self)

    def __repr__(self):
        """ Create a string representation of the cassette tape.

        :return: A string representation.
        :rtype: str
        """
        return f'Cassette tape Name: "{self.name}"\nBand: "{self.band}"\n' \
               f'price: {self.price} Baht'

    @property
    def name(self):
        """ Get or set the name of the cassette tape."""
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.__name = name

    @property
    def band(self):
        """ Get or set the band's name of the cassette tape."""
        return self.__band

    @band.setter
    def band(self, band):
        if not isinstance(band, str):
            raise TypeError("Band must be a string.")
        self.__band = band

    @property
    def price(self):
        """ Get or set the price of the cassette tape."""
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            TypeError("Price must be a number.")
        if price < 0:
            raise ValueError("Price must greater or equal to zero.")
        self.__price = price

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        if not isinstance(url, str):
            raise TypeError("Url link must be a string.")
        self.__url = url

    @property
    def db(self):
        """ Get or set the database for the cassette tape collection."""
        return self.__db

    @db.setter
    def db(self, db):
        if not isinstance(db, CollectionData):
            raise TypeError("bd must be a CollectionData object.")
        self.__db = db

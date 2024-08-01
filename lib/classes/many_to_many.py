class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise Exception("Hometown must be a non-empty string")
        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return self._concerts

    def venues(self):
        venues = set(concert.venue for concert in self._concerts)
        return list(venues)

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise Exception("Venue must be a Venue instance")
        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Date must be a non-empty string")
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        venue._concerts.append(concert)
        return concert

    def all_introductions(self):
        introductions = [concert.introduction() for concert in self._concerts]
        return introductions


class Concert:
    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Date must be a non-empty string")
        if not isinstance(band, Band):
            raise Exception("Band must be a Band instance")
        if not isinstance(venue, Venue):
            raise Exception("Venue must be a Venue instance")
        self._date = date
        self._band = band
        self._venue = venue

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Date must be a non-empty string")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise Exception("Band must be a Band instance")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise Exception("Venue must be a Venue instance")
        self._venue = value

    def hometown_show(self):
        return self._band.hometown == self._venue.city

    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"


class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        if not isinstance(city, str) or len(city) == 0:
            raise Exception("City must be a non-empty string")
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("City must be a non-empty string")
        self._city = value

    def concerts(self):
        return self._concerts

    def bands(self):
        bands = set(concert.band for concert in self._concerts)
        return list(bands)

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
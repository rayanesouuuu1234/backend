from __init__ import db

# Define the "Travel" model
class Travel(db.Model):
    # Define the table name in the database
    __tablename__ = "Travel"

    # This defines all of the attributes
    id = db.Column(db.Integer, primary_key=True)  
    destination = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)
    time_zone = db.Column(db.String, nullable=False)
    weather = db.Column(db.String, nullable=False)
    travel_type = db.Column(db.String, nullable=False)  # New attribute for type of travel

    # Constructor to initialize a new travel destination object
    def __init__(self, destination, language, time_zone, weather, travel_type):
        self.destination = destination  # Initialize destination
        self.language = language  # Initialize language
        self.time_zone = time_zone  # Initialize time_zone
        self.weather = weather  # Initialize weather
        self.travel_type = travel_type  # Initialize type of travel

    def to_dict(self):
        return {"destination": self.destination, "language": self.language, "time_zone": self.time_zone, "weather": self.weather, "travel_type": self.travel_type}
    
    # Create method to let users add a travel destination to the DB
    def create(self):
        try:
            db.session.add(self)  # add prepares to persist object to table
            db.session.commit()  # SQLAlchemy requires a manual commit to get it working
            return self
        except: 
            db.session.remove() # remove object from table if invalid
            return None

    # Method to return travel destination details for API response
    def read(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "language": self.language,
            "time_zone": self.time_zone,
            "weather": self.weather,
            "travel_type": self.travel_type
        }

def initDestinations(): # This initializes the database with travel destinations and their attributes
    destinations = [
        ("New York City", "English", "Eastern Time Zone", "Humid subtropical climate", "City"),
        ("Tokyo", "Japanese", "Japan Standard Time", "Humid subtropical climate", "City"),
        ("London", "English", "Greenwich Mean Time", "Temperate maritime climate", "City"),
        ("Hong Kong", "Chinese", "Hong Kong Time", "Humid subtropical climate", "City"),
        ("Istanbul", "Turkish", "Turkey Time", "Mediterranean climate", "City"),
        ("Yellowstone National Park", "English", "Mountain Time Zone", "Cold semi-arid climate", "National Park"),
        ("Grand Canyon National Park", "English", "Mountain Time Zone", "Cold semi-arid climate", "National Park"),
        ("Yosemite National Park", "English", "Pacific Time Zone", "Mediterranean climate", "National Park"),
        ("Banff", "English", "Mountain Time Zone", "Subarctic climate", "National Park"),
        ("Kruger National Park", "English", "South Africa Standard Time", "Subtropical climate", "National Park"),
        ("Rio de Janeiro", "Portuguese", "Brasília Time", "Tropical savanna climate", "Tropical"),
        ("Bora Bora", "French", "Tahiti Time", "Tropical rainforest climate", "Tropical"),
        ("Bali", "Indonesian", "Central Indonesia Time", "Tropical monsoon climate", "Tropical"),
        ("Cancun", "Spanish", "Eastern Standard Time", "Tropical wet and dry climate", "Tropical"),
        ("Maui", "English", "Hawaii-Aleutian Time Zone", "Tropical rainforest climate", "Tropical")
    ]

    for destination_info in destinations:
        destination = Travel(*destination_info)
        db.session.add(destination)

    db.session.commit()

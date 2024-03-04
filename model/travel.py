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

    # Constructor to initialize a new travel destination object
    def __init__(self, destination, language, time_zone, weather):
        self.destination = destination  # Initialize destination
        self.language = language  # Initialize language
        self.time_zone = time_zone  # Initialize time_zone
        self.weather = weather  # Initialize weather

    def to_dict(self):
        return {"destination": self.destination, "language": self.language, "time_zone": self.time_zone, "weather": self.weather}
    
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
            "weather": self.weather
        }

def initDestinations(): # This initializes the database with travel destinations and their attributes
    NewYorkCity = Travel(destination="New York City", language="English", time_zone="Eastern Time Zone", weather="Humid subtropical climate")
    Tokyo = Travel(destination="Tokyo", language="Japanese", time_zone="Japan Standard Time", weather="Humid subtropical climate")
    London = Travel(destination="London", language="English", time_zone="Greenwich Mean Time", weather="Temperate maritime climate")
    HongKong = Travel(destination="Hong Kong", language="Chinese", time_zone="Hong Kong Time", weather="Humid subtropical climate")
    Istanbul = Travel(destination="Istanbul", language="Turkish", time_zone="Turkey Time", weather="Mediterranean climate")
    Yellowstone = Travel(destination="Yellowstone National Park", language="English", time_zone="Mountain Time Zone", weather="Cold semi-arid climate")
    GrandCanyon = Travel(destination="Grand Canyon National Park", language="English", time_zone="Mountain Time Zone", weather="Cold semi-arid climate")
    Yosemite = Travel(destination="Yosemite National Park", language="English", time_zone="Pacific Time Zone", weather="Mediterranean climate")
    Banff = Travel(destination="Banff", language="English", time_zone="Mountain Time Zone", weather="Subarctic climate")
    Kruger = Travel(destination="Kruger National Park", language="English", time_zone="South Africa Standard Time", weather="Subtropical climate")
    RioDeJaneiro = Travel(destination="Rio de Janeiro", language="Portuguese", time_zone="Brasília Time", weather="Tropical savanna climate")
    BoraBora = Travel(destination="Bora Bora", language="French", time_zone="Tahiti Time", weather="Tropical rainforest climate")
    Bali = Travel(destination="Bali", language="Indonesian", time_zone="Central Indonesia Time", weather="Tropical monsoon climate")
    Cancun = Travel(destination="Cancun", language="Spanish", time_zone="Eastern Standard Time", weather="Tropical wet and dry climate")
    Maui = Travel(destination="Maui", language="English", time_zone="Hawaii-Aleutian Time Zone", weather="Tropical rainforest climate")

    # Add the travel destinations to the session
    db.session.add_all([NewYorkCity, Tokyo, London, HongKong, Istanbul, Yellowstone, GrandCanyon, Yosemite, Banff, Kruger, RioDeJaneiro, BoraBora, Bali, Cancun, Maui])
    db.session.commit()

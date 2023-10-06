from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
# for artist in artists:
#     print(artist)

# Find function prints corresponding artist
# print(artist_repository.find(1))

# Albums
album_repository = AlbumRepository(connection)
# all albums
# for album in album_repository.all():
#     print(album)
# find album
# print(album_repository.find(1))


class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        # "Runs" the terminal application.
        # It might:
        #   * Ask the user to enter some input
        #   * Make some decisions based on that input
        #   * Query the database
        #   * Display some output
        # We're going to print out the artists!
        
        print("Welcome to the music library manager!")
        print("What would you like to do?")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("")
            print("Here is the list of albums:")
            for album in album_repository.all():
                print(f"{album.id}: {album.title} {album.release_year}")
        elif choice =="2":
            print("")
            print("Here is the list of albums:")
            for artist in artists:
                print(f"{artist.id}: {artist.name} {artist.genre}")
        else:
                print("Invalid choice. Please enter 1 or 2")


    # artist_repository = ArtistRepository(self._connection)
    # artists = artist_repository.all()


if __name__ == '__main__':
    app = Application()
    app.run()
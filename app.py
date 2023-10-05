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
for artist in artists:
    print(artist)

# Find function prints corresponding artist
print(artist_repository.find(1))

# Albums
album_repository = AlbumRepository(connection)
# all albums
for album in album_repository.all():
    print(album)
# find album
print(album_repository.find(1))
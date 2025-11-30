from pymongo import MongoClient

# ---------------------------------------------
# CONNECT TO MONGODB
# ---------------------------------------------
def connect_db():
    # client = MongoClient("mongodb://localhost:27017/")
    client = MongoClient("mongodb+srv://learnriteshdhekane_db_user:Ritesh884@temp-python.1gpstub.mongodb.net/?appName=temp-python")
    db = client["MovieDB"]
    return db

# ---------------------------------------------
# CREATE COLLECTION & INSERT MOVIES
# ---------------------------------------------
def insert_movies(collection):
    n = int(input("Enter number of movies to insert: "))
    movie_list = []

    for i in range(n):
        print(f"\n--- Enter details for Movie {i+1} ---")
        title = input("Movie Title: ")
        writer = input("Writer: ")
        year = int(input("Release Year: "))
        director = input("Director: ")
        actors = input("Actors (comma separated): ").split(",")

        movie_list.append({
            "title": title,
            "writer": writer,
            "year": year,
            "director": director,
            "actors": [a.strip() for a in actors]
        })

    collection.insert_many(movie_list)
    print("\nMovies inserted successfully!")

# ---------------------------------------------
# a) GET ALL DOCUMENTS
# ---------------------------------------------
def get_all(collection):
    print("\n--- All Movies ---")
    for doc in collection.find():
        print(doc)

# ---------------------------------------------
# b) MOVIES DIRECTED BY “Raj Kapoor”
# ---------------------------------------------
def get_by_director(collection):
    print("\n--- Movies directed by Raj Kapoor ---")
    for doc in collection.find({"director": "Raj Kapoor"}):
        print(doc)

# ---------------------------------------------
# c) MOVIES WHERE ACTORS INCLUDE "Amitabh Bachchan"
# ---------------------------------------------
def get_by_actor(collection):
    print("\n--- Movies with actor Amitabh Bachchan ---")
    for doc in collection.find({"actors": "Amitabh Bachchan"}):
        print(doc)

# ---------------------------------------------
# d) MOVIES RELEASED IN THE 90s (1990–1999)
# ---------------------------------------------
def get_movies_90s(collection):
    print("\n--- Movies released in the 90s ---")
    for doc in collection.find({"year": {"$gte": 1990, "$lte": 1999}}):
        print(doc)

# ---------------------------------------------
# e) MOVIES RELEASED BEFORE 2000 OR AFTER 2010
# ---------------------------------------------
def get_before2000_after2010(collection):
    print("\n--- Movies released before 2000 OR after 2010 ---")
    for doc in collection.find({"$or": [{"year": {"$lt": 2000}}, {"year": {"$gt": 2010}}]}):
        print(doc)

# ---------------------------------------------
# f) UPDATE DOCUMENTS WITH EXTRA FIELDS
# ---------------------------------------------
def update_add_fields(collection):
    title = input("Enter movie title to update: ")
    new_rating = float(input("Enter rating to add: "))
    new_genre = input("Enter genre to add: ")

    result = collection.update_one(
        {"title": title},
        {"$set": {"rating": new_rating, "genre": new_genre}}
    )

    print(f"{result.modified_count} movie updated successfully!")

# ---------------------------------------------
# g) DELETE MOVIE
# ---------------------------------------------
def delete_movie(collection):
    title = input("Enter movie title to delete: ")

    result = collection.delete_one({"title": title})
    if result.deleted_count > 0:
        print("Movie deleted successfully!")
    else:
        print("Movie not found!")

# ---------------------------------------------
# MAIN PROGRAM MENU
# ---------------------------------------------
def main():
    db = connect_db()
    movies = db["movies"]

    while True:
        print("\n=========== MOVIE MENU ===========")
        print("1. Insert Movies")
        print("2. Get All Movies")
        print("3. Movies by Director 'Raj Kapoor'")
        print("4. Movies with Actor 'Amitabh Bachchan'")
        print("5. Movies Released in the 90s")
        print("6. Movies before 2000 or after 2010")
        print("7. Update Movie (Add Fields)")
        print("8. Delete Movie")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_movies(movies)
        elif choice == "2":
            get_all(movies)
        elif choice == "3":
            get_by_director(movies)
        elif choice == "4":
            get_by_actor(movies)
        elif choice == "5":
            get_movies_90s(movies)
        elif choice == "6":
            get_before2000_after2010(movies)
        elif choice == "7":
            update_add_fields(movies)
        elif choice == "8":
            delete_movie(movies)
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
main()

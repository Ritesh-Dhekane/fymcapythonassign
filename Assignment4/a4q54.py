from pymongo import MongoClient

# ---------------------------------------------
# CONNECT TO MONGODB
# ---------------------------------------------
def connect_db():
    # client = MongoClient("mongodb://localhost:27017/")
    client = MongoClient("mongodb+srv://learnriteshdhekane_db_user:Ritesh884@temp-python.1gpstub.mongodb.net/?appName=temp-python")
    db = client["RestaurantDB"]
    return db

# ---------------------------------------------
# CREATE COLLECTION & INSERT DOCUMENTS
# ---------------------------------------------
def create_and_insert(restaurants):
    data = []

    n = int(input("Enter number of restaurants to insert: "))
    for i in range(n):
        print(f"\n--- Enter details of Restaurant {i+1} ---")
        rest_id = input("Restaurant ID: ")
        name = input("Name: ")
        year = int(input("Establishment Year: "))
        cuisine = input("Cuisine: ")
        score = int(input("Score: "))

        data.append({
            "restaurant_id": rest_id,
            "name": name,
            "establishment_year": year,
            "cuisine": cuisine,
            "score": score
        })

    restaurants.insert_many(data)
    print("\nInserted Successfully!")

# ---------------------------------------------
# a) DISPLAY ALL DOCUMENTS
# ---------------------------------------------
def display_all(restaurants):
    print("\n--- All Restaurants ---")
    for doc in restaurants.find():
        print(doc)

# ---------------------------------------------
# b) DISPLAY SELECTED FIELDS
# ---------------------------------------------
def display_selected_fields(restaurants):
    print("\n--- restaurant_id, name, establishment_year, cuisine ---")
    for doc in restaurants.find({}, {"_id": 0, "restaurant_id": 1, "name": 1,
                                     "establishment_year": 1, "cuisine": 1}):
        print(doc)

# ---------------------------------------------
# c) FIND RESTAURANTS WITH SCORE > 90
# ---------------------------------------------
def score_more_than_90(restaurants):
    print("\n--- Restaurants with score > 90 ---")
    for doc in restaurants.find({"score": {"$gt": 90}}):
        print(doc)

# ---------------------------------------------
# d) SORT RESTAURANTS BY NAME ASCENDING
# ---------------------------------------------
def sort_by_name(restaurants):
    print("\n--- Restaurants Sorted by Name (ASC) ---")
    for doc in restaurants.find().sort("name", 1):
        print(doc)

# ---------------------------------------------
# e) UPDATE SCORE FOR ESTABLISHMENT YEAR 2019
# ---------------------------------------------
def update_score_2019(restaurants):
    new_score = int(input("\nEnter new score for restaurants established in 2019: "))
    result = restaurants.update_many(
        {"establishment_year": 2019},
        {"$set": {"score": new_score}}
    )
    print(f"Updated {result.modified_count} documents.")

# ---------------------------------------------
# MAIN MENU
# ---------------------------------------------
def main():
    db = connect_db()
    restaurants = db["restaurants"]

    while True:
        print("\n========== MENU ==========")
        print("1. Create & Insert Restaurant Records")
        print("2. Display All Documents")
        print("3. Display Selected Fields")
        print("4. Find Restaurants with Score > 90")
        print("5. Sort Restaurant Names (Ascending)")
        print("6. Update Score for Establishment Year 2019")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_and_insert(restaurants)
        elif choice == "2":
            display_all(restaurants)
        elif choice == "3":
            display_selected_fields(restaurants)
        elif choice == "4":
            score_more_than_90(restaurants)
        elif choice == "5":
            sort_by_name(restaurants)
        elif choice == "6":
            update_score_2019(restaurants)
        elif choice == "7":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
main()

"""Restaurant rating lister."""
from random import choice

def create_dictionary(file_path):
    full_ratings = open(file_path)
    restaurant_ratings = {}

    for line in full_ratings:
        line = line.rstrip().split(":")
        restaurant_ratings[line[0]] = int(line[1])

    return restaurant_ratings

def print_ratings(ratings):
    alphabetical_ratings = sorted(ratings.items())

    for rating in alphabetical_ratings:
        print(f"{rating[0]} is rated at {rating[1]}.")

def get_new_rating(ratings):
    new_restaurant = input("New restaurant to rate: ").title()
    
    validate_rating_num(new_restaurant, ratings)

    print()

    return ratings

def validate_rating_num(restaurant, ratings):
    while True:
        number = input("What should this restaurant be rated? ")
        
        if number.isnumeric() and int(number) < 6 and int(number) > 0:
            ratings[restaurant] = int(number)
            break
        else:
            print("Try again. Rate with number 1 - 5.")

        print()

    return ratings


def change_random_rating(ratings):
    list_restaurants = list(ratings.keys())
    random_restaurant = choice(list_restaurants)

    print(f"The selected restaurant is {random_restaurant}.")

    validate_rating_num(random_restaurant, ratings)

    return ratings

def change_selected_rating(ratings):
    
    for i, key in enumerate(ratings):
        print(f"{i + 1} {key}")

    print()

    while True:
        number = input("Which restaurant would you like to update? ")
        
        if number.isnumeric() and int(number) < len(ratings) + 1 and int(number) > 0:
            chosen_num = int(number)
            break
        else:
            print("Try again. Input number from given list")

        print()
    
    for i, key in enumerate(ratings):   
        if i + 1 == chosen_num:
            chosen_restaurant = key

    validate_rating_num(chosen_restaurant, ratings)

    return ratings

def ratings_app():
    current_ratings = create_dictionary('scores.txt')

    print("Welcome to the Ratings App")
    print()

    print("""You can:
    [S]ee all ratings
    [A]dd a new restaurant rating
    [U]pdate a rating of random restaurant
    [C]hoose a restaurant to change its rating
    [E]xit""")
    print()

    while True:
        user_choice = input("What would you like to do? ")
        print()

        if user_choice.upper().startswith("S"):
            print_ratings(current_ratings)

        
        elif user_choice.upper().startswith("A"):
            current_ratings = get_new_rating(current_ratings)

        elif user_choice.upper().startswith("U"):
            current_ratings = change_random_rating(current_ratings)

        elif user_choice.upper().startswith("C"):
            current_ratings = change_selected_rating(current_ratings)
            
        elif user_choice.upper().startswith("E"):
            print("Thanks! Bye!")
            break

        else:
            print("Please enter valid option")

        print()

ratings_app()
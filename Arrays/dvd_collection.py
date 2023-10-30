
# A function that holds an allocated amount of dvds in a catalog

def dvd_catalog(catalog_size):

    size = int(catalog_size)

    catalog = []

    while True:

        if len(catalog) == size:
            print("Catalog is now full.")
            break

        movie_name = input("Enter the name of the movie: ")
        director = input("Enter the directors name: ")
        release_year = input("Enter the release year: ")

        movie = f"{movie_name} directed by {director} released {release_year}"

        catalog.append(movie)

        answer = input("Would you like to add  another movie to your catalog? (y/n): ")

        if answer == "n":
            print("Thank you!")
            break
        elif answer == "y":
            continue

    return catalog


print(dvd_catalog(3))

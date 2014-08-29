import sys
import urllib2
import json

#Load movie titles from file
def load_movies(file_name):
    """ Loads all movies from the given text file into a dictionary. 
        The IMDB API is used for queries, and the running time of
        this tool is dependent on this service.
    """
    movies = {}
    success = 0
    total = 0

    print "Loading movies from \"%s\"..." % file_name
    with open(file_name, 'r') as file:
        for title in file:
            searchstring = title.rstrip('\n').replace(' ', '+')
        
            url = "http://www.imdbapi.com/?t=" + searchstring
            response = json.load(urllib2.urlopen(url))
            if response["Response"] == "True":
                minutes = response["Runtime"]
                runtime_stripped = minutes[:-4]
                movies[response["Title"]] = {"Runtime": runtime_stripped, "imdbRating": response["imdbRating"], "Metascore": response["Metascore"]}
                success += 1
            else:
                print "Unable to load %s." % (title)
            total += 1
    print "Done loading. Loaded %d/%d movies successfully.\n" % (success, total)
    return movies

def shortest_movie(movies):
    """ Finds the movie with the shortest running time. """
    shortest_minutes = 400
    shortest_title = ""    

    for title in movies:
        runtime = int(movies[title]["Runtime"])
        if runtime < shortest_minutes:
            shortest_title = title
            shortest_minutes = runtime

    return shortest_title, shortest_minutes

def highest_imdb(movies):
    """ Finds the movie with the highest IMDB rating. """
    highest_rating = 0
    highest_title = ""    

    for title in movies:
        imdb_rating = movies[title]["imdbRating"]
        if imdb_rating != "N/A" and float(imdb_rating) > highest_rating:
            highest_title = title
            highest_rating = float(imdb_rating)

    return highest_title, highest_rating

def highest_metascore(movies):
    """ Finds the movie with the highest Metascore. """
    highest_metascore = 0
    highest_title = ""    

    for title in movies:
        metascore = movies[title]["Metascore"]
        if metascore != "N/A" and int(metascore) > highest_metascore:
            highest_title = title
            highest_metascore = int(metascore)

    return highest_title, highest_metascore

def highest_weighted_rating(movies):
    """ Computes a weighted rating from the IMDB rating and Metascore
        and returns the movie with the highest value.
    """
    highest_weighted_score = 0
    highest_title = ""    

    for title in movies:
        metascore = movies[title]["Metascore"]
        imdb_rating = movies[title]["imdbRating"]
        if metascore != "N/A" and imdb_rating != "N/A":
            weighted_score = (float(imdb_rating) * 10 + int(metascore)) / 2
            if weighted_score > highest_weighted_score:
                highest_title = title
                highest_weighted_score = weighted_score

    return highest_title, highest_weighted_score

def print_movie(title, movies):
    """ Prints the movie details given a specific title. """
    if title in movies:
        #Change runtime format from minutes to hour and minutes
        runtime = convert_time(movies[title]["Runtime"])
        
        imdbRating = movies[title]["imdbRating"]
        metascore = movies[title]["Metascore"]
        
        length = len(title)
        padding = 36 - length
        print "    %s" % title, " " * padding, "%s" % runtime, " " * 15, "%s" % imdbRating, " " * 18, "%s" % metascore

def convert_time(minutes):
    """ Converts a number of minutes into hours and minutes. """
    hours = str(int(minutes) / 60) + "h"
    mins = int(minutes) % 60
    if mins < 10:
        mins = "0" + str(mins)

    return hours + str(mins)

def main():
    """ Main method to execute tool features. """
    movies = load_movies("movies_to_watch.txt")

    print "    Title", " " * 30 , "Runtime", " " * 10, "IMDB Rating", " " * 10, "Metascore"
    print " ", "-" * (len("Title") + len("Runtime") + len("IMDB Rating") + len("Metascore") + 58)
    for title in movies:
        print_movie(title, movies)

    print ""
    shortest_title, shortest_minutes = shortest_movie(movies)
    highest_imdb_title, highest_rating = highest_imdb(movies)
    highest_metascore_title, highest_meta = highest_metascore(movies)
    highest_weighted_title, highest_weighted_score = highest_weighted_rating(movies)

    print "Shortest movie: " + shortest_title + " - " + convert_time(shortest_minutes)
    print "Highest IMDB rating: " + highest_imdb_title + " - " + str(highest_rating)
    print "Highest Metascore: " + highest_metascore_title + " - " + str(highest_meta)
    print "Highest weighted rating: " + highest_weighted_title + " - " + str(highest_weighted_score)

if __name__ == '__main__':
    main()
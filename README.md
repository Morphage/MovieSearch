MovieTool
=========

A tool to help in deciding which movie to watch, based on criteria such as runtime, IMDB rating and Metascore. Uses the IMDB API and database to gather the previously mentioned information.

##### How to Use
Open a terminal or command prompt and run `python movie_tool.py`. The list of movies you want to use the tool on should be located in a file called `movies_to_watch.txt` and this file should contain the exact title of the movies, one per line. Example output of the tool is shown below:

```
python movie_tool.py
Loading movies from "movies_to_watch.txt"...
Done loading. Loaded 33/33 movies successfully.

    Title                                Runtime    IMDB Rating    Metascore
  ------------------------------------------------------------------------------------------
    Good Will Hunting                     2h06          8.2           70
    Black Swan                            1h48          8.0           79
    Life of Pi                            2h07          8.0           79
    Se7en                                 2h07          8.7           65
    The Matrix                            2h16          8.7           73
    Watchmen                              2h42          7.6           56
    The Prestige                          2h10          8.5           66
    Pulp Fiction                          2h34          9.0           94
    Bully                                 1h55          7.0           45
    The Godfather                         2h55          9.2           100
    The Avengers                          2h23          8.2           69
    Sunshine                              1h47          7.3           64
    Schindler's List                      3h15          8.9           93
    The Usual Suspects                    1h46          8.7           77
    The Shawshank Redemption              2h22          9.3           80
    The Hunger Games: Catching Fire       2h26          7.8           75
    The Machinist                         1h41          7.8           61
    The Green Mile                        3h09          8.5           61
    American Psycho                       1h42          7.6           64
    Memento                               1h53          8.5           80
    The Mist                              2h06          7.2           58
    Rosemary's Baby                       2h16          8.0           N/A
    Fight Club                            2h19          8.9           66
    Princess Mononoke                     2h14          8.4           76
    The Fountain                          1h36          7.4           51
    The Strangers                         1h26          6.2           47
    The Thing                             1h49          8.2           N/A
    American History X                    1h59          8.6           62
    Mystic River                          2h18          8.0           84
    Zodiac                                2h37          7.7           78
    Neighbors                             1h37          6.8           68
    Prisoners                             2h33          8.1           74
    Ink                                   1h47          7.0           N/A

Shortest movie: The Strangers - 1h26
Highest IMDB rating: The Shawshank Redemption - 9.3
Highest Metascore: The Godfather - 100
Highest weighted rating: The Godfather - 96.0
```

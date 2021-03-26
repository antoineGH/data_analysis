## Python Data Analysis

## Table of contents

-   [General info](#general-info)
-   [Technical Details](#technical-details)
-   [Screenshots](#screenshots)
-   [Technologies](#technologies)
-   [Setup](#setup)

## General info

URLs can be extremely long and not user-friendly. When people share links or even try to remember a URL, it’s difficult because most URLs are filled with more difficult characters and don’t form meaningful words. This is where the URL Shortener comes in. A URL Shortener reduces the characters or letters in a URL, making them easier to read and remember. A URL like xyz.com/wwryb78&svnhkn%sghq?sfiyh can be shortened to xyz.com/piojwr. With the URL Shortener, URLs become a joy to work with.

## Technical Details

The main objective of this project idea is to shorten URLs. The main task the application will accomplish is to shorten URLs and then redirect users to the original URL when the shortened URL is visited. In the application, the users will input the original URL, and they will get the new, shortened URL as the result. To do this, you can use a combination of the random and string modules to generate the characters for the shortened URL. Since users will visit the shortened URL days, months, or even years after, you’ll need to save the original and shortened URLs in a database. When a request comes in, the application checks if the URL exists and redirects to the original, or else it redirects to a 404 page.

## Screenshots

![Login Screenshot](https://github.com/antoineratat/ShortURL/blob/master/screenshots/s1.PNG?raw=true)

## Technologies

Project is created with:

-   Python v3.9.0
-   certifi v2020.12.5
-   chardet v4.0.0
-   cycler v0.10.0
-   idna v2.10
-   kiwisolver v1.3.1
-   matplotlib v3.3.4
-   numpy v1.20.1
-   panda v0.3.1
-   pandas v1.2.3
-   Pillow v8.1.2
-   pyparsing v2.4.7
-   python-dateutil v2.8.1
-   pytz v2021.1
-   requests v2.25.1
-   scipy v1.6.2
-   seaborn v0.11.1
-   six v1.15.0
-   urllib3 v1.26.4

## Setup

```
$ git clone https://github.com/antoineratat/data_analysis.git
$ py -3 -m venv venv
$ venv\Script\Activate
$ pip install -r requirements.txt
```

### Pandas / Seaborn

FIFA World Cup Goal

```
$ cd seaborn\seaborn_distribution
$ python .\fifa.py
```

### Matplotlib

Line Graphs

```
$ cd matplotlib\1_line_graphs
$ python .\line_graphs.py
```

Sublime Lines

```
$ cd matplotlib\2_sublime_lines
$ python .\sublime_lines.py
```

Plot Types

```
$ cd matplotlib\3_plot_types
$ python .\plot_types.py
```

Graph Matplotlib

```
$ cd matplotlib\4_graph_matplotlib
$ python .\graph_matplotlib.py
```

## Python Data Analysis

## Table of contents

-   [General info](#general-info)
-   [Technical Details](#technical-details)
-   [Screenshots](#screenshots)
-   [Technologies](#technologies)
-   [Setup](#setup)

## General info

This study project aims to visualize the Distribution of the goals during Word Cup football matches from 1930 to 2014.

Dataset has been downloaded from Kaggle at https://www.kaggle.com/abecklas/fifa-world-cup

> WorldCupMatches.csv (233.4Kb)

## Technical Details

Seaborn is a Python data visualization library that provides simple code to create elegant visualizations for statistical exploration and insight. Seaborn is based on Matplotlib, but improves on Matplotlib in several ways:

-   Seaborn provides a more visually appealing plotting style and concise syntax.
-   Seaborn natively understands Pandas DataFrames, making it easier to plot data directly from CSVs.
-   Seaborn can easily summarize Pandas DataFrames with many rows of data into aggregated charts.

Pandas is a data analysis library for Python that provides easy-to-use data structures and allows you to organize and manipulate datasets so they can be visualized.

## Screenshots

![Average Screenshot](https://github.com/antoineratat/github_docs/blob/main/data_analysis/1.PNG?raw=true) ![Average Screenshot](https://github.com/antoineratat/github_docs/blob/main/data_analysis/2.PNG?raw=true)

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

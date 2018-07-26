#!/usr/bin/env python


import psycopg2

DBNAME = "news"


def execute_query(query):
        """
        execute_query takes an SQL query as a parameter,
        executes the query and returns the results as a list of tuples.

        args:
          query - (string) an SQL query statement to be executed.

        returns:
          A list of tuples containing the results of the query.
        """
        try:
            # enter your code here to get a database connection and cursor,
                    db = psycopg2.connect(database=DBNAME)
                    c = db.cursor()
            # execute the query
                    c.execute(query)
            # store the results
                    results = c.fetchall()
            # close the database connection
                    db.close()
            # return the results
                    return results
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


def get_mostViewedArticles():
      """Return the most viewed articles of all time."""

      query = """
            SELECT articles.title,COUNT(*) as views
            FROM articles JOIN log
            ON log.path LIKE ('/article/' || articles.slug)
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3
      """

      posts = execute_query(query)
      print('\nWhat are the most popular three articles of all time?')
      for title, views in posts:
        print(title + " - " + str(views) + " views")


def get_mostPopularAuthors():
      """Return the most poular authors of all time."""

      query = """
        SELECT authors.name,COUNT(*) as views
        FROM articles join authors
            ON articles.author=authors.id
            JOIN log ON log.path LIKE ('/article/' || articles.slug)
            GROUP BY authors.name
            ORDER BY views DESC
      """

      posts = execute_query(query)
      print('\nWho are the most popular article authors of all time?')
      for author, views in posts:
        print(author + " - " + str(views) + " views")


def get_errorMoreThan1Percent():
      """Return the days when more than 1% of requests lead to errors """

      query = """SELECT * FROM error_Records WHERE percent > 1.00"""

      posts = execute_query(query)
      print('\nOn which days did more than 1% of requests lead to errors?')
      for i in posts:
        print(str(i[0])+'-'+str(i[1])+'% errors')


if __name__ == '__main__':
        get_mostViewedArticles()
        get_mostPopularAuthors()
        get_errorMoreThan1Percent()

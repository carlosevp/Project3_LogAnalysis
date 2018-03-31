#!/usr/bin/env python3
#
# Import the Postgres adapter for Python
import psycopg2

# Quick reference for HTML return codes used here:
# 200 OK
# 404 NOT FOUND
# As returned using the query “select distinct status from log;”

# SQL queries
# SQL query 1: What are the three most popular articles of all time?
# Filters only valid HTML code 200.
request_articles = """select articles.title, count(*) as num
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

# SQL query 2: Who are the most popular article authors of all time?
# Use only the valid HTML responses as code 200.
request_authors = """select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;
            """

# SQL query 3: On which day did more than 1% of requests lead to errors?
# Filters through HTML codes 404.
request_errors = """select time, countfails
            from v_count
            where countfails > 1;
            """


# Fetch data from the database using the SQL queries defined,
# opens and closes the connection as required.
def query_db(sql_request):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results


# Generating the report
# Print report title
def print_title(title):
    print ("\n\t\t" + title + "\n")


# Display top 3 articles
def top_three_articles():
    top_three_articles = query_db(request_articles)
    print_title("1. What are the most popular three articles of all time?")

    for title, num in top_three_articles:
        print(" \"{}\" - {} views".format(title, num))


# Display top authors
def top_three_authors():
    top_three_authors = query_db(request_authors)
    print_title("2. Who are the most popular article authors of all time?")

    for name, num in top_three_authors:
        print(" {} - {} views".format(name, num))


# Display days where more than 1% were bad HTML requests
def high_error_days():
    high_error_days = query_db(request_errors)
    print_title("3. On which days did more than 1% requests lead to errors?")

    for day, countfails in high_error_days:
        print("""{0:%B %d, %Y} - {1:.2f} % errors""".format(day, countfails))


if __name__ == '__main__':
    top_three_articles()
    top_three_authors()
    high_error_days()

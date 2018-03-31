# Log Analysis Project

**Project 3 for Full Stack Web Developer Nanodegree**

Build a report that interacts with a Postgres SQL database and generate text output with data required to answer 
3 main questions proposed by Udacity.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Write permissions are required to download and store this project.

```
It is required to use python3 to test this project. 
Assuming vagrant and VirtualBox are using Udacity's default image,
and the database was created with `psql -d news -f newsdata.sql`.
```

### Installing

git clone or download this repository. Create the required views.

### Required views

````
CREATE VIEW v_totals AS
SELECT time ::date,
       status
FROM log;
````

````
CREATE VIEW v_failed AS
SELECT time,
       count(*) AS num
FROM v_totals
WHERE status = '404 NOT FOUND'
GROUP BY time;
````

````
CREATE VIEW v_all AS
SELECT time,
       count(*) AS num
FROM v_totals
WHERE status = '404 NOT FOUND'
  OR status = '200 OK'
GROUP BY time;
````

````
CREATE VIEW v_count AS
SELECT v_all.time,
       v_all.num AS numall,
       v_failed.num AS numfailed,
       v_failed.num::double precision/v_all.num::double precision * 100 AS countfails
FROM v_all,
     v_failed
WHERE v_all.time = v_failed.time;
````

## Running the tests

On the command line, bring the VM online so we can access the database and run the code:

`vagrant up && vagrant ssh`

Navigate to vagrant/newsdata - where you should download the program code

`cd vagrant\newsdata`

Run Python to display the results

`python3 report.py`

## Versioning

Version 1.0

## Authors

* **Carlos Veiga Pereira** - *Initial work*  

## License

This project is licensed under the GNUv3 License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Udacity team for offering the Full Stack Web Developer Nanodegree, specially my mentor Evan who is always available to help.

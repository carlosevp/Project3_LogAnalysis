# Log Analysis Project

**Project 3 for Full Stack Web Developer Nanodegree**

Build a report that interacts with a Postgres SQL database and generate text output with data required to answer 
3 main questions proposed by Udacity.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Write permissions are required to download and store this project and required software.

#### Steps:
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone or download this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **[newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)** file and move them to your **vagrant** directory within your VM. 

```
It is required to use python3 to test this project. 
Assuming vagrant and VirtualBox are using Udacity's default image,
and the database was created with `psql -d news -f newsdata.sql` after step 4.
```

### Installing

Create the required views.

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

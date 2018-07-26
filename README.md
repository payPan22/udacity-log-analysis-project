# Reporting Tool
The third project in Udacity's full stack web development nanodegree program.

## Project Overview
The aim of the project is to create a reporting tool that prints out reports (in plain text) based on the data in the database provided. The database is a PostgreSQL database for a news website.The database is named 'news' and has 3 tables - authors,articles and log. Running the file newsdata.sql will execute the SQL commands in the file, creating tables and populating them with data. The authors table includes information about the authors of articles.
The articles table includes the articles themselves. The log table includes one entry for each time a user has accessed the site. The python script reportingTool.py answers the following questions - What are the most popular three articles of all time?,Who are the most popular article authors of all time? and On which days did more than 1% of requests lead to errors?</h2>


## Requirements
1. Python 2 - The code uses ver 2.7.2
2. Vagrant - A virtual environment builder and manager
3. VirtualBox - An open source virtualization product.


## Access the project
For using this project, follow the steps listed below:

1. Download Python - https://www.python.org/getit/
2. Downlaod and install VirtualBox - https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
3. Download and install Vagrant - https://www.vagrantup.com/downloads.html
4. You will need a terminal.If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, use the Git Bash terminal that comes with the Git software. Link - https://git-scm.com/downloads
5. Download the VM configuration. Use Github to fork and clone the repository - https://github.com/udacity/fullstack-nanodegree-vm
6. You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory.
7. From your terminal, inside the vagrant subdirectory, run the command **vagrant up**. This will cause Vagrant to download the Linux operating system and install it. 
8. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run **vagrant ssh** to log in to your newly installed Linux VM.
9. Download the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
10. To load the data, cd into the vagrant directory and use the command **psql -d news -f newsdata.sql**.
11. To run the database type psql -d news
12. Unzip the contents of the reportingTool.zip and place the reportingTool.py inside the vagrant directory.
13. You must run the commands from the Create views section here to run the python program successfully.
14. Use command **python reportingTool.py** to run the python program that fetches query results.


## Create Views
A View (error_records) was created to answer the third query in the project with the purpose of leaving the original database unchanged. 

```sql
CREATE VIEW error_records AS
SELECT date(time),ROUND(100.00*sum(case log.status when '200 OK' then 0 else 1 end)/COUNT(log.status),2) as percent FROM log group by date(time) ORDER BY percent DESC; 
```
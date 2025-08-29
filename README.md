# What is this for?

This SQL-SERVER allows you to quickly, and easily setup an SQL server for database interaction, and integration into a software. 

# How to use it? 

Simple just run setup.bat, this will install all dependencies, and automatically run server.py. 

To test it on Windows, you can run: `curl -X POST http://127.0.0.1:8000/edp -H "Content-Type: application/json" -d "{\"SQL\": \"sql_command\", \"db\": \"db_name\"}"`
The result should be: `{"ERROR":"There was a syntax ERROR: near \"sql_command\": syntax error"}` - Needs proper SQL

You can test better with the `TEST.py` script.

# Flask - PostgreSQL - Heroku Boilerplate

**detailed instructions on setting up app are coming**

This repo contains a boilerplate Flask App. All application code is inside of the application dir, and is run from the run.py file. This app takes a package based approach to building a Flask app. The structure is quite more complicated than a basic Flask app but should be better suited for larger applications.

There is more I can / plan to add but this should be a good starting point.  

## Setup
* all python commands should be python3 / pip3
* you will need to setup a local env `python3 -m venv <name>`
* you **can** setup autoenv (instructions to follow)
* you will need to create a file outside of the application called local_env/secrets.py
    * this is where your SECRET_KEY and other API keys should go
    * these are set to be ignored by git
    * you can set these config vars from the Heroku CLI or App settings online
    * DATABASE_URL is sourced from here, can be hardcoded in config.py if you want
* you need to pip3 install from the requirements.txt file
* you should probably delete the migrations folder before trying to migrate your database
* setup a postgreSQL database 
    ```shell script
      psql
      create database <db-name>;
      \c <db-name>
      \q # to exit
    ```
* to locally migrate the db run `flask db init` `flask db migrate` `flask db upgrade`
* to migrate the database on Heroku (better instructions coming)
    * create the Postgres DB as an addon in Heroku
    * `git commit` `git push heroku master`
    * `heroku run flask db upgrade --app <app-name>`
        * need to re-confirm this
        * should just need to do upgrade if migration folder exist
        

## the sample API
The sample API provided provides basic CRUD operations on a User table (id, name). The app utilizes blueprints but only returns JSON. You will need to add templates/ views/ static etc. to take full advantage of blueprints. 



### Endpoints
* "/" - [GET] redirects to show all users
* "/users" - [GET] shows all users
* "/users/<value>" - [GET] search for name or id
* "/users/string:name" - [POST] adds a user
* "/users/int:id" -- [PUT] updates a users information
* "/users/int:id" -- [DELETE] removes a user

## todo
* add basic testing
* update docs to clarify setup instructions
* clarify which files are needed for setting up Heroku
* link to repos / articles / tutorials that inspired this
* use this to actually build something, lol
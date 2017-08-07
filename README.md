# mlab_demo_county_demographics

A second mlab demo, with no web app involved.   

We are using data from the CORGIS project, specifically the [county
demographics
file](https://think.cs.vt.edu/corgis/json/county_demographics/county_demographics.html)
which in turn, gets its data from the [US
Census](http://www.census.gov/quickfacts/table/PST045215/00)

The original file can be downloaded from
[here](https://think.cs.vt.edu/corgis/json/county_demographics/demographics.json?forcedownload=1)

A snapshot of that file is in this repo in
[demographics.json](demographics.json)

# To use this application

1.  Copy the env.sh.SAMPLE to a file called env.sh (this EXACT filename) and
    then edit that file to have the confidential values for username, password,
    etc. for accessing the database.

    Note that it is IMPORTANT to call it exactly `env.sh` because that filename
    appears in `.gitignore`, so that your username/password won't be
    compromised.  Don't use another filename unless you understand what you
    are doing.

    The value in env.sh come from the screen in MLab for the MongoDB Deployment
    (see: https://ucsb-sbhs-cs.github.io/topics/mongodb_mlab/ )
	
	Note for Windows Users:  Copy the env.sh.SAMPLE to a file called env.bat and change all "export" commands to "set" commands.

2.  Run python upload_json_data_to_mongodb.py demographics.json to upload the contents to a MongoDB database.

3. Run python get_json_data_to_mongodb.py to retrieve a record by its primary key.


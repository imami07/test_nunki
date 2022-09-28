# API : Test technique Nunki
This API was built using Flask library from Python.

this API has the following enspoints :

- GET /users/<user_id> : Get txitter user details using th screen name.
- GET /search?q=<keyword>&media=<boolean> : Get tweets containing a specific keyword given in parameter 'keyword' & media content if patameter 'media' = "True".


How to run the API : 
Step 1 : Launch the python script twitter_wrraper_api.py with the following command line python twitter_wraper_api.py
Step 2 : Copy the following like to the browser & start testing the endpoints : 
- 127.0.0.1:5000/users/<user_id>
- 127.0.0.1:5000//search?q=<keyword>&media=<boolean>

Examples : 
127.0.0.1:5000/users/elonmusk to get all details about Elon Musk twitter account.
127.0.0.1:5000/search?q=bitcoin&media=True to get tweets related to bitcoin with media content.

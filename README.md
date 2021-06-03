


In brief this project leverage Django and Django rest framework to mimic tweeter.So a user can browse our users profiles and their tweets , comment ,like or dislike their tweets 
if wanted.
The core project is built using django rest framework ModelViewset and the nested routing is ensured by drf-nested-routers framework which I have found more interesting to use 
because if its conciseness.
Main routes:

1. /api/profiles/  or /api/profiles/<pk> ; Accepted Methods=["POST","HEAD","PATCH","DELETE","GET","PUT"] and Content_Type : Application/json ;

2. /api/tweets/ or  /api/tweets/<tweet_pk> ; Accepted Methods=["POST","HEAD","PATCH","DELETE","GET","PUT"] and Content_Type : Application/json ;

3. /api/comments/ or /api/cooments/<comment_pk> ; Accepted Methods=["POST","HEAD","PATCH","DELETE","GET","PUT"] and Content_Type : Application/json ;

3. /api/profiles/<pk>/tweets/<tweet_pk> ; Accepted Methods=["HEAD","GET"] and Content_Type : Application/json ;

4. /api/tweets/<tweet_pk>/tweets/<comment_pk> ; Accepted Methods=["HEAD","GET"] and Content_Type : Application/json ;

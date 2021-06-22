


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

5. /api/tweet_likes/ or /api/tweet_likes/<tweet_like_pk> ; Accepted Methods=["POST","HEAD","PATCH","DELETE","GET","PUT"] and Content_Type : Application/json ;
  
6. /api/comment_likes/ or /api/comment_likes/<tweet_like_pk> ; Accepted Methods=["POST","HEAD","PATCH","DELETE","GET","PUT"] and Content_Type : Application/json ;
  
7. /api/tweets/tweet_likes/ or /api/tweets/tweet_likes/<tweet_like_pk> ; Accepted Methods=["HEAD","GET"] and Content_Type : Application/json ;
  
8. /api/comments/comment_likes/ or /api/comments/comment_likes/<comment_like_pk> ; Accepted Methods=["HEAD","GET"] and Content_Type : Application/json ;
  
  
 NB: As every project needs improvement .This project could enhance using a python grapghQL server to resolve complexe relationship between different entities or models for 
complexes routhing .GraphQL technology is the cutting edge of web server technology and it's the best solution for implementing a complexe routing web technology in my humble
opinion.

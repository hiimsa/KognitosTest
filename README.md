# KognitosTest
HTTPS GET Endpoint :
https://vfawjrs678.execute-api.ap-southeast-2.amazonaws.com/default/histogram_counter?word=Kognitos

How to use: Replace the word with any other word in the above URL 
?word=<>

Approach:
Traverse the string and store the all char in lowercase to a Dictionary/MAP
Used Amazon EFS to persist across different lambda invocation

At the Lambda initialization, we read the cache and update the cache in the mounted path

Caveat:
Somehow it is not working after lambda timeout. 

Another Approach: 
Use Amazon Dynamo DB for persisting cache. Didn't get time for that. Above approach took me more than 4 hours due to debugging.


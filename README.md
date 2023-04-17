# KognitosTest
HTTPS GET Endpoint :
https://vfawjrs678.execute-api.ap-southeast-2.amazonaws.com/default/histogram_counter?word=Kognitos

How to use: Replace the word with any other word in the above URL 
?word=<>
 
Approach:
Traverse the string/word and store all distinct chars in lowercase to a Dictionary/MAP
I have ysed Amazon EFS to persist data across parallel lambda invocation

At the Lambda initialization, we read the cache from mounted EFS path and update the cache after every word processed. 

EFS endpoint:
https://ap-southeast-2.console.aws.amazon.com/efs/home?region=ap-southeast-2#/file-systems/fs-021623a0ef1a094e3

Problem in the existing code:
Somehow it is not working after lambda timeout. It means it is working with multiple parallel execution but stops working after Lambda instance got timed out. 
We need to use a persistent db to solve this.
I am sorry I didn't get time to debug the EFS duarabilty issue: 
I may go for Amazon Dynamo DB for persisting cache.

Other optimizations:
If the string is too large, we can do the parallel processing in multiple threads.
May go for fork & join pool. 


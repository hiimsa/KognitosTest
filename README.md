# KognitosTest
HTTPS GET Endpoint :
https://vfawjrs678.execute-api.ap-southeast-2.amazonaws.com/default/histogram_counter?word=Kognitos

How to use: Replace the word with any other word in the above URL 
?word=<>
 
Approach:
Traverse the string and store the all char in lowercase to a Dictionary/MAP
Used Amazon EFS to persist across different lambda invocation

At the Lambda initialization, we read the cache and update the cache in the mounted EFS path

EFS endpoint:
https://ap-southeast-2.console.aws.amazon.com/efs/home?region=ap-southeast-2#/file-systems/fs-021623a0ef1a094e3

Problem in the existing code:
Somehow it is not working after lambda timeout. It means it is working with multiple parallel execution nut stops working after Lmabda instance timeout. 
We need to use a persistent db to solve this.
I am sorry I didnt get time to debug the EFS for duarabilty issue: 
I may use Amazon Dynamo DB for persisting cache if time persists.

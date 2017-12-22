# Channel Management

### Objectives

1. Assign phone numbers to channels and changes phone
numbers as needed.
2. Minimize the number of phone numbers allocated.
3. Do not allow collisions.
4. Minimize the impact of a channel phone number change.
5. Minimize the number of potential channel phone number changes by balancing
the phone number allocations such that least used phone numbers are the first
to be allocated when a new channel needs a number.

### Code

src contains the Channel, Following and User classes. 

Channel class contains assign_phone_number method which assigns phone numbers such that 
all objectives are met. 

User class contains the follow_channel method which makes the particular
 user follow the specified channel. If there is a collision after the new following, 
 the phone numbers of the channels are changed subject to the constraints in the objective. 
 
utils is a utility module which contains functions for getting 
least used phone number, least impacted channel and detecting collisions. 
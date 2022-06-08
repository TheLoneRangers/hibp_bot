# HIBP bot.
At the moment, this loops through a yaml list and submits an auth'd request to haveibeenpwned.com to check for pwnage of a particular email address.  

The API key for HIBP is in AWS Parameter store, so wherever this runs needs access to that. This will eventually run in lambda. 
The email list is currently in my .gitignore file because there's no need to make that data public, but it's set up like this:
```
---
  - emailaddress1@something.com
  - emailaddress2@somethingelse.com
```
Eventually this will reside in s3, so that access will also be needed.  
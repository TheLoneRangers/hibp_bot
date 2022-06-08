# Further plans
- Source emails.yaml from s3 instead of here in the repo
- more routes/api calls to HIBP
- validate this works for >1 domain...
- full lambda-ization

# Possible features
- API gateway?
  - would allow easier control over params
- dynamic updating of email list

## In-Progress things
### feature1 branch
- A "good" (read: no breaches) result right now is a 404, which checks out via the HIBP api docs.  Need to add some checks/handling to handle that good output better.  If there are no breaches, do we care?  
- get/source email list from s3
- validate >1 domain functions correctly
  - it did/does, but I was mis-using the api route, so refactored so this is no longer a worry since we don't have to worry about specific domains
- Not sure how to test this, but it'd be nice to have a known-pwned address to verify this works right. 
- need to add some sleeps/rate limit handling
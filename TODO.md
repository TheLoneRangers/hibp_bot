# Further plans
- more routes/api calls to HIBP
- slack integration for on-demand run?
  - flask fronted? jenkins webhook? 
- ad-hoc runs, probably from slack

# Possible features
- API gateway?
  - would allow easier control over params
  - maybe flask for this?
- dynamic updating of email list

## In-Progress things
### feature1 branch
- A "good" (read: no breaches) result right now is a 404, which checks out via the HIBP api docs.  Need to add some checks/handling to handle that good output better.  If there are no breaches, do we care?  
- get/source email list from s3
- validate >1 domain functions correctly
  - it did/does, but I was mis-using the api route, so refactored so this is no longer a worry since we don't have to worry about specific domains
- Not sure how to test this, but it'd be nice to have a known-pwned address to verify this works right. 
- need to add some sleeps/rate limit handling
  - done, but hacky

### feature2 branch
- change "no breach" result to handle the 404 "good result"
  - oops, this was actually already done.
- dockerization
  - done. jenkins is local-only, but the container builds, runs, and outputs results to the console. Need to figure out how to properly surface results to people, but that's probably not going to happen here in Git. 

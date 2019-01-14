# HolidayProject2018
Search a website for a given word over time, or search for changes in general over time.

**You need to create a file named "variables.py" that contains your Twilio account SID (named "account_sid"), your authentication token (named"auth_token"), and your Twilio phone numer (named "twilio_phone_number").**

githoliday_final_stable.py is the most stable. Only use githoliday.py to look at other potential ways of doing this that I didn't end up using. I can't find the problem with githoliday_final.py, but it has several errors and doesn't run. Were it to work correctly, githoliday_final.py would be the most complete version.

index.html is just being used as a sample site for testing that can be easily controlled and updated.

Only major bug: When looking for changes and not cancelling after a success, the function doesn't update the original page contents, it just bases future changes on the page content that was declared outside of either function. Because of this, after one change, it will say that it has changed every time it checks even if there was only one change made at a certain time.

**Update: githoliday_ultraminimal.py is the simplest, smallest file and only checks changes. Use this if anything.**

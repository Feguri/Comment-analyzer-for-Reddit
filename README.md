# Comment-analyzer-for-Reddit
This Python software will scan all the 'p' elements in a website and separate all the keywords selected by the user into an ordered list.

Video Help -> https://youtu.be/vX-ZG5A0P_E
# Step 1
Istall the chrome driver at https://chromedriver.chromium.org/downloads. You should use the latest version for chrome.
save the path to chromedriver.exe and input it into the 'path' variable
# Step 2
set variables for wait_time (seconds), alist and url for the Analyze Class.

# Step 3
The point of wait_time is to set a time for you to scroll through the comments of the reddit page you want to data mine, therefore loading the comments.
the key word elements in your list will compare to all p instances in the HTML page.



# Example result:
Comments analysis:
{'not': 17, 'is': 37}

Percentage analysis:
{'not': '31.48%', 'is': '68.52%'}

Comments analyzed:
227

# Any bugs or problems 
please contact 
felipeserrou@hotmail.com

'''
Given  pairs of names and email addresses as input,print each name and email address pair having a valid email
address on a new line.

===============================================================
Input:
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Output:
DEXTER <dexter@hotmail.com>

=================================================================
    Time Complexity:    O(N)
    Space Complexity:   O(N)
    
 
'''

############
# Solution #
############

# Import the necessary modules.
import re
import email.utils

N = int(input())

pattern = re.compile(
    r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")

for i in range(N):
    # Parse the input string and get the name and email address.
    name, email_id = email.utils.parseaddr(input())
    # Check Pattern Matching
    validation = re.match(pattern, email_id)
    if validation:
        # Print the name and email address pair.
        print(email.utils.formataddr((name, email_id)))

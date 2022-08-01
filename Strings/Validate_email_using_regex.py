'''
Solution to the problem "Validating and Parsing Email Addresses
from the HackerRank challenge.
'''
# -----------------------------------------------------------------------
# Given  pairs of names and email addresses as input,
# print each name and email address pair having a valid email
# address on a new line.

# Input Format
# The first line contains a single integer,N ,
# denoting the number of email address.
# Each line i of the n subsequent lines contains a name and an email address
# as two space-separated values following this format:
# name <user@email.com>
#
# Constraints:
# 0 <= N <= 100
# Print the space-separated name and email address pairs containing valid email
# addresses only.
# Each pair must be printed on a new line in the following format:
# name <user@email.com>
#
# Sample Input:
# 2
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>
#
# Sample Output:
# DEXTER <dexter@hotmail.com>
# -----------------------------------------------------------------------
# Solution:
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

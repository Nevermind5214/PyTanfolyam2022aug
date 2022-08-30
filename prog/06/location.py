"""
A junior Python programmer wants to have a user input a location
and then have the location print on the screen.
In addition, the developer wants to tell the user to enter
North, South, East, or West for a location and have the user
try again if a proper location is not entered or
print the location if the location is North, South, East, or West.

location = ["North", "South", "West", "East"]
response = input("Enter North, South, West, or East for a location: ")
"""

def main():
    location = ["North", "South", "West", "East"]
    response = ""
    while True:
        response = input("Enter North, South, West, or East for a location: ")
        if response not in location: print("Try again")
        else:
            print(response)
            break

##############################################################################

if __name__ == "__main__":
    main()

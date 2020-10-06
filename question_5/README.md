This solution was built in Python 3.8, relying heavily on pandas to interface with the csv.

Known Issues:
* No tests for question 5: Due to time constraints, I wasn't able to get to testing the weather station data solution.
* I've done the bulk of my testing on an abbreviated version of the full data.csv (short_data.csv that I've included) to make debugging easier.
* Pandas dataframes seem to be adding a .0 to all ints passed in, given the time constraights I just rounded the outputs.  I didn't see any siginificant issues with doing that, but that conversion is likely costly on large datasets, and adds in some uncertainty about any calculations.
* Not quite an issue, but and improvement I'd like to make.  As I write this, one of the top stories on Hacker News is that Python 3.9 just came out and changed how Typing declarations work in Python, so that should be upgraded (importing Typing is pretty clunky).
* We might considering changing from tuples to make it a bit more readable.  Using a named tuple would probably make this code easier to maintain.

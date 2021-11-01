[![Build Status](https://app.travis-ci.com/vnsvakanda/ku-polls.svg?branch=main)](https://app.travis-ci.com/Ing140943/ku-polls)     
[![codecov](https://codecov.io/gh/vnsvakanda/ku-polls/branch/main/graph/badge.svg?token=O5A09DJNU3)](https://codecov.io/gh/vnsvakanda/ku-polls)

# KU-polls

Web applications for conducting surveys and polls to the community. [Click here!](https://github.com/vnsvakanda/ku-polls/wiki) for more details.

## Project Documents

* [Vision Statement](https://github.com/vnsvakanda/ku-polls/wiki/Vision-Statement)
* [Requirements](https://github.com/vnsvakanda/ku-polls/wiki/Requirements)

Iteration Plans

* [Iteration1](https://github.com/vnsvakanda/ku-polls/wiki/Iteration-1)
* [Iteration2](https://github.com/vnsvakanda/ku-polls/wiki/Iteration-2)
* [Iteration3](https://github.com/vnsvakanda/ku-polls/wiki/Iteration-3)


## Running KU Polls

Users provided by the initial data (users.json):

| Username  | Password    |
|-----------|-------------|
| admin     | 123456789    |
| saimai     | natnaree2544    |
| demo1     | Vote4me1    |
| demo2     | Vote4me2    |

## Initialize Polls Data in a New Installation
### Command
When someone installs the application in a new location, the person should be able to recreate the database using:
```python3 manage.py migrate```
```python3 manage.py loaddata users polls```
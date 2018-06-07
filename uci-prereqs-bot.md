# uci-prereqs-bot

WIP for a reddit bot that gives you the prerequisites for a UCI course. it comes in two parts:

- creates a json file for the desired course department's courses and its prereqs
- runs a reddit bot to reply to a comment requesting a course's prereqs

it also creates a logfile that records any comments and errors the bot generates while trying to post comments.

**very** *very* ***very*** much still a work in progress! this is a very quick and rough implementation. read the TODO!

## getting started

### you'll need

- praw
- python3

### specifics

- edit uciprereqsbot.sh and change `dept` to whichever department you'd like to get courses from
- edit bot.py and change `subreddit = reddit.subreddit('X')` where X is the subreddit you'd like to monitor

## usage
- generate the json source for prereqs

```
./uci-prereqs-bot.sh --get-prereqs
```

- run the bot

```
./uci-prereqs
```

- summon the bot on reddit
  - comment "UCIPreReqs DEPARTMENT NUM" for prerequisites
  - example: UCIPreReqs COMPSCI 161
  
## TODO

there's a lot of room for improvement (obviously!)

- write some tests
- automate creation of multiple department's course json files
- monitor multiple departments
- handle comments with additional text (other than the call for the bot and the course name)
- fix formatting of comment replies
- make code readable, fix variable/function names, make it more efficient
- clean up log files

## goals

- use regular expressions with python in a project
- create a functioning reddit bot
- write a shell script to automate part of the proccess (in this case downloading the prereqs html page is sort of automated)
- use and produce a json file
- put something on github

## acknowledgements

thanks to @billycastelli for showing me how to make a reddit bot at your workshop!
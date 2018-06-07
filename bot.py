# !/bin/python
# run the reddit bot!
import praw
import json
import datetime
import sys

# open json to access course info
dept = sys.argv[1]
classfile = open(dept + '.json')
classes = json.load(classfile)

reddit = praw.Reddit(
						client_id = '',
						client_secret = '',
						username = '',
						password = '',
						user_agent = 'web:UCIPrereqsBot (by /u/)'
					)

subreddit = reddit.subreddit('test')

logfile = open('log' + ''.join(str(datetime.datetime.utcnow()).split()) + '.txt', 'w')

for comment in subreddit.stream.comments():
	if 'UCIPreReqs' in comment.body:
		course = comment.body.split('UCIPreReqs')[1][1:].strip()
		formattedcourse = '**' + course + '**'

		try:
			reply = formattedcourse + ': ' + classes[course]['title'] + '\n\n **Prerequisites**:'

			for req in classes[course]['prereqs']:
				reply = reply + ' ' + req + 'AND'

			reply = reply[:-3]
			comment.reply(reply)

			logfile.write(datetime.datetime.now().strftime('%H:%M:%S') + ':: ' + 'Success! posted a comment.\n')
			logfile.write('\tComment ID: '+ comment.fullname)
			logfile.write('\n\tComment Content: ' + reply + '\n')

		except praw.exceptions.APIException as apiexception:
			logfile.write(datetime.datetime.now().strftime('%H:%M:%S') + ':: ' + 'ERROR: Cannot post comment. APIException: ' + apiexception.message + '\n')
		except praw.exceptions.ClientException as clientexception:
			logfile.write(datetime.datetime.now().strftime('%H:%M:%S') + ':: ' + 'ERROR: Cannot post comment. ClientException: ' + clientexception.message + '\n')
		except KeyError:
			logfile.write(datetime.datetime.now().strftime('%H:%M:%S') + ':: ' + 'ERROR: Invalid course requested. Course attempted: ' + course + '\n')
		# except:
		# 	logfile.write(datetime.datetime.now().strftime('%H:%M:%S') + ':: ' + 'ERROR: Cannot post comment, some other error occurred\n')

logfile.close()
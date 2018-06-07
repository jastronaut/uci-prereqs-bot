# !/bin/python
# get prerequisites from an html page and put them into a file

import re
import json
import sys

def get_file(dept: str) -> 'file':
	f = open('prereqspage' + dept + '.html')
	start = 299 # where the list of prereqs begin
	for i in range(start):
		f.readline()
	return f

def get_course(courses: dict, f: 'file', dept: str) -> 'dict':

	curLine = f.readline()
	while curLine.find('name') < 0:
		if '&nbsp;' in curLine:
			while curLine.find('</tr>') < 0:
				curLine = f.readline()
			return False
		if 'contact-footer' in curLine:
			return True
		curLine = f.readline()
	course = dept + ' ' + curLine.split('"')[1]

	while curLine.find('title') < 0:
		curLine = f.readline()

	title = re.sub(r'\n', '', f.readline())

	while curLine.find('prereq') < 0:
		curLine = f.readline()
	prereqs = f.readline().split('<br>')

	prereqs = pretty_prereqs(prereqs)

	while curLine.find('</tr>') < 0:
		curLine = f.readline()
	courses[course] = { "title": title, "prereqs": prereqs }

	return False

def extract_prereqs(line: str, prereqs: []) -> None:
	prereqs.append(' '.join(re.sub(r'<\W?[\w]+>|\(|\)|\n', '', line).split()))	

def pretty_prereqs(reqs: [str]) -> []:
	newreqs = []
	for i in range(len(reqs)):
		if 'AND' not in reqs[i]:
			extract_prereqs(reqs[i], newreqs)
	return newreqs


def print_courses(classes: 'dict') -> None:
	for course in classes:
		print(course, ":", classes[course]["title"])
		print('\tPREREQUISITES:')
		print('\t', classes[course]["prereqs"])


def create_prereqs(dept: str):
	classes = {}

	f = get_file(dept)
	done = False

	while done == False:
		done = get_course(classes, f, dept)

	f.close()

	deptclasses = open(dept + '.json', 'w')
	jsonclasses = json.dump(classes, deptclasses)

if __name__ == '__main__':
	create_prereqs(sys.argv[1])
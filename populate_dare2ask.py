import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					'dare_2_ask_project.settings')

import django
django.setup()
from dare2ask.models import Lecture, Question

def populate():

	WAD_questions = [
		{"lecture":"WAD",
		 "text":"What does XML stand for?",
		 "upvotes":0,
		 "answered":False},
		{"lecture":"WAD",
		 "text":"What does AJAX stand for?",
		 "upvotes":5,
		 "answered":False}
	]

	Robotics_questions = [
		{"lecture":"Robotics",
		 "text":"Why does my battery keep running out?",
		 "upvotes":0,
		 "answered":False},
		{"lecture":"Robotics",
		 "text":"What are the three laws of robotics?",
		 "upvotes":3,
		 "answered":False},
		{"lecture":"WAD",
		 "text":"Are robots going to take over the world?",
		 "upvotes":10,
		 "answered":False},
	]

	lectures = {"WAD": {"questions":WAD_questions, "join_ID":1},
				"Robotics": {"questions":Robotics_questions, "join_ID":2}}

	for lec, lec_data in lectures.items():
		l = add_lecture(lec, lec_data["join_ID"])
		for q in lec_data["questions"]:
			add_question(l, q["text"], q["upvotes"], q["answered"])

	for l in Lecture.objects.all():
		for q in Question.objects.filter(lecture=l):
			print("- {0} - {1}".format(str(l), str(q)))

def add_question(lec, text, upvotes, answered):
	q = Question.objects.get_or_create(lecture=lec, text=text)[0]
	q.upvotes = upvotes
	q.answered = answered
	q.save()
	return q

def add_lecture(lecture, join_ID):
	l = Lecture.objects.get_or_create(title=lecture)[0]
	l.join_ID=join_ID
	l.save()
	return l


def add_user():

def add_lecture():
	c =

#Start execution here!
if __name__ == '__main__':
	print("Starting Dare2Ask population script...")
	populate()

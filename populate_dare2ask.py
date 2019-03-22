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
	print("questions created")
	lectures = {"WAD": {"questions":WAD_questions, "join_ID":1},
				"Robotics": {"questions":Robotics_questions, "join_ID":2}}
	print("lectures created")
	for lec, lec_data in lectures.items():
		l = add_lecture(lec, lec_data["join_ID"])
		for q in lec_data["questions"]:
			add_question(l, q["text"], q["upvotes"], q["answered"])
	print("here")
	for l in Lecture.objects.all():
		for q in Question.objects.filter(lecture=l):
			print("- {0} - {1}".format(str(l), str(q)))


def add_question(lec, text, upvotes, answered):
	print("adding question")
	q = Question.objects.get_or_create(lecture=lec, text=text)[0]
	q.upvotes = upvotes
	q.answered = answered
	q.save()
	return q

def add_lecture(lecture, join_ID):
	print("adding lecture")
	l = Lecture.objects.get_or_create(title=lecture)[0]
	print("1")
	l.join_ID=join_ID
	print("2")
	l.save()
	print("3")
	return l


#Start execution here!
if __name__ == '__main__':
	print("Starting Dare2Ask population script...")
	populate()

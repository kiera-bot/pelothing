
#Imports then gives list of all my workouts.
from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
workout = workouts[0]

for session in workouts:
	try:
		if session.metrics:
			print(session.metrics)
	except Exception as e:
		print(e)
	print(session)
	print(session.id)
	print(dir(session))
	print(type(session))
	print()
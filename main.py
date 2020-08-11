
#Imports then gives list of all my workouts.
from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
workout = workouts[0]

for session in workouts:
	try:
		print(dir(session.metrics))
		distance = session.metrics.distance_summary.value
		print('I went %s miles' % distance)
		# print(session.metrics.distance_summary.value)
		# print(session.metrics.speed)
		# print(session.metrics.output_summary)
		# print(session.metrics.output)
		# print(session.metrics.calories_summary)
	except Exception as e:
		print(e)
	
	print()

#Imports then gives list of all my workouts.
from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
workout = workouts[0]

for session in workouts:
	try:
		# print(dir(session))
		distance = session.metrics.distance_summary.value
		print('I went %s miles' % distance)
		# print(session.metrics.distance_summary)
		speed = session.metrics.speed.average
		print('Averaged %s mph' % speed)
		# print(session.metrics.speed.average)
			# average, max, name, serialize, slug, unit, values
		output = session.metrics.output_summary.value
		print('Generated %s watts' % output)	
		# print(session.metrics.output_summary.value)
			# name, serialize, slug, unit, value
		# print(session.metrics.output)
			# this appears to be all output generated, probably for graphs.
			# average, max, name, serialize, slug, unit, values
		calories = session.metrics.calories_summary.value
		print('Burned an estimated %s calories' % calories)
		# print(session.metrics.calories_summary.value)
			# name, serialize, slug, unit, value
		workout_time = session.metrics.workout_duration.real / 60
		print('Over a period of %s minutes' % workout_time)
			# mkay i believe it outputs the duration of the workout in seconds...
			# 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'
		date = session.end_time
		print('On %s' % date)
	except Exception as e:
		print(e)
	
	print()
		#why do i need this last print again?
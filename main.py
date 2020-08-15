# Imports
import csv
import time
from peloton import PelotonWorkout 
from absl import app
from absl import flags
from absl import logging

# Global Variables
# FLAGS = flags.FLAGS
# flags.DEFINE_string('csv_output', None, 'name of csv file to output')
# flags.mark_flag_as_required('csv_output')
FILENAME = 'peloton-%s.csv' % time.strftime('%F')


# Funky Functions
# Grabbing data beeop boop
def parse_workout(workout):
	try:
		parsed_data = {
			'distance': workout.metrics.distance_summary.value, 
			'speed': workout.metrics.speed.average,
			'output': workout.metrics.output_summary.value,
			'calories': workout.metrics.calories_summary.value,
			'workout_time': workout.metrics.workout_duration.real / 60,
			'date': workout.end_time.strftime('%F'),
		}
		return parsed_data

		

	except Exception as e:
		logging.error(e)
	return


# Main Function
def main(argv):
	print(FILENAME)
	logging.info('starting program')
	workouts = PelotonWorkout.list()

	with open(FILENAME, 'w', newline='') as csvfile:
	    fieldnames = ['distance', 'speed', 'output', 'calories', 'workout_time', 'date']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	    writer.writeheader()
	    for workout in workouts:
			workout_data = parse_workout(workout)
			writer.writerow(workout_data)

# okay so i got it 
	# with open(FILENAME, 'w') as csvfile:
	# 	writer = csv.writer(csvfile)

	# 	for value in workout_data.items():
 #   			writer.writerow(value)

# okay so i got it 
	 # with open(FILENAME, 'w') as csvfile:
	 # 	writer = csv.writer(csvfile)

		# for value in workout_data.items():
  #  			writer.writerows(value)


   	#well...this writes a csv + the first row ;/
		# with open(FILENAME, 'w') as csvfile:
		#     fieldnames = ['distance', 'speed', 'output', 'calories', 'workout_time', 'date']
		#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		#     writer.writeheader()
		#     writer.writerows(parsed_data.values)

	#this writes an empty csv but looks promising...
		# with open(FILENAME, 'w') as csvfile:
		#     writer = csv.DictWriter(csvfile)

		#     writer.writeheader(parsed_data.keys)
		#     writer.writerow(parsed_data.values)	
		


	# for session in workouts:
	# 	try:
	# 		# print(dir(session))
	# 		distance = session.metrics.distance_summary.value
	# 		print('I went %s miles' % distance)
	# 		# print(session.metrics.distance_summary)
	# 		speed = session.metrics.speed.average
	# 		print('Averaged %s mph' % speed)
	# 		# print(session.metrics.speed.average)
	# 			# average, max, name, serialize, slug, unit, values
	# 		output = session.metrics.output_summary.value
	# 		print('Generated %s watts' % output)	
	# 		# print(session.metrics.output_summary.value)
	# 			# name, serialize, slug, unit, value
	# 		# print(session.metrics.output)
	# 			# this appears to be all output generated, probably for graphs.
	# 			# average, max, name, serialize, slug, unit, values
	# 		calories = session.metrics.calories_summary.value
	# 		print('Burned an estimated %s calories' % calories)
	# 		# print(session.metrics.calories_summary.value)
	# 			# name, serialize, slug, unit, value
	# 		workout_time = session.metrics.workout_duration.real / 60
	# 		print('Over a period of %s minutes' % workout_time)
	# 			# mkay i believe it outputs the duration of the workout in seconds...
	# 			# 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'
	# 		date = session.end_time
	# 		print('On %s' % date)
	# 	except Exception as e:
	# 		print(e)
		
	# 	print()

	# with open('eggs.csv', 'w', newline='') as csvfile:
	#     spamwriter = csv.writer(csvfile, delimiter=' ',
	#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
	#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
	#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

if __name__ == '__main__':
    app.run(main)




    # https://docs.python.org/3/library/csv.html
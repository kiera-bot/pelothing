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
            if workout_data:
                writer.writerow(workout_data)

if __name__ == '__main__':
    app.run(main)

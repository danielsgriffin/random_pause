"""For use in Pythonista. Generate a reminder w/ alarm that will go off in a
random # of minutes.

Built from code here:
http://omz-software.com/pythonista/docs/ios/reminders.html

Inspiration:
Lately thinking about how I need more complete pauses w/o distractions. So
here is a variable length pause for me to simply pause.
(also I've been wanting to play around w/ Pythonista)
"""

# Imports
import reminders
import datetime
import random

# Body
r = reminders.Reminder()
r.title = 'Mandated Random Pause.'
max_minutes = 6
minutes = random.randint(1, max_minutes)
due = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
# Note: We're setting the due date to the same time as the alarm here,
# but they can also be different.
r.due_date = due
a = reminders.Alarm()
a.date = due
r.alarms = [a]
r.notes = 'for {} minutes'.format(minutes)
r.save()

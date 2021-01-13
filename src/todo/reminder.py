from plyer import notification
import datetime
from .models import task


def alert(request, id):
	task_time = datetime.timedelta(minutes=30)
	if 'start_date' == 'end_date' and - 3000: 
		notification.notify(
			title = "MFAIC TODO APP",
			message = "Hello, there is an upcoming event " + str(task.task),
			timeout = 10
		)
reminder = alert(notification, id)

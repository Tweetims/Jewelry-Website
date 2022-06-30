from datetime import datetime, timedelta
from calendar import HTMLCalendar
from apps.home.models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(event_date__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.name} </li>'

		if day != 0:
			if d:
				return f"<td><span class='date p-1'><a href='' class='active'>{day}</a></span></td>"
			return f"<td><span class='date'>{day}</span></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(event_date__year=self.year, event_date__month=self.month)

		cal = f'<table class="calendar"><div class="front">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		cal += f'</div></table>'
		return cal
from datetime import datetime
from dateutil.relativedelta import relativedelta

from calendar import HTMLCalendar
from apps.home.models import Course


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter courses by day
	def formatday(self, day, courses):
		courses_per_day = courses.filter(course_date__day=day)
		d = ''
		for course in courses_per_day:
			d += f'<li> {course.name} </li>'

		if day != 0:
			if d:
				return f"<td><span class='date active'><a href='' class='active'>{day}</a></span></td>"
			return f"<td><span class='date'>{day}</span></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, courses):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, courses)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter courses by year and month
	def formatmonth(self, withyear=True):
		courses = Course.objects.filter(course_date__year=self.year, course_date__month=self.month)
  
		ref_date = datetime(self.year, self.month, 1)
		fwd_date = ref_date
		bkw_date = ref_date
		fwd_date += relativedelta(months=+1)
		bkw_date += relativedelta(months=-1)
  
		# TODO: extend calendar class to more properly handle this chunk of code

		cal = f'<table class="calendar"><tbody><div class="icon month prev"><a href="/courses/{bkw_date.year}/{bkw_date.strftime("%B")}/"><i class="fa fa-angle-left" aria-hidden="true"></i></a></div><div class="icon month next"><a href="/courses/{fwd_date.year}/{fwd_date.strftime("%B")}/"><i class="fa fa-angle-right" aria-hidden="true"></i></a></div>\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, courses)}\n'
		padded_week = f"{self.formatweek([(0,1) for i in range(0, 7) ], courses)}\n"
		cal += f'{padded_week}</tbody></table>'
		return cal
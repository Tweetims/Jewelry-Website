import datetime
from dateutil.relativedelta import relativedelta

from calendar import HTMLCalendar
from apps.home.models import Course
import calendar


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
            d += f"<a href='/courses/view/{course.id}/' class='active'>{course.name}</a>"

        if day != 0:
            if d:
                # either button to open pop up or pictures in calendar days
                return f"<td><span class='date active'>{day}{d}</span></td>"
            return f"<td><span class='date'>{day}</span></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, courses):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, courses)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter courses by year and month
    def get_month(self):
        course_data = {}
        courses = Course.objects.filter(course_date__year=self.year, course_date__month=self.month)
        for course in courses:
            if not course_data.get(course.course_date.day):
                course_data[course.course_date.day] = []
            course_data[course.course_date.day].append({
                'id': course.id,
                'name': course.name
            })

        ref_date = datetime.datetime(self.year, self.month, 1)
        fwd_date = ref_date
        bkw_date = ref_date
        fwd_date += relativedelta(months=+1)
        bkw_date += relativedelta(months=-1)

        # TODO: extend calendar class to more properly handle this chunk of code
        # this is extremely slow
        cal_info = calendar.monthcalendar(self.year, self.month)
        cal_month = []
        for i in range(len(cal_info)):
            cal_week = []
            for j in range(len(cal_info[i])):
                if cal_info[i][j] == 0:
                    cal_week.append({'day': -1, 'courses': []})
                    continue
                day = {'day': cal_info[i][j], 'courses': []}
                if day['day'] in course_data:
                    for course in course_data[day['day']]:
                        day['courses'].append({'id': course['id'], 'name': course['name']})
                cal_week.append(day)
            cal_month.append(cal_week)
        self.formatweekheader()
        cal = {
            'prev': f'{bkw_date.year}/{bkw_date.strftime("%B")}/',
            'next': f'{fwd_date.year}/{fwd_date.strftime("%B")}/',
            'calendar': cal_month
        }
        return cal

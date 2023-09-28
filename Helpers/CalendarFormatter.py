import tkcalendar as tkc
import calendar


class MyCalendar(tkc.Calendar):
    def __init__(self, master=None, allowed_weekdays=(calendar.MONDAY,), **kw):
        self._select_only = allowed_weekdays
        tkc.Calendar.__init__(self, master, **kw)
        if self._sel_date and not (self._sel_date.isoweekday() - 1) in allowed_weekdays:
            year, week, wday = self._sel_date.isocalendar()
            next_wday = max(allowed_weekdays, key=lambda d: (d - wday + 1) > 0) + 1
            sel_date = self.date.fromisocalendar(year, week + int(next_wday < wday), next_wday)
            self.selection_set(sel_date)

    def _display_calendar(self):
        tkc.Calendar._display_calendar(self)
        for i in range(6):
            for j in range(7):
                if j in self._select_only:
                    continue
                self._calendar[i][j].state(['disabled'])

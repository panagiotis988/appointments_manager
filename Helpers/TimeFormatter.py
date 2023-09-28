import pandas as pd
import tkinter as tk


class TimeFormatter:
    @staticmethod
    def format(start, end, freq, formatter):
        time_list = []
        reversed_list = []

        timeLapses = pd.date_range(start, end, freq=str(freq) + 'min').strftime(formatter)

        for timeLapse in timeLapses:
            time_list.append(str(timeLapse))

        last_item = time_list.pop()
        reversed_list.insert(0, last_item)
        reversed_list.extend(time_list)
        reversed_list.pop(1)
        start_time_init = tk.StringVar()
        start_time_init.set('07:00')
        end_time_init = tk.StringVar()
        end_time_init.set('20:00')

        return {'time_list': time_list, 'reversed_list': reversed_list, 'start_init': start_time_init,
                'end_init': end_time_init}

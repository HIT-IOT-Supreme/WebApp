# -*- coding: utf-8 -*-
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import ConflictingIdError
from .pusher import push_weather, push_zhihu

# import app.apiv1.auth as auth 待解决的循环导入冲突问题


class Timer():

    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.actions = []
        self.is_reading = False
        # self.clock_set = map(lambda a:a['time'], auth.get_clocks())

    def start(self):
        self.scheduler.start()

    def add_timer(self, time):
        today = str(datetime.now()).split()[0]
        dtstr = today + ' ' + time
        print dtstr
        try:
            self.scheduler.add_job(self.action, 'interval', args=(dtstr,), id=dtstr,
                              next_run_time=datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S"), max_instances=1)
        except ConflictingIdError:
            pass

    def read_on(self):

        if not self.action:
            self.is_reading = False
            return

        self.is_reading = True
        func = self.actions.pop(0)
        func()

    def action(self, id):
        print('Tick! The time is: %s' % datetime.now())
        self.actions.extend([push_weather, push_zhihu])
        if not self.is_reading:
            self.read_on()

        self.scheduler.remove_job(job_id=id)


if __name__ == '__main__':
    timer = Timer()
    timer.start()

    while 1:
        pass






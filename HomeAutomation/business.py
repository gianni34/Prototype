# Aca tengo que refactorizar todos los metodos que tengo dispersos por clases incorrectas
# y ponerlos aca como logica de negocio

from HomeAutomation.models import *
import datetime
import sched
import time
import threading

s = sched.scheduler(time.time, time.sleep)


class Main:
    @staticmethod
    def is_execution_day(i):
        scene = Scene.objects.filter(id=i).first()
        string_days = scene.days
        days = string_days.split(',')
        days = list(map(int, days))
        for d in days:
            if d == datetime.datetime.now().weekday():
                return True
        return False

    @staticmethod
    def is_execution_time(i):
        scene = Scene.objects.filter(id=i).first()
        now = datetime.datetime.now().time()
        if scene.time <= now <= scene.end_time:
            return True
        else:
            return False

    @staticmethod
    def auto_execution_scene():
        print("Entro al Auto Execution Scene")
        scenes = Scene.objects.all()
        for s in scenes:
            if s.time_condition:
                if Main.is_execution_day(s.id):
                    now = datetime.datetime.now()
                    if s.time.hour == now.hour:
                        if s.time.minute == now.minute:
                            if not s.executed:
                                s.execute_scene()
            elif s.value_condition:
                if Main.is_execution_day(s.id) and Main.is_execution_time(s.id):
                    zone = s.zone
                    if zone.temperature > int(s.value):
                        print("Temperatura de la zona mayor al valor de escena")
                        if not s.executed:
                            s.execute_scene()

    @staticmethod
    def change_executed_scene():
        scenes = Scene.objects.filter(value_condition=True).all()
        for s in scenes:
            if s.executed:
                if not (Main.is_execution_day(s.id) and Main.is_execution_time(s.id)):
                    s.change_executed(False)

    @staticmethod
    def delete_actions(i):
        actions = SceneAction.objects.filter(scene=i).all()
        if actions:
            for a in actions:
                SceneAction.delete(a)


class ThreadScheduler(object):

    def __init__(self, interval=60):
        print("Inicializo el Hilo")
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            print("While True de RUN")
            s.enter(60, 1, Main.auto_execution_scene)
            s.enter(360, 1, Main.change_executed_scene)
            s.run()

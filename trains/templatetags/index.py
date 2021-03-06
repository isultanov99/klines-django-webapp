from datetime import datetime

from django import template

from trains.models import *

register = template.Library()


@register.filter
def index(indexable, i: int):
    return indexable[i]


@register.filter
def indexone(indexable, i: int):
    return indexable[i - 1]


@register.filter
def get_name(station: Station.objects.all(), key: int):
    return station[int(key) - 1].name


@register.filter
def get_slug(station: Station.objects.all(), key: int):
    return station[int(key) - 1].slug


@register.simple_tag
def keys_to_list(d):
    return list(d.keys())


@register.simple_tag
def same_line(st1, st2):
    return any(i in [line.name for line in st1.line.all()] for i in [line.name for line in st2.line.all()])


@register.simple_tag
def sov_svet(st1, st2):
    return any(set([line.id for line in st1.line.all()]) & set([1, 6]) and
               set([line.id for line in st2.line.all()]) & set([1, 6]))


@register.simple_tag
def sov_zel(st1, st2):
    return any(set([line.id for line in st1.line.all()]) & set([1, 7]) and
               set([line.id for line in st2.line.all()]) & set([1, 7]))


@register.simple_tag
def svet_zel(st1, st2):
    return (st1.id == 76 or st1.id == 75 or 6 in [line.id for line in st1.line.all()] and 7 not in [line.id for line in st1.line.all()]) and any(set([line.id for line in st2.line.all()]) & set([7]))


@register.simple_tag
def time_delta(time1, time2):
    t1 = datetime.strptime(time1, "%H:%M")
    t2 = datetime.strptime(time2, "%H:%M")
    return int((t2 - t1).seconds / 60)


@register.simple_tag
def find_train(st1, st2=None):
    if not st2:
        return [i for i in (Train.objects.filter(line__in=[line.id for line in st1.line.all()])) if
                str(st1.id) in i.timetable.values() and st1 != i.to_station]
    else:
        return [i for i in (Train.objects.filter(line__in=list(
            set([line.id for line in st1.line.all()]).intersection([line.id for line in st2.line.all()]))))
                if
                str(st1.id) in i.timetable.values() and
                str(st2.id) in i.timetable.values()
                and
                list(i.timetable.keys())[list(i.timetable.values()).index(str(st1.id))] <
                list(i.timetable.keys())[list(i.timetable.values()).index(str(st2.id))]]


@register.simple_tag
def station_time(st, tr):
    return list(tr.timetable.keys())[list(tr.timetable.values()).index(str(st.id))]


@register.simple_tag
def today(days):
    return (datetime.today().weekday() + 1) in days


@register.simple_tag
def get_station(n):
    return Station.objects.get(id=n)


@register.simple_tag
def day_color(num):
    if datetime.today().weekday() + 1 == num:
        return True
    return False

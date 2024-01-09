from icalendar import Calendar, Event, Alarm
from datetime import *
from dateutil.rrule import rrule, WEEKLY


def generate_classes(data):
    classes = set()
    for i in data:
        for j in i:
            x = j.split("-")
            if len(x) == 5:
                if x[0][0] == "L":
                    if int(x[0][1]) % 2 == 1:
                        classes.add(j)
                else:
                    classes.add(j)
    return classes

def generate_ical(classes):
    slots = {
        'A1': [('MO', '08:00'), ('WE', '09:00')],
        'B1': [('TU', '08:00'), ('TH', '09:00')],
        'C1': [('WE', '08:00'), ('FR', '09:00')], 
        'D1': [('MO', '10:00'), ('TH', '08:00')],
        'E1': [('TU', '10:00'), ('FR', '08:00')],
        'F1': [('MO', '09:00'), ('WE', '10:00')], 
        'G1': [('TU', '09:00'), ('TH', '10:00')],
        'TA1': [('FR', '10:00')],
        'TB1': [('MO', '11:00')],
        'TC1': [('TU', '11:00')], 
        'TD1': [('FR', '12:00')],
        'TE1': [('TH', '11:00')],
        'TF1': [('FR', '11:00')],
        'TG1': [('MO', '12:00')],
        'TAA1': [('TU', '12:00')],
        'TCC1': [('TH', '12:00')],
        'A2': [('MO', '14:00'), ('WE', '15:00')],
        'B2': [('TU', '14:00'), ('TH', '15:00')],
        'C2': [('WE', '14:00'), ('FR', '15:00')],
        'D2': [('MO', '16:00'), ('TH', '14:00')], 
        'E2': [('TU', '16:00'), ('FR', '14:00')],
        'F2': [('MO', '15:00'), ('WE', '16:00')],
        'G2': [('TU', '15:00'), ('TH', '16:00')],
        'TA2': [('FR', '16:00')],
        'TB2': [('MO', '17:00')],
        'TC2': [('TU', '17:00')],
        'TD2': [('WE', '17:00')],
        'TE2': [('TH', '17:00')], 
        'TF2': [('FR', '17:00')],
        'TG2': [('MO', '18:00')],
        'TAA2': [('TU', '18:00')],
        'TBB2': [('WE', '18:00')],
        'TCC2': [('TH', '18:00')],
        'TDD2': [('FR', '18:00')],
        'L1': [('MO', '8:00')], 'L3': [('MO', '9:50')], 'L5': [('MO', '11:40')], 'L7': [('TU', '8:00')], 'L9': [('TU', '9:50')], 'L11': [('TU', '11:40')], 'L13': [('WE', '8:00')], 'L15': [('WE', '9:50')], 'L17': [('WE', '11:40')], 'L19': [('TH', '8:00')], 'L21': [('TH', '9:50')], 'L23': [('TH', '11:40')], 'L25': [('FR', '8:00')], 'L27': [('FR', '9:50')], 'L29': [('FR', '11:40')], 'L31': [('MO', '14:00')], 'L33': [('MO', '15:50')], 'L35': [('MO', '17:40')], 'L37': [('TU', '14:00')], 'L39': [('TU', '15:50')], 'L41': [('TU', '17:40')], 'L43': ('WE', '14:00'), 'L45': [('WE', '15:50')], 'L47': [('WE', '17:40')], 'L49': [('TH', '14:00')], 'L51': [('TH', '15:50')], 'L53': [('TH', '17:40')], 'L55': [('FR', '14:00')], 'L57': [('FR', '15:50')], 'L59': [('FR', '17:40')]
    }
    
    days = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4}

    cal = Calendar()

    for _class in classes:
        _class = _class.split("-")
        slot, course, room = _class[0], _class[1], _class[3]
        slts = slots[slot]
        for x in slts:
            t = list(map(int, x[1].split(":")))
            event = Event()
            event.add('summary', course + "-" + room)
            day = datetime(2024, 1, 1).weekday() + days[x[0]] + 1
            event.add('dtstart', datetime(2024, 1, day, t[0], t[1]))
            if _class[2] == "LO" or _class[2] == "ELA":
                event.add('dtend', datetime(2024, 1, day, t[0], t[1]) + timedelta(hours=1, minutes=40))
            else:
                event.add('dtend', datetime(2024, 1, day, t[0], t[1]) + timedelta(minutes=50))
            event.add('rrule', {'freq': 'weekly', 'byday': x[0] , 'wkst': x[0], 'until': datetime(2024, 5, 20)})
            cal.add_component(event)

    file = open('calendar.ical', 'w')
    file.write(cal.to_ical().decode("utf-8"))
    file.close()


if __name__ == "__main__":
    import sys
    import csv
    input_file = sys.argv[1]
    with open("TimeTable.csv", 'r') as file:
        csvfile = csv.reader(file)
        data = []
        for row in csvfile:
            data.append(row)
    data = data[4:-4]
    classes = generate_classes(data)
    generate_ical(classes)
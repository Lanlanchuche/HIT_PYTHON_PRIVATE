
def create_event(name:str, day:str, time:str):
    event = {}
    event["name"] = name
    event["day"] = day
    event["time"] = time
    return event

def add_event(schedule:list, event:dict):
    schedule.append(event)

def find_by_day(schedule, day):
    for event in schedule:
        if event["day"] == day:
            return event
    return None

def remove_event(schedule, name):
    for event in schedule:
        if event["name"] == name:
            schedule.remove(event)
            return True
    return False

def export_schedule(schedule):
    for event in schedule:
        print(f"{event['day']}  {event['time']} - {event['name']}")

schedule = []
event1 = create_event("Math", "Mon", "07:00")
event2 = create_event("Physics", "Tue", "09:00")
event3 = create_event("English", "Thu", "07:30")
add_event(schedule, event1)
add_event(schedule, event2)
add_event(schedule, event3)

day = input("Enter day to search: ")
if find_by_day(schedule, day) == None:
    print("Not found")
else:
    print(find_by_day(schedule, day))

name = input("Enter name to remove: ")
if remove_event(schedule, name) == True:
    print("Succesfully removed")
else:
    print("Fail to remove")

export_schedule(schedule)


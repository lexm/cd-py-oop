import itertools

class Call(object):
    next_id = itertools.count().next
    def __init__(self,name,phone,call_time,reason):
        self.id = Call.next_id()
        self.name = name
        self.phone = phone
        self.call_time = call_time
        self.reason = reason
    def display(self):
        print "ID:", self.id
        print "Caller Name:", self.name
        print "Caller Phone Number:", self.phone
        print "Call Time:", self.call_time
        print "Reason for Call:", self.reason
        print
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self,name,phone,call_time,reason):
        self.calls.append(Call(name,phone,call_time,reason))
        return self
    def remove(self):
        return self.calls.pop(0)
    def info(self):
        for call in self.calls:
            print "Name:", call.name
            print "Phone:", call.phone
        print "Queue length:", len(self.calls)
        return self
        

center = CallCenter()
center.add("Fred","555-1212","12:43pm","Wrong number")
center.add("Amie","123-456-7890","3:15pm","Broken spigot needs fixing")
center.add("Doug","890-567-1234","9:45am","Blowing off steam")
center.remove()
center.info()

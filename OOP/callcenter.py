class Call(object):

    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
        # self.__str__()
    
    def __str__(self):
        # print "Unique ID: " + str(self.unique_id)
        # print "Caller Name: " + str(self.caller_name)
        # print "Caller Phone Number: " + str(self.caller_phone_number)
        # print "Time of call: " + str(self.time_of_call)
        # print "Reason for call: " + str(self.reason_for_call)
        return str(self.unique_id) + " Caller Name: " + str(self.caller_name) + " Caller Phone Number: " + str(self.caller_phone_number) + " Time of call: " + str(self.time_of_call) + " Reason for call: " + str(self.reason_for_call)

callone = Call(123, "bob", 408971, "14:20", "cancellation")
calltwo = Call(456, "mike", 789123, "12:10", "refund")
# callone.display()

class CallCenter(object):

    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    
    def add(self, newcall):
        # self.newcall = newcall
        self.calls.append(newcall)
        print self.calls
        return self

    def remove(self):
        if self.queue_size > 0:
            self.calls.pop[0]
        return self
    
    def info(self):
        for call in self.calls:
            print str(call)
        return self

callcenterone = CallCenter()
callcenterone.add(callone).info()
callcenterone.add(calltwo).info()
    
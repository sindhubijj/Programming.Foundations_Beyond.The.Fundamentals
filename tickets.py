#CLASSES AND METHODS
class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets): #constructor function
        self.name = name
        self.tickets = tickets

    def displayAttendee(self): #displayAttendee is a method
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))
            #printing the values for 'name' and 'tickets' for the current object

    def addTicket(self): #addTicket is another method
        self.tickets += 1 #increase ticket count by 1 that are assigned to an attendee
        print('{} tickets increased to {}'.format(self.name, self.tickets))

attendee1 = Attendee('A. Pierre', 1) #variable = class ([arg 1], [arg 2])
attendee2 = Attendee('K. Harrison Jr.', 2)

#Results
attendee1.displayAttendee() #Variable 1 Result: storing two properties using 'name' and 'tickets'
attendee2.displayAttendee() #Variable 2 Result: different name and property values, but shares methods

#Using Method 2 - Attendee 2 wants to add tickets
attendee2.addTicket()
attendee2.addTicket()

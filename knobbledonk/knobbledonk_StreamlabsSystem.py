ScriptName = "Donk or Knobble"
Website = "https://www.thedanives.com"
Description = "Detects votes of donks or knobbles"
Creator = "Dan"
Version = "0.5"

class VoteData:
    donks = 0
    knobbles = 0
    userlog = {}

def Init():
    return

def Execute(data):
    if data.IsChatMessage():
        # Check if the user is making a vote
        i = 0
        vote = None
        params = data.GetParamCount()
        while i < params:
            string = data.GetParam(i).lower()
            if (vote != None and (string == 'donk' or string == 'knobble')):
                # They have said both, so NONE for them
                Parent.SendStreamMessage("%s you can't make multiple votes!!" % data.UserName)
                vote = None
                i = params
            elif (string == 'donk'):
                vote = 'donk'
            elif (string == 'knobble'):
                vote = 'knobble';
            i += 1
        
        if (vote == None):
            return

        # Check if the user has already made a vote
        ident = data.UserName

        if ident in VoteData.userlog:
            if VoteData.userlog[ident] == 'donk' and vote == 'knobble':
                VoteData.donks -= 1
                VoteData.knobbles += 1
            elif VoteData.userlog[ident] == 'knobble' and vote == 'donk':
                VoteData.donks += 1
                VoteData.knobbles -= 1
        else:
            if vote == 'donk':
                VoteData.donks += 1
            else:
                VoteData.knobbles += 1

        VoteData.userlog[ident] = vote
        Parent.BroadcastWsEvent("EVENT_DK_VOTES", '{"donks":%d, "knobbles":%d}' % (VoteData.donks, VoteData.knobbles))

    return

def Tick():
    return


def ResetVotes():
    Parent.SendStreamMessage("Total Donks: %d" % VoteData.donks)
    Parent.SendStreamMessage("Total Knobbles: %d" % VoteData.knobbles)
    VoteData.donks = 0
    VoteData.knobbles = 0
    VoteData.userlog = {}
    Parent.SendStreamMessage("== Votes Begin Here ==")
    Parent.BroadcastWsEvent("EVENT_DK_VOTES", '{"donks":0, "knobbles":0}')
    return

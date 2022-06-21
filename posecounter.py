import json
import raisedhandsmodule

print("starting counting")
with open("allposes_labeled.json") as f:
	data = json.load(f)

raisedhands = 0
nonraisedhands = 0	
for element in data:
        if element["raisedhand"] == 1:
        	raisedhands+= 1
        elif element["raisedhand"] == 0:
        	nonraisedhands+= 1

        	
print(".json has following info: raised hands: " + str(raisedhands) + " and non raised hands: " + str(nonraisedhands))



truenegative=0
falsenegative=0
truepositive=0
falsepositive=0


elementcounter = 0
for element in data:
                raised_hands_counter = 0
                if raisedhandsmodule.wrist_above_nose(data,elementcounter):
               		raised_hands_counter += 1
                elif raisedhandsmodule.wrist_above_shoulders(data,elementcounter):
               		raised_hands_counter += 1
                elif raisedhandsmodule.hand_pointing_up(data,elementcounter):
               		raised_hands_counter += 1

                if raised_hands_counter == 0:
                        if element["raisedhand"] == 0:
                                truenegative = truenegative + 1
                        if element["raisedhand"] == 1:
                                falsenegative = falsenegative + 1
                if raised_hands_counter == 1:
                        if element["raisedhand"] == 1:
                                truepositive = truepositive + 1
                        if element["raisedhand"] == 0:
                                falsepositive = falsepositive + 1
                elementcounter = elementcounter + 1

print("truepositives: " + str(truepositive) + " falsepositives: " + str(falsepositive) + " truenegatives " + str(truenegative) + " falsenegatives " + str(falsenegative))

accuracy = ((truepositive + truenegative)) / ( truepositive + truenegative + falsepositive + falsenegative)
print("accuracy ", accuracy)
                        

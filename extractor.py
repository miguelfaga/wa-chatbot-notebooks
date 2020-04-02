from datetime import datetime

class LogObject:
    def __init__(self, log_object):
        if "conversation_id" in log_object["response"]["context"]:
            self.conversation_id = log_object["response"]["context"]["conversation_id"]
        else:
            self.conversation_id = "null"
        self.turn_counter = log_object["response"]["context"]["system"]["dialog_turn_counter"]
        self.response_timestamp = datetime.strptime(log_object["response_timestamp"][0:19], "%Y-%m-%dT%H:%M:%S")
        if "input" in log_object["request"]:
            if "text" in log_object["request"]["input"]:
                self.user_input = log_object["request"]["input"]["text"]
            else:
                self.user_input = "No input"
        else:
            self.user_input = "No input"
        if len(log_object["response"]["intents"]) > 0:
            self.intent = log_object["response"]["intents"][0]["intent"]
            self.confidence = float(log_object["response"]["intents"][0]["confidence"])
        else:
            self.intent = "Irrelevant"
            self.confidence = None
        if len(log_object["response"]["entities"]) > 0:
            self.entities = [log_object["response"]["entities"][i]["entity"] + ":" + log_object["response"]["entities"][i]["value"] for i in range(len(log_object["response"]["entities"]))]
        else:
            self.entities = ["No entity"]
        if len(log_object["response"]["output"]["text"]) > 0:
            self.botmessage = log_object["response"]["output"]["text"][0]
        else:
            self.botmessage = "No response"
        self.log_id = log_object["log_id"]

def extractor_list(log_object):
    log = LogObject(log_object)
    return [
        log.conversation_id, 
        log.turn_counter, 
        log.response_timestamp.strftime("%Y-%m-%d"),
        log.response_timestamp.strftime("%H:%M:%S"), 
        log.user_input, 
        log.intent, 
        log.confidence, 
        ", ".join(log.entities), 
        log.botmessage, 
        log.log_id
        ]
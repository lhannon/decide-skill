from mycroft import MycroftSkill, intent_file_handler


class Decide(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('decide.intent')
    def handle_decide(self, message):
        self.speak_dialog('decide')


def create_skill():
    return Decide()


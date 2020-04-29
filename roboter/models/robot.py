#TODO: ranking model
from roboter.views import console


DEFAULT_ROBOT_NAME = 'Roboko'


class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({'robot_name': self.name}))
            if user_name:
                self.user_name = user_name.title()
                break


class RestrantRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name=name)
        # TODO: ranking model

    def _hello_decorator(func):
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def recommend_restrant(self):
        # TODO: ranking model

    @_hello_decorator
    def ask_user_favorite(self):
        while True:
            template = console.get_template('which_restrant.txt', self.speak_color)
            restrant = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
            }))
            if restrant:
                # TODO: ranking model
                break

    @_hello_decorator
    def thank_you(self):
        template = console.get_template('good_by.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name,
        }))

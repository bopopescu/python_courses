"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""

from flask import request, redirect, flash
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        all_courses = self.models['Course'].get_all_courses()
      
        return self.load_view('index.html', courses=all_courses)

    def create(self):
        course_details = {
            'name': request.form['name'],
            'description': request.form['description']

        }


        self.models['Course'].add_course(course_details)

        return redirect('/')

    def show_confirm(self, id):
        one_course = self.models['Course'].get_course_by_id(id)
        return self.load_view('show.html', course=one_course[0])

    def destroy(self, id):
        self.models['Course'].destroy(id)
        return redirect('/')











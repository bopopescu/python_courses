""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """

    def add_course(self, course_details):
        insert_query = "INSERT INTO courses (name, description, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(course_details['name'], course_details['description'])

        return self.db.query_db(insert_query)




    def get_all_courses(self):
        get_all_query = "SELECT * FROM courses"
        return self.db.query_db(get_all_query)

    def get_course_by_id(self, course_id):
        get_one_query = "SELECT * FROM courses WHERE id = {}".format(course_id)
        return self.db.query_db(get_one_query)

    def destroy(self, id):
        delete_one_query = "DELETE FROM courses WHERE id ={}".format(id)
        return self.db.query_db(delete_one_query) 














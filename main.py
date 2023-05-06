import cherrypy

from server.app import App


def init_db():
    from server.models import db, People
    db.connect()
    db.create_tables([People])


# cherrypy.engine.subscribe("before_request", init_db)

# print(cherrypy.engine.listeners)

cherrypy.quickstart(App(), "/")

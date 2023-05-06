import cherrypy

from .models import People


class App:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        ps = People.select()
        return [{"name": p.name, "age": p.age, "created_at": p.created_at} for p in ps] or "index"

    @cherrypy.expose
    def create(self, name, age):
        p = People(name=name, age=int(age))
        p.save()
        return p.name

    @cherrypy.expose
    def ten_item(self):
        # 10个题的信息
        pass

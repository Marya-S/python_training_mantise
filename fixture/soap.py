from suds.client import Client
from suds import WebFault


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def get_project_list_soap(self,username="administrator", password="root"):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
            return project_list
        except WebFault:
            return False

    def add_project(self,project, username="administrator", password="root"):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_projects_get_user_accessible(username, password, project)
        except WebFault:
            return False

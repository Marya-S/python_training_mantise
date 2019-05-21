from model.project import Project
import random

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project(self, project):
        wd = self.app.wd
        wd.find_element_by_name('name').click()
        wd.find_element_by_name('name').clear()
        wd.find_element_by_name('name').send_keys(project.name)
        wd.find_element_by_name('description').click()
        wd.find_element_by_name('description').clear()
        wd.find_element_by_name('description').send_keys(project.description)

    def add_new_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_list = None


    project_list = None

    def get_project_list(self):
        if self.project_list is None:
            wd = self.app.wd
            self.open_project_page()
            project_list=[]
            for element in (wd.find_elements_by_xpath("//table[3]/tbody/tr"))[1:]:
                name = element.find_element_by_xpath('.//td[1]/a').text
                description = element.find_element_by_xpath(".//td[5]").text
                project_list.append(Project(projectname=name, description=description))
        return project_list

    def delete(self, project_list):
        wd = self.app.wd
        delete_project = project_list[0]
        wd.find_element_by_link_text(delete_project.name).click()
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()





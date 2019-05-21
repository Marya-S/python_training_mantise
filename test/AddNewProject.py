from model.project import Project
import time
import random


def test_add_project(app):
    old_projects = app.project.get_project_list()
    random_str = str(random.randint(0, 1000))
    project = Project(projectname="NewProjectTest" + random_str, description="Я создан автотестом")
    app.project.add_new_project(project)
    time.sleep(5)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda project: project.name) == sorted(new_projects, key=lambda project: project.name)
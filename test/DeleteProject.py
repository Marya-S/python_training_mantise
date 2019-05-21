import time
from model.project import Project


def test_delete_project(app):
    if app.project.get_project_list() == 0:
        app.project.add_new_project(
            Project(projectname="NewDelTest", description="Я создан для удаления"))
    old_projects = app.project.get_project_list()[1:]
    app.project.delete(old_projects)
    time.sleep(3)
    new_projects = app.project.get_project_list()[1:]
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[0:1] = []
    assert sorted(old_projects, key=lambda project: project.name) == sorted(new_projects,
                                                                            key=lambda project: project.name)

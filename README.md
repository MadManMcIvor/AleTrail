
# AleTrail

## Members
* Ryan Spurlock
* Alex Mclvor
* Justin Thomas
* Julie Liao


# Module3 Project Gamma

## Getting started

You have a project repository, now what? The next section lists all of the deliverables that are due at the end of the week. Below is some guidance for getting started on the tasks for this week.

## Deliverables
- [x] Wire-frame diagrams
- [x] API documentation
- [ ] Project is deployed to Heroku/GitLab-pages
- [ ] GitLab issue board is setup and in use

## Project layout

The layout of the project is just like all of the projects you did with `docker-compose` in module #2. You will create a directory in the root of the repository for each service that you add to your project just like those previous projects were setup.

### Directories

Several directories have been added to your project. The directories `docs` and `journals` are places for you and your team-mates to, respectively, put any documentation about your project that you create and to put your project-journal entries. See the README file in each directory for more info.

The other directories, `ghi` and `sample_service`, are sample services, that you can start building off of or use as a reference point.

Inside of `ghi` is a minimal React app that has an "under construction" page. It is setup similarly to all of the other React projects that you have worked on.

Inside of `sample_service` is a minimal FastAPI application. "Where are all the files?" you might ask? Well, the `main.py` file is the whole thing, and go take look inside of it... There's not even much in there..., hmm? That is FastAPI, we'll learn more about it in the coming days. Can you figure out what this little web-application does even though you haven't learned about FastAPI yet?

### Other files

The following project files have created as a minimal starting point. Please follow the guidance for each one for a most successful project.

- `docker-compose.yaml`: there isn't much in here, just a **really** simple UI. Add services to this file as you did with previous projects in module #2.
- `.gitlab-ci.yml`: This is your "ci/cd" file where you will configure
  automated unit tests, code quality checks, and the building and deployment
  of your production system. Currently, all it does is deploy an
  "under construction" page to your production UI on GitLab. We will learn
  much more about this file
- `.gitignore`: don't keep track of things you don't need to like
  `node_modules`, `__pycache__`, etc.

## How to complete the initial deploy

There will be further guidance on completing the initial deployment, but it just consists of these steps:

- setup Heroku account and app
- setup 2 CI/CD variables in GitLab
- push to main

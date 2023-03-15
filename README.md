![Fodmap recipes]()

# Welcome to Fodmap recipes!
#### This is a site that provides Fodmap diet recipes. 

The site should be both inspiering and informative and make it easy to find tasty recipes. The site provides the user the oportunity to easy register an account. When logged in the user can upload their own recipe posts on the site (which the user then can update/edit/delete), comment and like other recipes and also watch their own liked/favourite recipes. If the user prefers not to register an account they can still look at the recipes uploaded and the About Fodmap site is open to all users. The site provides healthy recipes beneficial to all users and ages, and weather you follow the Fodmap diet or not.

#### [Deployed site](https://fodmap-recipes.herokuapp.com/)
------


## Table of contents

[UX](#ux)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Agile Methodology](#agile-methodology)

[Existing Features](#existing-features)

- [Navbar](#navbar)
- [Home Page](#home-page)
- [Recipe details](#recipe-details)
- [About Fodmap](#about-fodmap)
- [Register](#register)
- [Signin](#signin)
- [Signout](#signout)
- [Footer](#footer)
- [Cloudinary API](#cloudinary-api)
- [Form and code validation](#form-and-code-validation)

[Technologies Used](#technologies-used)

- [Languages Used](#language-used)
- [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)
- [Database](#database-model-structure)

[Tests](#tests)

- [Automated Tests](#automated-tests)
- [Lighthouse](#lighthouse)

[Deployment](#deployment)

- [Deployment to heroku](#deployment-to-heroku)
- [Setting up local enviroment](#setting-up-local-environment)

[Credit](#credits)

- [Online resources](#online-resources)
- [Tutorials and inspiration](#tutorials-and-inspiration)
- [People](#people)

## UX

------

### User Stories

GitHub issues were used to record the user stories. The user stories were categorised into different priorities.

![User Stories Screenshot](media/user_stories.png)

### Wireframes

Wireframes

#### Mobile and Desktop device

![wireframe mobile and desktop device]()

##### Detail page

![Wireframe detail page]()

##### User register view

![Wireframe user register view]()

##### User create post view

![Wireframe user create post]()

### Agile Methodology

Github issues were used to create the User stories and acceptance criteria. Link to the project with live issues can be found [here](https://github.com/users/Karasp1980/projects/7).  

## Existing Features

------

### Navbar
The navbar 

![Navbar]()

### Home Page

The home page consists of a welcome hero image with a yellow clear login/register button (or when already logged in, a logout button). The hero image should be inviting.

![home page image]()

The next part of the home page is the recipe blog section, showing the latest 6 blog posts entered (the last post in the upper left corner). The blog post showing consists of an image (if no image is not uploaded by the post creator a placeholder image is displayed) as well as the number of comments and likes and the date the post is published on.

![]()

### Recipe details

The recipe details page consists of the recipe uploaded by the user displaying the title/image uploaded (if not a placeholder image, which is the same image as the hero image on the home page), description, ingredients and preparation steps. 1

### About Fodmap
The About Fodmap shoud be an informative site about the Fodmap diet. It consists of a presentation what Fodmaps are and why the diet could be beneficial when having IBS and sensitive stomach, with the same style as the welcome section on the home page. It then consists of two fileds with Low Fodmap and High Fodmap grocerys, the first in green to aware the user that this is the grocerys to choose, and the High Fodmap grocerys in red to implicit that these foods should be avoided.

### Register
The user could register for an account by register a username, email (optional) and password

### Sign in
When having registered an account the user could easily login byt entering username and password.

### Sign out
The signout page has the same style as the sign in page.

### Footer
The footer  

![Navbar]()

### Cloudinary API

For images the cloud based API Cloudinary is used. When a user uploads an image, it is saved in Cloudinary.

### Form and code Validation

Form Validation

1. HTML validation using HTML attribute
2. CSS Validation
3. Javascript validation
4. Django form validation

## 1. HTML Validation

![HTML Validation](https://validator.w3.org/nu/#textarea)
| File Name | Result |
| ------ | ------ |
| base.html | ![no error](README/home.txt) |
| index.html | ![no error](README/home.txt) |
| post_detail.html | ![error found auto generated](README/Post_details.txt) |
| add.html | ![error found auto generated](README/add.txt) |
| edit.html | ![error found auto generated](README/Edit.txt) |
| delete.html | ![no error](README/Delete.txt) |
| category.html | ![no error]() |

**2. CSS Validation**
CSS file was tested by W3C css validation and everything was well. Screenshot report shows below

![W3C CSS validation report]()

**3. Javascript Validation**
This file was tested by jshint.com and everything was well.
![jshint validstion report]()

**4. Django code validation**
PEP8online.com site is not available at the moment. Its corrently down and thats why I use pycodestyle in gitpod workspace. In the django framework, python code validation complated by gitpod workspace. It shows problem at starting like "line is too long" but now it fixed.

- No error found in gitpod workspace
- anushilon2022
  - asgi.py
  - settings.py
  - urls.py
  - wsgi.py

- No error found in gitpod workspace
- rsnblog
  - admin.py
  - apps.py
  - forms.py
  - models.py
  - tests.py
  - urls.py
  - views.py
  - env.py
  - manage.py

- Procfile
- readme.md
- requirements.txt

![python code validation report](media/python_validation.png)

## Technologies Used

------

### Language Used

    - HTML 5
    - CSS 3
    - JavaScript
    - Python
    - Django

### Technologies and Program Used

    - GitHub
        The Git was used for version control
        Git issues were used for user stories
        GitPod was used as IDE to write the code and push to GitHub
    
    - Heroku
        The page was deployed to Heroku
    - PostgreSQL
        PostgreSQL was used as database for this project
    - Cloudinary storage
        Cloudinary used for storing static files
    - Allauth
        Allauth functionality used for page inloggning.

### Frameworks Libraries and Programs Used

    - Bootstrap 5
        Bootstrap was used to add style to the website.
    - Django
        This is python framework and used this project.
    - Database
        Database model schema structure added below

### Database Model Structure

![database model structure](media/models.png)

## Tests

------

### Automated tests

Automated tests already fixed on W3School, JShint and pycodetest(gitpod)

### Lighthouse

![Lighthouse general report]()

The site was run through Lighthouse in Chrome dev tools has been run. 

## Deployment

### Deployment to heroku

## In the app

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

## Log into heroku

1. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

2. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

3. Write app name - it has to be unique, it cannot be the same as this app
4. Choose Region - I am in Europe
5. Click "Create App"

**The page of project opens.**

1. Go to Resources Tab, Add-ons, search and add Heroku Postgres

2. Choose "settings" from the menu on the top of the page

3. Go to section "Config Vars" and click button "Reveal Config Vars".

4. Add the below variables to the list

    - Database URL will be added automaticaly
    - Secret_key - is the djnago secret key can be generated self
    - Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register.
    - Google API key can be obtained [here](https://cloud.google.com/gcp?authuser=1)

## Go back to code

1. Procfile needs to be created in your app

'''
web: gunicorn PROJ_NAME.wsgi
'''

1. In settings in your app add Heroku to ALLOWED_HOSTS

2. Add and commit the changes in your code and push to github

## Final step - deployment

1. Next go to "Deploy" in the menu bar on the top

2. Go to section "deployment method", choose "GitHub"

3. New section will appear "Connect to GitHub" - Search for the repository to connect to

4. type the name of your repository and click "search"

5. once Heroku finds your repository - click "connect"

6. Scroll down to the section "Mamual Deploys"

7. Click choose "Deploy branch" and manually deploy

8. Click "Deploy branch"

Once the program runs:
you should see the message "the app was sussesfully deployed"

1. Click the button "View"

### Setting up local environment

1. Create Virtual enviroment on computer or use gitpod built in virtual enviroment feature.

2. Create env.py file in the top directory. It needs to contain those variables.

- Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app.
- Secret_key - is the djnago secret key can be generated self.
- Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register.

'''
os.environ["DATABASE_URL"] = "..."
os.environ["SECRET_KEY"] = "..."
os.environ["CLOUDINARY_URL"] = "..."
'''

1. Run command

'''
pip3 install -r requirements.txt
'''

## Credits

#### Inspiration and help has also come from the Code Institute projects [Hello Django]() and [I think therefore I blog]() .

### The image used are taken from:
[Pixbay](https://pixabay.com/)
## The recipes are taken from:
[BBC good food](https://www.bbcgoodfood.com)

#### The following sites has also been helpful:
* [W3Schools](https://www.w3schools.com/) 
* [Cleveland clinic](https://my.clevelandclinic.org/health/treatments/22466-low-fodmap-diet) 
* [Monash University](https://www.monashfodmap.com) 
* [P4 News](https://github.com/mamuzaan/Portfolio-P4-News) 
* [The Healthy Family](https://github.com/Iris-Smok/The-Healthy-Family-PP4) 









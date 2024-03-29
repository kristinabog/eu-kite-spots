<h1 align="center">EU Kitespots</h1>

EU Kitespots is a website where users can look up kitesurf spots around Europe. Users can sign up and 
share their favourite kitesurf spots in Europe. The best kitesurf spots are often secret or difficult
to find on the internet. With this website kitesurfers, beginner to expert, can share their spots.

[View Live Website](https://eu-kite-spots.onrender.com) - Update 12/2022: redeployed on [Render](https://render.com
)

![Responsiveness](static/img/responsive-ms3.png)

## Table of Content

- [User Experience](#user-experience-(ux))
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


## User Experience (UX)

### User stories


  - As a First time user I want to

    1. Find an explanation of the website and about what kitesurfing is.
    2. Be able to sign up and have my own profile.
    3. Be able to look up kitesurf spots by name, region.
    4. Be able to browse kitesurf spots by country.
    5. Access the website on mobile and desktop and for it to be responsive.
    6. Find more info about a kitespot when I click on it in the list of kitespots
    7. Find info about the country and their windseason.


- As a member I want to:

    1. Be able to add my own kitesurf spots.
    2. Log in with user friendly form.
    3. Edit and delete my own kitesurf spots.
    4. Get feedback for adding, editing, logging in and logging out.
    5. Get an error messages in case I have done something wrong or there is an issue with the database.


- As an admin I want to be able:

    to access, edit and delete spots and countries from the admin profile



### Strategy
The goal of this website is so kitesurfers easily can find a website where they can find the latest popular kitesurf spots or share them.

### Scope
After looking around on the internet, you can find websites about kitesurfing in general and with popular spots around the world but nowhere
can you find a website where you can add your own and share it with other kitesurfers. This is what this website will specialize in. This way also experienced kitesurfers can share their
less touristic known spots to other kitesurfers around the world.

### Structure
Visitors are welcomed with an image to amaze them and see a kitesurfer in action. This give them the immediate idea what the website is about.
As they scroll down they will see an actual description of what the website is about and what kitesurfing is.
The log in and sign up page will have a similar clean look. There is 1 page where you can browse through all the kitesurf spots by name, region. When you click on a spot, you will be redirected to an individual page of that spot with all the info
There is also a page where you can look up spots by country.
When you click on one of the countries it will take you to a page with a brief description of the country and a all kitesurf spots in that country. 
When you sign up as a member you will be able to have a profile and a button in the navbar to add a kitesurf spot.
In the footer you will find the general navigation links. And on the left side you will find all the social media links.

### Surface

#### Colour Scheme
Shades of teal, dark blue shade, and white are chosen for the color scheme as it goes along with all the pictures of the kitesurf spots.

![Color Palette](static/img/color-palette.png)

#### Typography
Montserrat is used as the general font-size of the website for it's clean typography and suitability with the logo. 
Cormorant Garamond is used for the dramatic headers to give it a touch of indie.

#### Imagery
Every image used on the website is a clear visualisation of what kitesurfing is, always chosen for the amazing looking backgrounds.
The home page has a gif with someone kitesurfing, so visitors can see the sport in action as a first interaction with the website.


### Skeleton

- Wireframe: 
    - [Home page](static/img/wireframe-home.pdf)
    - [log in/Sign up  + Profile page](static/img/wireframe-login.pdf)
    - [Spots pages](static/img/wireframe-spots.pdf)
    - [Countries pages](static/img/wireframe-country.pdf)
    - [Website Diagram](static/img/website-diagram.pdf)

## Features

Note:
Original plan was to implement a google maps API that will show all spots on a map on the spots template and
on the country pages displaying all the spots per country. But because of a lot of
unsuccesfull attempts trying to find solutions on how to implement google maps API and connect it to
the mongoDB Database, I decided to leave this out for this project.

### Existing Features
- Log in
- Register for an account
- Search bar to look up spots by name and region with reset button. If nothing found will return 'No results'
- Adding, editing and removing of spots in the profile only by registered users
- Adding, editing and/or removing countries only by admin
- Flash messages after every login, logout, add, edit and removal
- Profile page displays username
- Spot and countries have their own page
- Input field validation in the forms
- Responsive on all devices
    
### Future Features
- Google maps API for all the spots to be displaying on
- Password reset
- More profile information to add and ability to edit them
- SSL certificate
- Registration with email or through Google
- Page loading animation
- Pagination on the spots page, and on profile page so not more than 4 spots are shown
- Sort spots by region, experience and kitesurf season
    

## Information Architecture

MongoDB Atlas was used for storing data

Database diagram:

![Database diagram](static/img/db-diagram.png)

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://www.python.org)

### Frameworks, Libraries & Programs Used:

1. [Materialize:](https://materializecss.com)
    was used to assist with the responsiveness and styling of the website.
    Used it for the nav bar, footer, card panels, cards, buttons, modal, text inputs and the icons in the log in and sign up forms.
2. [Google Fonts:](https://fonts.google.com/)
    was used to import the font-family 'Montserrat' and 'Cormorant Garamond' into the style.css file.
3. [Font Awesome:](https://fontawesome.com/)
    was used to add social media icons in the footer.
4. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
    Flask is the web framework used to provide libraries, tools and technologies for the app.
5. [Git:](https://git-scm.com/)
    was used for version control. In the terminal of Gitpod, I used Git to add and commit to Git and after pushing it to Github.
6. [GitHub:](https://github.com/)
    is used to store and share my project.
7. [MongoDB:](https://www.mongodb.com)
    used to set up the database and manage it.
8. [Balsamiq:](https://balsamiq.com/)
    was used to create the wireframes during the design process.
9. [TinyPNG:](https://tinypng.com/)
    was used to compress the images.
10. [Heroku:](https://www.heroku.com) 
    was used to deploy the website.
11. [Ezgif:](https://ezgif.com/)
    was used to convert a video to a gif.
12. [Savefrom:](https://en.savefrom.net )
    was used to download the youtube video used for the gif.
16. [JQuery:](https://jquery.com/)
    was used for the interactive elements from Materialize.
17. [Jinja:](https://jinja.palletsprojects.com/en/3.0.x/)
    Jinja was used for templating Python
18. [Werkzeug:](https://werkzeug.palletsprojects.com/en/2.0.x/)
    Werkzeug was used for password hashing in this project

## Testing

### Validators

The following validators were used to make sure there were no syntax errors in the project.

[W3C HTML Validator](https://validator.w3.org/#validate_by_input) Passed without errors

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) Passed without errors

[JSHint](https://jshint.com/) Passed without errors

[PEP8](http://pep8online.com/) Passed without errors

### Lighthouse testing

Home page does not score well with lighthouse because of the huge gif that takes loading time.
The gif has been resized and tinified as much as possible, but also not too much to keep quality of image.
A lot of matereliaze elements trigger warnings in lighthouse as well.
Other pages always score 80-90+.

### Testing User Stories from User Experience (UX) Section

- #### As a First Time User I want to
    1. Find an explanation of the website and about what kitesurfing is.

        The explanation about the website and about what kitesurfing is, is showing on the home page.
        
        ![screenshot1](static/img/screenshot1.png)

    2. Be able to sign up and have my own profile.

        When you click in the nav bar on sign up you will get the following form
        
        ![screenshot2](static/img/screenshot2.png)

    3. Be able to look up kitesurf spots by name, region.

        In the search bar you can enter any name or region to find the kitesurf spot. You can also reset your search.
        
        ![screenshot3](static/img/screenshot3.png)

    4. Be able to browse kitesurf spots by country.

        When you click on countries in the navbar it will take you to a page with all the countries listed with pictures
        
        ![screenshot4](static/img/screenshot4.png)

    5. Access the website on mobile and desktop and for it to be responsive.

        The website is repsonsive and accessible on mobile devices.
        
        ![screenshot5](static/img/screenshot5.png)

    6. Find more info about a kitespot when I click on it in the list of kitespots

        When you click on the name in the card, it will take you to an individual page about the spot. If clicked on the picture
        it will show you the description of the spot.
        
        ![screenshot6](static/img/screenshot6.png)
        ![screenshot7](static/img/screenshot7.png)

    7. Find info about the country and their wind season.

        When you click on one of the countries it will take you to the individual page of the country with a description, wind season table and the spots in the country.
        
        ![screenshot8](static/img/screenshot8.png)


- #### As a member I want to
    1. Be able to add my own kitesurf spots.

        To make it very accessible and easy to add a spot, there are 2 ways. One link in the navbar and a link in your profile.
        
        ![screenshot9](static/img/screenshot9.png)
        ![screenshot10](static/img/screenshot10.png)

    2. Log in with user friendly form.

        When you click on log in in the navbar it will take you to the log in page.
        
        ![screenshot14](static/img/screenshot14.png)

    3. Edit and delete my own kitesurf spots.

        In your profile you will be able to see all of your spots listed and with edit and delete options next to every spot.
        But also in the list of spots on spots.html, when you click on the picture of one the search results, you will also find edit and delete buttons if it is a spot your account has added.
        
        ![screenshot11](static/img/screenshot11.png)
        ![screenshot12](static/img/screenshot12.png)


    4. Get feedback for adding, editing, logging in and logging out.

        Everytime you add, edit, delete, log in or log out, there will be a flash message.
        
        ![screenshot13](static/img/screenshot13.png)

    5. Get an error messages in case I have done something wrong or there is an issue with the database.

        In case with an error the following error page will display with a link to go back to the home page.
        
        ![screenshot15](static/img/screenshot15.png)

- #### As an admin I want to be able:

    1. To access, edit and delete spots and countries from the admin profile

        The admin's profile page will also have all the countries listed that the admin can edit and delete in the same
        way as with the spots.
        
        ![screenshot16](static/img/screenshot16.png)


### Functional Testing

| Action        | Expected Behaviour         | Pass/Fail  |
| ------------- |:-------------:| -----:|
| Click on the nav buttons| Brings you to the page | Pass |
| `Spots.html` |||
| Fill in something in the search bar | Returns a spot or 'No Results Found' | Pass |
| Click the reset button | Page shows all spots again | Pass |
| `Countries.html` |||
| Click on one of the country images | Redirects you to individual country page | Pass |
| `Log_in.html` |||
| Fill in existing username and password | Logs in and shows the profile with flash message "Hello again, (username)" | Pass |
| Fill in non existing username and password | Shows flash message "Incorrect username and/or Password" | Pass |
| `Sign_up.html` |||
| Fill in username and password with min. 5 characters | Logs in and shows the profile with flash message "Account created" | Pass |
| Fill in username and passwword with less than 5 characters | Will show required under input field with info why | Pass |
| Fill in existing username | Will show flash message "Username already in use" | Pass |
| `profile.html` |||
| View profile page | View list of spots made by current logged in user | Pass |
| Click on button "Add spot" | Redirects you to page to add spot | Pass |
| Click on name of spot in list | Redirects to individual spot page | Pass |
| Click on edit button next to name of spot | Redirects you to edit form of spot | Pass |
| Click on Delete button | Modal shows up if you want to delete or not | Pass |
| Click on delete in the delete modal | Deletes spot | Pass |
| Click on cancel in the delete modal | Modal disappears and nothing happened | Pass |
| Admin only sees section to edit and delete Countries | Same functionality as list of spots | Pass |
| Click on Log out in nav bar | You log out and redirected to log in page | Pass |
| `add_spot.html add_country.html` |||
| Not filling something in | The input line turns red and required appears | Pass |
| Click on Submit | Spot or Country is added and redirected to spots.html or profile.html | Pass |
| `edit_spot.html edit_country.html` |||
| Entering the page | Shows all database elements in the input fields | Pass |
| Click on Edit button | Spot is edited and shows flash msg "Spot successfully updated" | Pass |
| Click on Cancel button | Nothing changes and redirects to profile | Pass |


### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and Firefox.
-   The website was tested on all device sizes that are viewable in DevTools.
-   Family members and friends were asked to test the website on their devices.
-   The website was viewed on a variety of devices:

    Desktop:
    - HP Spectre Notebook
    - Sony VAIO Fit15E (laptop)
    - Acer Predator G5900 (computer)
    - ASUS 18363 (computer) 
    - ASUS N73S (laptop)

    Mobile:
    - Samsung Galaxy A41
    - Samsung Galaxy S7 2017
    - Samsung Galaxy A70
    - Huawei Y60 2018
    - Huawei P30 Pro
    - Xiaomi mi 9 SE
    - Iphone XS Max

### Known Bugs

- Tried to give the callout container and columns on home.html all 1 fade in class. But the fade in effect then dissappears.
So I pasted the fade in css as an id for the 2 columns and directly in the callout-container class.

## Deployment

### 1. Making a Local Clone

1. Log in to [GitHub](https://github.com/) and navigate yourself to the repository.
2. Click the 'Code' dropdown above the file list.
3. Copy the URL for the repository.
4. Open Git Bash
5. Change the current working directory to where you want the cloned directory.
6. Type git clone in the CLI and then paste the URL you copied earlier.
   It should look like this:
```
$ git clone https://github.com/kristinabog/greek-beaches-memory-game
```
7. Press enter to create clone

### 2. Connect to MongoDB

Make a free account on [MongoDB](https://www.mongodb.com/) an recreate the database

In your development environment, upgrade pip if needed
```
pip install --upgrade pip
```
Install all dependencies to enable the installation of the packages required for this project 
```
$ pip3 install -r requirements.txt
```
Create the following files in the root directory:

- env.py
- .gitignore

Oopen the .gitignore file and add:

- env.py
- __pycache__/

These files will not be pushed to GitHub

Open the env.py file and add the following:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<secret key>")
os.environ.setdefault("MONGO_URI", "<from mongo>")
os.environ.setdefault("MONGO_DBNAME", "<database name>")
```

The app can crun locally typing the following in the terminal:
```
python3 app.py
```

### Deploy to Heroku

Heroku requires the following files to run properly:
- requirements.txt
- Procfile

Heroku was the chosen deployment platform for this project. 
These are the steps to deploy the local app to Heroku:

- In Heroku, create an app with an unique name
- Choose region, click 'Create App'
- Select GitHub as Deployment method. Make sure your GitHub username is displayed
- Type in repo name and click 'search' and then 'connect'

How to find the variables to define in env.py 

- Click on 'Settings' Tab
- Click on ‘Reveal Config Vars’

Deploying

- Click on the Deploy tab
- Click ‘enable automatic deploys’
- Click ‘deploy branch’ below. Make sure the master branch is selected
- When deployment is succesfull you will see the following message: ‘Your app was successfully deployed’


## Credits

### Code

- The python code in app.py was inspired by the task manager app mini project from Code Institute 
- Materialize: styling, responsiveness, nav bar, footer, card panels, cards, buttons, modal, text inputs and the icons in the log in and sign up forms.
- [Fade in effect home page](https://stackoverflow.com/questions/11679567/using-css-for-a-fade-in-effect-on-page-load)
- [Search bar](https://codepen.io/huange/pen/rbqsD)

### Video

The gif on home.html came from the following video: 
- [Drone footage - kitesurfing, Playa De Sotavento, Fuerteventura](https://youtu.be/c0LgNLFbon8)
Found on Youtube.com searching with a Creative common filter

### Images

Log in and sign up template:
- [Log in and sign up side picture](https://pixabay.com/photos/kite-surfing-kitesurfing-sea-3857693/)

Countries.html:
- [Greece](https://globalkitespots.com/wp-content/uploads/Greece-wind.png)
- [Italy](https://images.pexels.com/photos/417239/pexels-photo-417239.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)
- [Portugal](https://cdn.pixabay.com/photo/2017/09/08/00/25/sea-2727251__340.jpg)
- [Spain](https://cdn.pixabay.com/photo/2014/08/19/13/01/sand-castle-421483__340.jpg)
- [Wind diagrams](https://globalkitespots.com/)

Spots:
- [Royal Sands Marmari Surf Club](https://photos.tpn.to/rs/os/oh/qi/653x490.jpg)
- [Playa De Sotavento](https://www.kiteworldmag.com/wp-content/uploads/2015/01/reneegli_zones-pic-by-kerstin-reiger.jpg)
- [La Cinta Sardinia](https://media.istockphoto.com/photos/spiaggia-la-cinta-kite-and-surf-beach-sardinia-italy-picture-id1064631184?k=6&m=1064631184&s=170667a&w=0&h=tpZGgR_Ok7mJSMRw4BN9nlvi4LCPsgAm2qLaT0iro4k=)
- [Bolonia](https://t4.ftcdn.net/jpg/00/05/41/15/360_F_5411543_IKg1nDJJjvvbRvUXaSrgyTTeKYO41Ou9.jpg)
- [Mikri Vigla](https://img.theculturetrip.com/768x/smart/wp-content/uploads/2020/08/kitesurfing-in-mikri-vigla-beach-on-naxos-island-greece.jpg)
- [Cabadelo](https://blog.bstoked.net/wp-content/uploads/2018/04/kiteboarding-in-portugal.jpg)
- [Favicon](https://icon-library.com/icon/kitesurf-icon-3.html)

### Content

- [Kitesurf description](https://www.thekitesurfcentre.com/what-is-kitesurfing)
- [Description Marmari Surf Club](https://www.worldpackers.com/locations/royal-sands-marmari-surf-club#:~:text=Time%201%20day-,Royal%20Sands%20Marmari%20Surf%20Club,experience%20for%20all%20our%20team.)
- [Description Playa De Sotavento](https://www.kiteworldmag.com/travel/sotavento-fuerteventura/)
- [Description La Cinta Sardinia](http://www.sardinianbeaches.com/best-kitesurfing-beaches-of-sardinia/)
- [Description Bolonia](https://wakeupstoked.com/kitesurf-tarifa-spain/)
- [Description Mikri Vigla](https://theculturetrip.com/europe/greece/articles/where-to-go-windsurfing-and-kitesurfing-in-naxos/)
- [Description Cadabelo](https://blog.bstoked.net/locations/top-5-kitesurfing-spots-in-portugal-new-in-2018/)

### Acknowledgements

- My Mentor for the helpful feedback.

- A very big thank you to the Tutor support who helped me solve bugs.

- A thank you to family and friends that took the time to test the website.


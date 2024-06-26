# Board game review 

Being interested in different board games, this Django challenge was an interesting experience. The site should attract all user liking board games and contributing to an open-minded exchange on them.

![Displaying responsiveness of the homepage](read-me-images/responsive.png)

View the live project here: <https://bg-review-p4-acb57fa06b77.herokuapp.com/>


## Table of content

- [Board game review ](#board-game-review )
  - [Table of content](#table-of-content)
  - [UX](#ux)
    - [Site owner goals](#site-owner-goals)
    - [Agile planning](#agile-planning)
      - [Milestones](#milestones)
      - [User stories](#user-stories)
        - [As a visitor](#as-a-visitor)
        - [As the administrator](#as-the-administrator)
        - [As the developer](#as-the-developer)
      - [Wireframes](#wireframes)
      - [Flow Chart](#flow-chart)
      - [Method](#method)
        - [POC (proof of concept)](#poc-(proof-of-concept))
        - [MVP (minimum viable product)](#mvp-(minimum-viable-product))
      - [Tasks](#tasks)
    - [Features](#features)
      - [Homepage](#homepage)
      - [Detailed review page](#detailed-review-page)
      - [Comment section](#comment-section)
      - [Login](#login)
      - [Register](#register)
      - [Logout](#logout)
      - [Features left to implement](#features-left-to-implement)
  - [Used Technologies](#used-technologies)
    - [Languages Used](#languages-used)
    - [Framework, Libraries and Programs](#framework-libraries-and-programs)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Testing user stories](#testing-user-stories)
    - [Validator testing](#validator-testing)
    - [Unfixed bugs](#unfixed-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)


## UX

### Website owner goals

As the owner of the website, I want to create a contribution to the community by giving them another place to share their opinions on board games.
Therefore, I set my website owner goals as followed:
- Within the first two months I want to get 100 registrations of users who created at least one review.
- Within the first six months I want to have reviews of at least 500 different board games on the website.
- Each month I want to have at least 100 persons visiting my website.

### Agile planning

The development of this project was done with an agile approach.

Here is an example of the Kanban board from an early development stage:
![Example of the Kanban board in an early stage](read-me-images/kanban.png)

The project board can be found here: <https://github.com/users/RenaSchott/projects/3>.

#### Milestones
- **1-Preparation:** Make the preparation for the project as for example user stories, set up, deployment etc.
- **2-Create landing page:** Create the first page of the homepage
- **3-Make landing page interactive:** Add search bar, comments, and open review option
- **4-Accounts:** Create option to make and account and log in and out
- **5-Review:** Make it possible to review existing and new board games
- **6-Admin:** Make it possible for the administrator to delete, edit and add content
There is no final deployment milestone, since the deployment started as early as possible to avoid mistakes in early steps.

The milestones can be found here <https://github.com/RenaSchott/Project4-BoardGameReview/milestones>.

#### User stories

The user stories can be found here <https://github.com/RenaSchott/Project4-BoardGameReview/issues>.

##### As the developer
- **Preparation:** As a **developer**, I need to **set up my project**, so **I can create work on it.** 
  - **Acceptance Criteria:**
    - Coding is about to start 
    - Readme file is up-to-date
    - Deploy project

##### As a visitor

- **View the newest reviews:**  As a **Site User**, I can **view the reviews on the starting page** so that **I can select a specific one to read.**
  - **Acceptance Criteria:**
    - homepage is styled and structured
    -  page is scrollable

- **Open a review:** As a **Site User**, I can **open a review** so that **I can read the full text.**
  - **Acceptance Criteria:**
    - An expand button is showing
    - button is clickable
    - full review is showing
    - site is scrollable
- **View ratings:** As a **Site User**, I can **view the ratings on the starting page** so that **I can get an impression of the specific board game.**
  - **Acceptance Criteria:**
    - homepage is styled and structured
    - ratings are shown
- **Search:** As a **Site User**, I can **use the search bar** so that **I can look for a specific board game.**
  - **Acceptance Criteria:**
    - in to top left a search bar is shown
    - search results will be displayed
- **View comments:** As a **Site User**, I can **view the comments of other people** so that **I can get to know their opinion on the review.**
  - **Acceptance Criteria:**
    - number of comments is shown on the homepage
    - button is clickable
    - all existing comments are shown 
- **Comment on a review:** As a **Site User**, I can **comment on a review** so that **I can share my opinion on that.**
  - **Acceptance Criteria:**
    - Clickable button is shown on the website
    - form is opening
    - comment is addable
- **Account registration:** As a **Site User**, I can **register an account** so that **I can add reviews and ratings.**
  - **Acceptance Criteria:**
    - Clickable button exists on the homepage
    - form opens
    - registration is possible
- **Create new reviews/ratings:** As a **Site User**, I can **create new reviews and ratings** so that **I can contribute to the site's grows.**
  - **Acceptance Criteria:**
    - Button is clickable 
    - form is opening
    - review and rating is added
- **Add my own review/ratings:** As a **Site User**, I can **add my own reviews and ratings on already reviewed board games** so that **I can share my personal opinion.**
  - **Acceptance Criteria:**
    - Button is clickable 
    - form is opening
    - image can be added
    - review and rating is added
- **Manage reviews:** As a **Site User**, I can **create, read, update and delete my reviews** so that **I can manage my contents.**
  - **Acceptance Criteria:**
    - reviews/ratings are shown on personal site
    - button is clickable
    - form opens
    - editing is shown

##### As the administrator

- **Manage comments/reviews:** As **the Admin**, I can **manage the comments and reviews** so that **I can make sure that the site contributes to the growth of the community in a friendly and social way.**
  - **Acceptance Criteria:**
    - an overview of the reviews and comments is shown
    - page is scrollable
    - complete deletion and part deletion is possible
    - editing is possible

#### Wireframes

Here are the drawings of the wireframes for the browsers and for smartphones:

**Homepage:**
![Drawing of the homepage](read-me-images/wireframe5.png)
![Drawing of the homepage](read-me-images/wireframe6.png)

**Register:**
![Drawing of the register page](read-me-images/wireframe3.png)
![Drawing of the register page](read-me-images/wireframe4.png)

**Log In:**
![Drawing of the login page](read-me-images/wireframe1.png)
![Drawing of the login page](read-me-images/wireframe2.png)

**Personal user page:**
![Drawing of the personal user page](read-me-images/wireframe11.png)
![Drawing of the personal user page](read-me-images/wireframe12.png)

**Add review:**
![Drawing of the add review page](read-me-images/wireframe9.png)
![Drawing of the add review page](read-me-images/wireframe10.png)

**Add comment:**
![Drawing of the add comment page](read-me-images/wireframe7.png)
![Drawing of the add comment page](read-me-images/wireframe8.png)


#### Flow Chart

Here is the outlined flow chart:

![Drawn flowchart of the project](read-me-images/flowchart_P4.png)

#### Entity Relationship Diagram

Here is the outlined ERD:

![Drawn entity relationship diagram of the project](read-me-images/erd_P4.png)

#### Method

##### POC (proof of concept)

- Register
- Log in and out
- Uploading/Deleting image
- Adding comments
- Adding reviews
- Editing reviews
- Rating system

##### MVP (minimum viable product)

- Interacting with an existing entry
    - Commenting on an entry
- Create new account
- Logging in and out of the page
    - Making a new entry
        - Adding an image of a board game
        - Adding a review
        - Rating the board game
    - Editing own entries
        - Deleting own image of a board game
        - Load other image
        - Editing own reviews
    - Interacting with other entries
        - Writing own review
        - Rating the board game 


#### Tasks
**In product backlog (with (untested) storypoints)**

The tasks can be found within the user stories here: <https://github.com/RenaSchott/Project4-BoardGameReview/issues>.

- **Userstory 1 - Preparation:**
  - Task 1: Setup workspace
  - Task 2: Create User Stories with acceptance criteria, Storypoints and Tasks
  - Task 3: Create Wireframes
  - Task 4: Create Flowchart
  - Task 5: Create Entity Relationship Diagram
  - Task 6: Deploy project (ElephantSQL + Heroku)
- **Userstory 2 - View the newest reviews:** 
  - Task 1: Create HTML + CSS --- Storypoint/s: 2
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 3 - Open a review:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 2
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 4 - View ratings:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 2
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 5 – Search:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 1
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 6 - View comments:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 1
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 7 - Comment on a review:**
  - Task 1: Design User Interface --- Storypoint/s: 4
  - Task 2: Create HTML + CSS --- Storypoint/s: 2
  - Task 3: Create the models --- Storypoint/s: 1
  - Task 4: Testing --- Storypoint/s: 2
- **Userstory 8 - Account registration:**
  - Task 1: Design User Interface --- Storypoint/s: 8
  - Task 2: Create HTML + CSS --- Storypoint/s: 4
  - Task 3: Create the models --- Storypoint/s: 2
  - Task 4: Testing --- Storypoint/s: 1
- **Userstory 9 - Create new reviews/ratings:**
  - Task 1: Design User Interface --- Storypoint/s: 16
  - Task 2: Create HTML + CSS --- Storypoint/s: 8
  - Task 3: Create the models --- Storypoint/s: 4
  - Task 4: Testing --- Storypoint/s: 4
- **Userstory 10 - Add my own review/ratings:**
  - Task 1: Design User Interface --- Storypoint/s: 8
  - Task 2: Create HTML + CSS --- Storypoint/s: 4
  - Task 3: Create the models --- Storypoint/s: 4
  - Task 4: Testing --- Storypoint/s: 4
- **Userstory 11 - Manage reviews:**
  - Task 1: Design User Interface --- Storypoint/s: 16
  - Task 2: Create HTML + CSS --- Storypoint/s: 8
  - Task 3: Create the models --- Storypoint/s: 8
  - Task 4: Testing --- Storypoint/s: 4
- **Userstory 12 - Manage comments/reviews:**
  - Task 1: Design User Interface --- Storypoint/s: 32
  - Task 2: Create HTML + CSS --- Storypoint/s: 16
  - Task 3: Create the models --- Storypoint/s: 8
  - Task 4: Testing --- Storypoint/s: 8


## Features

### Homepage

- The homepage welcomes the user and reminds the user of a friendly with each other. 
Then all the reviews are displayed with an image, the author, the creation date and an excerpt. 
At the bottom, the user can go to the next page or later on to the previous one.
- The final project differs from the planned one. There is room for more features.

![Screenshot of the homepage](read-me-images/homepage.png)
![Screenshot of the homepage](read-me-images/next.png)
![Screenshot of the homepage](read-me-images/prev.png)

### Detailed review page

- By clicking on the text of one specific review on the main homepage, the user will be forwarded to the detailed page. 
There are next to an image, the title, the author, the creation date, the content and count of comments as well as the average rating
together with the number of ratings, is displayed. The lower half of the page is filled with the comment section.

![Screenshot of the detailed page](read-me-images/rev-details.png)

### Comment section

- The comment section displays approved comments on the left and an explanation of how to make a comment on the right. Logged-in users can see their submitted and not yet approved comments on the left, where there are also the buttons for editing and deletion. On the right, they can submit another comment. After approval, the comment is displayed for everyone on the homepage of the review details.

![Screenshot of the comment section](read-me-images/comment.png)
![Screenshot of the question for deletion](read-me-images/del-com.png)

### Login

- In the menu bar in the header, the user can choose to log in. After clicking the button, the login forms opens and the user can sign in.

![Screenshot of the login button](read-me-images/reg-login.png)
![Screenshot of the login form](read-me-images/signin.png)

### Register

- In the menu bar in the header, the user can choose to register. After clicking the button, the signup forms opens and the user can register.

![Screenshot of the register button](read-me-images/reg-login.png)
![Screenshot of the login form](read-me-images/signup.png)

### Logout

- The user can find the logout button in the menu in the header. After clicking the button, the user is asked again whether the user wants to sign out. After the confirmation click, a written confirmation is displayed.

![Screenshot of the logout button](read-me-images/logou-btn.png)
![Screenshot of the sign out](read-me-images/signout.png)
![Screenshot of the sign out confirmation](read-me-images/signout-confirmation.png)


### Features left to implement

There is the possibility to integrate:

- **V2 (version 2)**
    - Rating system 
        - Divided up for each year
        - Divided into complexity
        - Divided into family, connoisseur and expert board game
    - Images 
        - Expand upload capacity
    - Adding chat/message function
    - Adding extra forum for further exchange
    - Edit own account
        - Personal data
        - Upload personal image
        - Delete Account

## Used Technologies

### Languages Used

- HTML, CSS, Python, Jinja

### Framework, Libraries and Programs

- Frameworks were used to speed up 
    - Django
    - Bootstrap
- Libraries 
    - Gunicorn
      - was used as python http server for WSGI applications
    - Pyscopg2
      - was used as PostgresSQL Database adapter
    - Django-allauth
      - was used to create user authentication
    - Django-crispy-forms
      - was used to control rendering behavior of Django forms
    - Whitenoise
      - was used to serve static non-media files
    - Summernote
      - was used as WYSIWYG editor
- Programs
    - Balsamiq
        - was used to create the wireframes
    - Lucidchart
        - was used to create the flow chart
    - dbdiagram
        - was used to create the entity relationship diagram
    - GitHub
        - was used to store the project site
    - Gitpod
        - was used to write the code and commit it to GitHub
    - Heroku 
        - was used to deploy the project 
    - CI Database Maker
        - was used for storing the database
    - Cloudinary
        - was used to serve static media files  
    - Validator W3
        - was used to validate the HTML
    - Validator W3C
        - was used to validate the CSS
    - JSHint
        - was used to validate the JavaScript
    - CI Python Linter
        - was used for finding errors
    - Languagetool
        - was used to check the spelling and grammar in the README file


## Testing

### Manual testing

- The site was tested on different browsers: Chrome, Firefox and Safari.
- I confirmed that the page is readable.
- I confirmed that links are functioning.

| **Feature** | **Expect** | **Action** | **Result** |
|---------------------|--------------------|--------------------------|------------------------------|
| next / previous button | User should be directed to the next or previous page | click on button | Redirection to previous or next page |
| Login | User should be forwarded to sign-in page | click on button | Redirection to sign-in page |
| Sign-in | User should be forwarded to the homepage as login | fill in details and click on button | Redirection to the homepage as logged-in user |
| Logout | User should be forwarded to confirmation page | click on button | Redirection to confirmation page |
| Logout confirmation | User should be forwarded to homepage | click on button | Redirection to the homepage |
| Register | User should be forwarded to signup form | click on button | Redirection to signup form |
| Signup | User should be forwarded to the homepage as logged-in user | fill in details and click on button | Redirection to the homepage as logged-in user |
| View detailed review | the reviews on the main page should be clickable, and a detailed review page should open | click on the review text | Redirection to specific review page |
| Submit comment | User should be able to type in text and submit it | type and click on button | Text box can be used and after clicking submission the comment can be seen as waiting for approval. |
| Edit comment | User should be able to edit every comment they have written | login and click on button | Comments are editable |
| Delete comment | User should be redirected to confirmation page | click on button | Redirection to confirmation page |
| Deletion confirmation | User should be asked whether they want to return or delete the comment | click on button | Deletion and cancellation are fully functioning |



### Testing user stories

| **Expectation - User** | **Result**|
|--------------|------------|
| I can view the reviews on the starting page so that I can select a specific one to read. | All reviews are shown on the homepage on different sites and are clickable. |
| I can open a review so that I can read the full text. | The detailed review page opens and the content displays. |
| I can view the ratings on the starting page so that I can get an impression of the specific board game. | The ratings were moved. The average ratings and the amount of ratings can be seen on the review details page. |
| I can use the search bar so that I can look for a specific board game. | A search bar is not included at the moment. |
| I can view the comments of other people so that I can get to know their opinion on the review. | Approved comments can be seen on the review details page. |
| I can comment on a review so that I can share my opinion on that. | Logged-in users can comment on the reviews. |
| I can register an account so that I can add reviews and ratings. | Site users can register and add comments. Superusers can add reviews and ratings in the admin panel. |
| I can create new reviews and ratings so that I can contribute to the site's grows. | A superuser can contribute to the site's growth via the admin panel. |
| I can add my own reviews and ratings on already reviewed board games so that I can share my personal opinion. | A superuser can add reviews via the admin panel to share their opinion. |
| I can create, read, update and delete my reviews so that I can manage my contents. | A superuser can use all the CRUD functions in the admin panel, and a normal user can use them on their comments. |


**As the developer**

| **Expectation - Administrator** | **Result**|
|--------------|------------|
|  I need to set up my project, so I can create work on it. | The project setup worked. |


**As the administrator**

| **Expectation - Administrator** | **Result**|
|--------------|------------|
|  I can manage the comments and reviews so that I can make sure that the site contributes to the growth of the community in a friendly and social way. | Via the admin panel, everything can be managed. |


### Validator testing

- **Validator W3**

All sites tested - each result:
![Screenshot of one result of the testings](read-me-images/html-validation.png)

- **Validator W3C**

Test results:
![Screenshot of the errors](read-me-images/css-validation1.png)
![Screenshot of the warnings](read-me-images/css-validation2.png)

- **JSHint**

Test result:
![Screenshot of one undefined variable](read-me-images/js-val1.png)


- **CI Python Linter**

Test results of files with custom written code:
![Screenshot of one result of the testings](read-me-images/pep8.png)


- **Lighthouse**

The results of the lighthouse testing are sufficient.
![Screenshot of the lighthouse results](read-me-images/lighthouse.png)

### Unfixed bugs

- The CSS validation results showed a problem with Bootstrap5. Errors and warnings were acceptable since Bootstrap is needed for the project.
- The results of the JS validation are also acceptable. The variable did not need to be defined at this point.

## Deployment

The deployment was done after the tutorial in the course content using <https://www.heroku.com/>, <https://cloudinary.com/>, <https://dbs.ci-dbs.net/> and <https://whitenoise.readthedocs.io/en/latest/>.

For deployment:
- Some libraries have to be installed:
  - Gunicorn
  - psycopg2
  - Cloudinary
  - Whitenoise
- A Heroku account must be created.
- Set your GitHub repository to public.
- Create a new app and linked to the correct repo in GitHub while choosing Automatic Deploys for easier handling.
- Create a database with Ci database Maker and link it to the project and the heroku app.
- Hide sensitive information in the env.py with the .gitignore file and update the settings.py file.
- Connect the project and Heroku app with Cloudinary.
- Then deploy
 
The link to the live page can be found here: [Link to live page] (<https://bg-review-p4-acb57fa06b77.herokuapp.com/>)


## Credits

### Content

The content of this project was inspired by the "Hello Django" and "I Think Therefore I Blog" project and the content of the course. In general, the following websites were used for inspiration:
  - <https://www.youtube.com/watch?v=sm1mokevMWk>
  - <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/>
  

Inspirations for specific problems were taken from the following websites:
  - <https://docs.djangoproject.com/en/4.2/topics/db/models/>
  - <https://www.geeksforgeeks.org/emailfield-django-models/>
  - <https://www.makeuseof.com/django-dynamic-routing/>
  - <https://mdbootstrap.com/how-to/bootstrap/footer-at-bottom/>
  - <https://getbootstrap.com/docs/5.0/utilities/text/>
  
### Media

Images were downloaded from <https://pixabay.com/de/>
- Placeholder image: <https://pixabay.com/de/illustrations/schach-hunde-haustier-schach-spiel-7802136/>
- Carcassonne: 
  - <https://pixabay.com/de/illustrations/brettspiel-brett-spiel-spiele-2237460/>
- Ludo: 
  - <https://pixabay.com/de/vectors/brett-spiel-ludo-freizeit-gl%C3%BCck-48117/>
  - <https://pixabay.com/de/vectors/ludo-spiel-spielbrett-148865/>
- Chess: 
  - <https://pixabay.com/de/illustrations/schach-strategie-spiel-k%C3%B6nig-brett-1709603/>
  - <https://pixabay.com/photos/checkmate-chess-board-chess-board-1511866/>
  - <https://pixabay.com/de/vectors/schach-planke-brettspiel-4538802/>
- Monopoly:
  - <https://pixabay.com/de/illustrations/hintergrund-spiel-brett-monopol-8383489/>
  - <https://pixabay.com/de/illustrations/monopol-spielbrett-spiel-spa%C3%9F-1984400/>

## Acknowledgements

- I would love to thank the following persons:
  - My mentor for his support
  - The Code Institute tutor support for their fast answers
  - My facilitator for her support
  - The slack community for their fast answers and support
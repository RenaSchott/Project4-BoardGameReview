# Battleship

Being interested in different board games, this Django challenge was an interesting experience. The site should attract all user liking board games and contributing to an open-minded exchange on them.

View the live project here: <>


## Table of content

- [Battleship](#battleship)
  - [Table of content](#table-of-content)
  - [UX](#ux)
    - [Site goals](#site-goals)
    - [User stories](#user-stories)
      - [As a visitor](#as-a-visitor)
      - [As the administrator](#as-the-administrator)
    - [Wireframes](#wireframes)
    - [Flow Chart](#flow-chart)
  - [Method](#method)
    - [POC (prove of concept)](#poc-(prove-of-concept))
    - [MVP (minimum viable product)](#mvp-(minimum-viable-product))
  - [Features](#features)
    - [Welcome screen](#welcome-screen)
    - [Username](#username)
    - [Game rules](#game-rules)
    - [Game board](#game-board)
    - [User moves](#user-moves)
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

As the owner of the website I want to create a contribution to the community by giving them another place to share their opinions on board games.
Therefore I set my website owner goals as followed:
- Within the first two month I want to get 100 registrations of users who created at least one review.
- Within the first six month I want to have reviews of at least 500 different board games on the website.
- Each month I want to have at least 100 persons visiting my website.

### User stories

#### As a visitor

- **View newest reviews:**  As a **Site User** I can **view the reviews on the starting page** so that **I can select a specific one to read.**
- **Open a review:** As a **Site User** I can **open a review** so that **I can read the full text.**
- **View ratings:** As a **Site User** I can **view the ratings on the starting page** so that **I can get an impression of the specific board game.**
- **Search:** As a **Site User** I can **use the search bar** so that **I can look for a specific board game.**
- **View comments:** As a **Site User** I can **view the comments of other people** so that **I can get to know their opinion on the review.**
- **Comment on a review:** As a **Site User** I can **comment on a review** so that **I can share my opinion on that.**
- **Account registration:** As a **Site User** I can **register an account** so that **I can add reviews and ratings.**
- **Create new reviews/ratings:** As a **Site User** I can **create new reviews and ratings** so that **I can contribute to the sites grows.**
- **Add my own review/ratings:** As a **Site User** I can **add my own reviews and ratings on already reviewed board games** so that **I can share my personal opinion.**
- **Manage reviews:** As a **Site User** I can **create, read, update and delete my reviews** so that **I can manage my contents.**

#### As the administrator

- **Manage comments/reviews:** As **the Admin** I can **manage the comments and reviews** so that **I can make sure that the site contributes to the grows of the community in a friendly and social way.**

### Wireframes

Here are the drawings of the wireframes for the browsers and for smartphones:

**Homepage:**
![Drawing of the homepage](read-me-images/wireframe5.png)
![Drawing of the homepage](read-me-images/wireframe6.png)

**Register:**
![Drawing of the register page](read-me-images/wireframe3.png)
![Drawing of the register page](read-me-images/wireframe4.png)

**Log In:**
![Drawing of the log in page](read-me-images/wireframe1.png)
![Drawing of the log in page](read-me-images/wireframe2.png)

**Personal user page:**
![Drawing of the personal user page](read-me-images/wireframe11.png)
![Drawing of the personal user page](read-me-images/wireframe12.png)

**Add review:**
![Drawing of the add review page](read-me-images/wireframe9.png)
![Drawing of the add review page](read-me-images/wireframe10.png)

**Add comment:**
![Drawing of the add comment page](read-me-images/wireframe7.png)
![Drawing of the add comment page](read-me-images/wireframe8.png)


### Flow Chart

Here is the outlined flow chart:

![Drawn flowchart of the project](read-me-images/flowchart_P4.png)

### Entity Relationship Diagram

Here is the outlined ERD:

![Drawn entity relationship diagram of the project](read-me-images/erd_P4.png)

### Method

#### POC (prove of concept)

- Register
- Log in and out
- Uploading/Deleting image
- Adding comments
- Adding reviews
- Editing reviews
- Rating system

#### MVP (minimum viable product)

- Interacting with an existing entry
    - Commenting on an entry
- Create new account
- Logging in and out of the page
    - Making a new entry
        - Adding an image of a board game
        - Adding an review
        - Rating the board game
    - Editing own entries
        - Deleting own image of a board game
        - Load other image
        - Editing own reviews
    - Interacting with other entries
        - Writing own review
        - Rating the board game 


### Tasks in product backlog (with (untested) storypoints):
- **Userstory 1 - View newest reviews:** 
  - Task 1: Create HTML + CSS --- Storypoint/s: 2
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 2 - Open a review:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 2
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 3 - View ratings:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 2
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 4 – Search:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 1
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 5 - View comments:**
  - Task 1: Create HTML + CSS --- Storypoint/s: 1
  - Task 2: Create the models --- Storypoint/s: 1
  - Task 3: Testing --- Storypoint/s: 2
- **Userstory 6 - Comment on a review:**
  - Task 1: Design User Interface --- Storypoint/s: 4
  - Task 2: Create HTML + CSS --- Storypoint/s: 2
  - Task 3: Create the models --- Storypoint/s: 1
  - Task 4: Testing --- Storypoint/s: 2
- **Userstory 7 - Account registration:**
  - Task 1: Design User Interface --- Storypoint/s: 8
  - Task 2: Create HTML + CSS --- Storypoint/s: 4
  - Task 3: Create the models --- Storypoint/s: 2
  - Task 4: Testing --- Storypoint/s: 1
- **Userstory 8 - Create new reviews/ratings:**
  - Task 1: Design User Interface --- Storypoint/s: 16
  - Task 2: Create HTML + CSS --- Storypoint/s: 8
  - Task 3: Create the models --- Storypoint/s: 4
  - Task 4: Testing --- Storypoint/s: 4
- **Userstory 9 - Add my own review/ratings:**
  - Task 1: Design User Interface --- Storypoint/s: 8
  - Task 2: Create HTML + CSS --- Storypoint/s: 4
  - Task 3: Create the models --- Storypoint/s: 4
  - Task 4: Testing --- Storypoint/s: 4
- **Userstory 10 - Manage reviews:**
  - Task 1: Design User Interface --- Storypoint/s: 16
  - Task 2: Create HTML + CSS --- Storypoint/s: 8
  - Task 3: Create the models --- Storypoint/s: 8
  - Task 4: Testing --- Storypoint/s: 4
- **Userstory 11 - Manage comments/reviews:**
  - Task 1: Design User Interface --- Storypoint/s: 32
  - Task 2: Create HTML + CSS --- Storypoint/s: 16
  - Task 3: Create the models --- Storypoint/s: 8
  - Task 4: Testing --- Storypoint/s: 8


## Features

### Welcome screen

- The welcome screen is the first thing the user sees from the battleship app. Here the large letters "Welcome to Battleship!" can be seen, as well as the question "Do you want to start the game (y/n)?. The (y/n) indicates the possible input. By typing in y the user can progress with the game. While n will stop the game from running. If the user gives any other input, the user will be asked again to answer the question correct. The y and n answer will be automatically commented.

![Screen shot of the welcome screen of the project](assets/readmeimages/welcome-screen.png)


### User moves

- 

![]()

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

- Frameworks 
    - Django
    - Bootstrap
- Libraries 
    - 
- Moduls
    - 
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
    - CI Python Linter
        - was used for finding errors
    - Languagetool
        - was used to check the spelling and grammar in the README file.


## Testing

### Manual testing

- The site was tested on different browsers: Chrome, Firefox and Safari.
- I confirmed that the page is readable.
- I confirmed that questions are functioning.

| **Feature** | **Expect** | **Action** | **Result** |
|---------------------|--------------------|--------------------------|------------------------------|
|  |  |  |  |


### Testing user stories

| **Expectation - User** | **Result**|
|--------------|------------|
| |  |


**As the administrator**

| **Expectation - Administrator** | **Result**|
|--------------|------------|
|  |  |


### Validator testing

- **CI Python Linter**

![]()


- **Lighthouse**

![]()

### Unfixed bugs

- The comments are acceptable.


## Deployment

The deployment was done after the tutorial in the course content using <https://www.heroku.com/>.

For deployment:
- A Heroku account must be created.
- Set your GitHub repository to public.
- Create a new app in Heroku with the following settings:
  - Add Python and Node.js (in this order!)
  - Add PORT as key and 8000 as value
- The Heroku App must be linked to the correct repo in GitHub
- Choose Automatic Deploys for easier handling.
- Then deploy
 
The link to the live page can be found here: [] (<>)


## Credits

### Content

The content of this project was inspired by the "Hello Django" and "I Think Therefore I Blog" project and the content of the course. In general, the following websites were used for inspiration:
  - <>
  

Inspirations for specific problems were taken from the following websites:
  - <>
  
### Media

Images were downloaded from <https://pixabay.com/de/>
- Login image <https://pixabay.com/de/illustrations/schach-hunde-haustier-schach-spiel-7802136/>


## Acknowledgements

- I would love to thank the following persons:
  - My mentor for his support
  - The Code Institute tutor support for their fast answers
  - My facilitator for her support
  - The slack community for their fast answers and support
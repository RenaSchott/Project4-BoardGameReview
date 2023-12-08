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

### Site goals

The site wants to challenge the user to .

### User stories

#### As a visitor

- 

#### As the administrator

- 

### Wireframes

Here are the drawings of the wireframes:

![]()


### Flow Chart

Here is the previously outlined flow chart, which contains parts of the actual project and of version 2:

![]()

### Method

#### POC (prove of concept)

- Log in and out
- Uploading/Deleting image
- Adding comments
- Adding reviews
- Editing reviews
- Rating system

#### MVP (minimum viable product)

- Interacting with an existing entry
    - Commenting on an entry
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
        - divided up for each year
        - divided into complexity
        - divided into family, connoisseur and expert board game
    - Images 
        - expand upload capacity
    - Adding chat/message function
    - Adding extra forum for further exchange

## Used Technologies

### Languages Used

- Python

### Framework, Libraries and Programs

- Frameworks 
    - Django
- Libraries 
    - 
- Moduls
    - 
- Programs
    - Balsamiq
        - was used to create the wireframes
    - Lucidchart
        - was used to create the flow chart
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

The content of this project was inspired by the Love Sandwiches project and the content of the course. In general, the following websites were used for inspiration:
  - <>
  

Inspirations for specific problems were taken from the following websites:
  - <>
  
### Media

- no media was used


## Acknowledgements

- I would love to thank the following persons:
  - My mentor for his support
  - The Code Institute tutor support for their fast answers
  - My facilitator for her support
  - The slack community for their fast answers and support
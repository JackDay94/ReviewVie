<h1 align="center">ReviewVie - Movie Review Website</h1>

## Introduction
ReviewVie is a Movie Review website that allows users to share their opinions on movies that they may or may not enjoy. The site allows users to browse for movies and rate them on a scale of 1-5 and leave a review of what their opinions on that movie was. Users can also request a new movie to be added to the website by filling out a form, which can then be checked and approved by site admins. The main aim of this site is to allow users to share their opinions on movies and help others with deciding what to watch. 

[The live site can be accessed here.](https://reviewvie.herokuapp.com/)

![Responsive check](readme-images/device-mockup.PNG)

## Table of Contents

1. [Intended Audience](#intended-audience)
    - [User Stories](#user-stories)
2. [Design](#design)
    - [Colours](#colours)
    - [Font styles](#font-styles)
    - [Wireframes](#wireframes)
3. [Agile Development](#agile-development)
4. [Data Model](#data-model)
    - [Database Schema](#database-schema)
5. [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
4. [Technologies](#technologies)
5. [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Manual Testing](#manual-testing)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
6. [Deployment](#deployment)
7. [Credits](#credits)
    - [Content](#content)

## Intended Audience
ReviewVie is intended for people who love movies and love to share their opinions on them. The users coming to this site will be looking to either share their opinions on movies that they have watched or wanting to read other user reviews to help them decide what movie(s) they want to watch.
Some may even want to add a movie that they just saw and really want to share their opinion on it and see what others have to say too.

### User Stories
Using github projects I was able to create a series of user stories related to the site. These can be found [here.](https://github.com/users/JackDay94/projects/3)

The user stories can be divided into the following Epics:
1. User Authentication:
    - As a site user I can register an account so that I can review and comment. (Must-have)
    - As a site user/ owner I can sign into and sign out of my account to access certain site features when I need to. (Must-have)
    - As a site user I can register and sign in using social media accounts to share my reviews on social media easier. (Could-have)
2. Engaging in reviews:
    - As a site user I can leave a review on a movie so that I can interact with the content. (Must-have)
    - As a site user I can edit and delete my reviews for movies to allow me to update my opinion on a movie or remove what I do not want anymore. (Should-have)
    - As a site user I can like / dislike reviews to interact with other users and share my opinion. (Could-have)
3. Browsing Movies:
    - As a site user I can select and view a movie and its reviews so that I can read about a movie and its reviews. (Must-have)
    - As a site user I can search for movies to allow me to find a specific movie faster. (Should-have)
    - As a site user I can view a list of movies that have been reviewed so that I can select a review to read. (Must-have)
    - As a site user I am able to be reccomended movies to help me decide what I should watch next. (Should-have)    
4. Adding and managing Movies and reviews:
    - As a site user/ owner I can add a new movie to be able to review and allow others to review it. (Must-have)
    - As a site owner I can create, read, update and delete movies to manage my site content. (Must-have)
    - As a site owner I can approve new movies added by users to review their legitimacy. (Must-have)
    - As a site owner / user I can create, read, update and delete my reviews for movies to give me full control over my own reviews. (Must-have)
5. Site Navigation:
    - As a site user/ owner I can navigate pages of the site to find the content I wish to see with ease. (Must-have)
    - As a site owner / user I can navigate between pages of reviews/movies to explore more content of the site. (Must-have)
6. Profile:
    - As a site user I can set my favourite director/genre etc. so that I can be reccomended movies that suit my tastes best. (Should-have)

## Design

### Colours
The main colours of the site are mostly dark, with the body being a dark gray and the navbar and footer both being dark. The main content container of the site is a lighter gray with a 40% opacity which allows the dark gray background pattern to slightly be seen through the container. I chose this colour scheme to make the colourful images of the movies stand out, making them the main focus of the site.
Other areas of the site, such as the login, logout and sign up forms use a card with a dull white background. This helps to present the forms in an easier to read format. I tried to keep the black, gray and white colour scheme constant throughout the site to help provide a feeling of fluidity when exploring the site.

### Font styles
As the site is based around viewing and reviewing movies, I wanted to use a simple and readable font style for the site. For this I used the font style 'Lato' from Google Fonts as I felt that it was easily readable. Many of the main headings of the site use bold font weights to distinguish them from the rest of the content. Other smaller text that uses bold styles include the username of users who review on movies, to seperate their username from the rest of the review content.

### WireFrames
I used Balsamiq wireframes to create the wireframes for this project. Most of the wireframes reflect the final project, but their are some differences to the design.
<details>
<summary>Desktop</summary>
Home page

![Desktop Wireframe home](readme-images/wireframes/desktop/wireframe-desktop-home.PNG)

All movies

![Desktop Wireframe allmovies](readme-images/wireframes/desktop/wireframe-desktop-allmovies.PNG)

Movie Detail

![Desktop Wireframe moviedetail](readme-images/wireframes/desktop/wireframe-desktop-detail.PNG)

Add Movie

![Desktop Wireframe addmovie](readme-images/wireframes/desktop/wireframe-desktop-addmovie.PNG)

Register and Sign in

![Desktop Wireframe register signin](readme-images/wireframes/desktop/wireframe-desktop-register-signin.PNG)
</details>

<details>
<summary>Mobile</summary>
Home and Details

![Mobile Wireframe home and details](readme-images/wireframes/mobile/wireframe-mobile-home-details.PNG)

All movies

![Mobile Wireframe allmovies](readme-images/wireframes/mobile/wireframe-mobile-allmovies.PNG)

Add movie

![Mobile Wireframe addmovie](readme-images/wireframes/mobile/wireframe-mobile-addmovie.PNG)

Register and Sign in

![Mobile Wireframe register signin](readme-images/wireframes/mobile/wireframe-mobile-register-signin.PNG)
</details>

## Agile Development
For this project I employed an Agile approach through the use of github projects to plan and track user stories through the course of development.
At the start of the project I created user stories that would fit the goal of the project and labelled these based on priority as either must-have, should-have or could-have. Initially all 17 user stories were placed in the 'Todo' column, and as the project progressed I moved these to the 'In progress' column. When a user story was completed, I then moved it to the 'Done' column and moved on to the next.
Overall a total of 14/17 user stories were completed.

![User Stories](readme-images/user-stories.PNG)

The user stories I did not manage to complete were:
- USER STORY: Sign in using social media accounts: As a site user I can register and sign in using social media accounts to share my reviews on social media easier. (could-have)
- USER STORY: Movie reccomendations: As a site user I am able to be reccomended movies to help me decide what I should watch next. (should-have)
- USER STORY: Like / Dislike reviews: As a site user I can like / dislike reviews to interact with other users and share my opinion. (could-have)

These features were unimplemented due to time constraints, but are not required for the site to function as needed.

## Data Model

### Database Schema

![ER Diagram](readme-images/er-diagram.PNG)

The ER Diagram for this project shown above gives the relationship between the data models used.

- The profile model extends the user model through a one-to-one relationship and contains its own optional fields that a user can use to customise their profile.
- Using signals, a new profile is created for every new user.
- The Review model author field uses a foreign key relationship between the user model id field.
- The Review model movie field shares a foreign key relationship between the Movie model id field.

## Features

### Navbar
- The navbar displays the main site navigation for users to reach other pages.

![Navbar normal](readme-images/features/navbar-normal.PNG)

- When a user is signed in the navbar displays more options.

![Navbar user](readme-images/features/navbar-user.PNG)

- When a superuser is signed in, the Admin panel becomes visible

![Navbar admin](readme-images/features/navbar-admin.PNG)

- The navbar is fully responsive and shrinks to a menu on smaller screens.

![Navbar small](readme-images/features/navbar-small.PNG)

### Footer
- The footer displays icons which link to social media sites.

[!Footer](readme-images/features/footer.PNG)

### Home
- The home page displays a variety of information for users. The first thing they see is the top rated movie on the site.

![Top rated](readme-images/features/top-rated.PNG)

- The next four highest rated movies, latest movies and latest reviews are also shown here, with a button leading to all the other movies at the bottom.

![Home](readme-images/features/home-img.PNG)

### All Movies
- The All movies page displays all of the approved movies in a list. There is also a search feature for users to search for movies by name, director or genre.

![All movies](readme-images/features/all-movies.PNG)

### Movie Detail
- The movie detail page displays the details of a particular movie and its corresponding reviews. From this page, signed in users can add a review to the movie.
- Users can also choose to edit or delete their reviews from this page, which takes them to the corresponding edit/delete page.
- Superusers can choose to edit/delete the movie from this page.

![Movie Detail](readme-images/features/movie-detail1.PNG)

![Movie review](readme-images/features/movie-detail2.PNG)

### Add Movie
- This page allows users to request to add a movie by filling out the form fields.
- The admin can then choose to approve this from the admin panel.

![Add movie](readme-images/features/add-movie.PNG)

### Edit Review
- Users can edit their review for a movie on this page by filling out the fields and submitting.
- This page can only be accessed by the user who wrote the review and superusers.

![Edit review](readme-images/features/edit-review.PNG)

![Access denied](readme-images/features/access-denied.PNG)

### Delete Review
- This page displays the review the user is about to delete and then deletes it when they submit.
- Only accessed by the user who wrote the review and superusers.

![Delete review](readme-images/features/delete-review.PNG)

### Edit Movie
- This page displays the current movie details and allows a superuser to edit the movie by submitting the form.
- This page is only accessible by superusers and normal users are redirected.

![Edit movie](readme-images/features/edit-movie.PNG)
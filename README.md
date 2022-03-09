# Armoire

Welcome to Armoire. Armoire is a web application that lets you digitize your wardrobe to easily view your clothes at a glance. Create outfits and pair your articles of clothing with each other to have an ensemble for each day of the week. All those old sweaters in the back of your closet won't be as easily forgotten anymore now that it is on Armoire!

## Distinctiveness and Complexity

Throughout the course, I have utilized a lot of front and back end web programming, and in this web application, Armoire, I fully believe that I applied everything I had learned throughout the course to develop this site to what it has become.

Armoire is distinct in that it allows users to upload their own items and clothing onto the database under their account for their own viewing. I pushed what I have learned in projects such as *commerce* and *network* to develop a unique experience with Armoire.

Armoire is complex because I wanted to add features that make it more dynamic, such as simple animations and scrolling image carousels. I wanted to stray away from a static looking website. Outside of the programming itself, I flexed a little bit of graphic design muscle and took the time to develop a brand for Armoire to give it the look and feel that I wanted. 

## What's contained in these files

#### armoire.js

This is the general javascript file that holds some of the basic functions for the application: 
- showing and hiding the forms to create the outfits and pieces
- showing and hiding the outfits and pieces themselves when the forms are requested
- buttons that apply filters to view specific categories of pieces
- simple user interaction with said buttons
- adding and removing pieces from outfits
- deleting outfits and pieces

#### carousel.js

I wanted to create a dynamic view of a user's outfits and pieces. This javascript file contains all the code necessary to create functioning carousels in the HTML pages. It populates on the page dynamically so that each user has a unique experience.

#### styles.css

Just basic styling of items such as buttons, carousel elements, image sizing and position, etc.

#### addpiece.html

Form to create pieces.

#### index.html

The landing page for visitors.

#### layout.html

Contains the navigation bar and footer HTML for all the other pages.

#### login.html

Page for returning users to log into their account.

#### mycloset.html

The logged-in user's main page. Contains all their current outfits and pieces. From here, the user is able to scroll through their outfits and pieces. The outfit cards are links to each individual outfit page. The user is also able to create new pieces and outfits as well as delete unwanted ones.

#### outfit.html

This is the template for each outfit that has been created. Showcases the user's pieces they chose to be in said outfit. User also has the option to click pieces on and off to add and remove pieces from the outfit.

#### register.html

Page for new users to sign up for an account.

## How to run application

At the moment, Armoire is only accessible locally via Django's runserver command. I plan on hosting this website publicly at some point and as a mobile app for ease of use. 

## Final Words

I had a great time doing CS50 W and have learned a lot through my web programming journey. I plan to add more features in the near future, some of which include a view enlarged image function, and make use of the extra attributes that the pieces have (like the colors and styles).

I was inspired to create Armoire by my partner and her wanting to organize the clothes in her closet. I thought that this application would help her in doing just that. I am very happy with the outcome of Armoire and hope that others find it useful as well!

## Demo Video

https://youtu.be/TxlQmzSL8LQ
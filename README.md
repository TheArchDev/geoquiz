# geoquiz
# https://young-brushlands-36442.herokuapp.com/
Summary

An early-stage Django project hosted on Heroku. A basic geography quiz app for learning countries and their capitals, and an opportunity for me to experiment with different technologies.

Functionality

Users must create an account and login to use the main site. They can view a list of all countries in the world, their capitals and which regions they are found in. Users can then also take a quiz in a selected region, either being asked for a country's correct capital, or a capital's correct country. After the quiz, the results are shown and all the correct answers.

Technologies Used

Python/Django web framework 
Back-end: SQL (SQLite w/local, PostGres w/Heroku)
Front-end: HTML/CSS, Bootstrap, JavaScript, jQuery
Restful API to populate database. (All country information courtesy of http://restcountries.eu/)

Roadmap - major aims

Incorporating flag images, to allow for 6 different quiz types: a combination of country, capital and flag (in both directions).
Statistics page: for users to see how their success rate for different countries, and how all users perform. Visualisation of this data. SQL infrastructure is already in place, tracking every quiz started, every question asked and whether it was answered (in)/correctly
Improvement of front-end (further work with Bootstrap).
Free-mode quiz: allow user to do as many questions as they want in a row (until they hit stop), using the whole world as the region.
Random quiz: each question will be of a different type, rather than the whole quiz just being eg country-to-capital.


# ⚽ ChampPredict

ChampPredict is a Django web application that allows users to predict football scores for fixtures in the English Football League Championship.

The Championship is one of the most competitive football leagues in the world but is often overlooked by prediction platforms that focus on the Premier League, Champions League or international tournaments. ChampPredict aims to provide a dedicated prediction platform specifically for Championship supporters.

Users submit predictions before kickoff and earn points based on the accuracy of their predictions once match results are entered.

---

## 📑 Table of Contents

- [Project Goals](#-project-goals)
- [User Stories](#-user-stories)
- [Technologies Used](#-technologies-used)
- [Project Status](#-project-status)
- [Features](#-features)
- [Planned Features](#-planned-features)
- [UX Design](#-ux-design)
- [Wireframes](#-wireframes)
- [Database Schema](#-database-schema)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Security](#-security)
- [Credits](#-credits)
- [Future Features](#-future-features)

---

## 📌 Project Goals

- Allow registered users to submit and manage predictions for Championship fixtures.
- Organise fixtures by matchweek for easy navigation.
- Hide predictions until kickoff to prevent copying.
- Display a leaderboard showing participant scores.

---

## 👤 User Stories

### Visitor

- As a visitor, I want to view upcoming fixtures so that I can see which matches are available for prediction.
- As a visitor, I want to see the leaderboard so that I can understand how participants are performing.

### Registered User

- As a registered user, I want to create predictions so that I can participate in the competition.
- As a registered user, I want to edit my prediction before kickoff so that I can change my mind.
- As a registered user, I want predictions to remain hidden until kickoff so that users cannot copy predictions.
- As a registered user, I want to see other users’ predictions after kickoff so that I can compare opinions.
- As a registered user, I want predictions to be locked once the fixture has kicked off so that predictions remain fair.

### Site Administrator

- As an administrator, I want to add teams so that fixtures can be created.
- As an administrator, I want to add fixtures so that users can predict upcoming matches.
- As an administrator, I want to add results so points can be calculated.

---

## 🛠 Technologies Used

- Python – primary programming language
- Django – web framework used to build the application
- PostgreSQL – relational database used in production
- HTML5 – page structure
- CSS3 – styling
- Bootstrap – responsive layout and UI components
- JavaScript – front-end interactivity
- Git – version control
- GitHub – repository hosting
- Heroku – cloud hosting platform used for deployment

---

## 🧱 Frameworks & Libraries

- Django authentication system
- Bootstrap for responsive layout
- Gunicorn – WSGI server used in production
- WhiteNoise – static file serving for Django
- dj-database-url – database configuration helper
- psycopg2-binary – PostgreSQL database adapter

---

## 🚧 Project Status

This project is currently under development as part of the Level 5 Diploma in Web Application Development.

Core backend functionality including fixture modelling, prediction logic and points calculation has been implemented. 

The next development milestone focuses on building front-end pages allowing users to view fixtures, submit predictions and track their performance via the leaderboard.

---

## ⭐ Features

- Teams are stored once in the database and reused across fixtures.
- Fixtures link two teams together using relational database relationships.
- Fixtures are organised by season and matchweek.
- Validation prevents the same team being selected as both the home and away team in a fixture.
- Fixtures are automatically ordered by kickoff time.
- Database constraints prevent duplicate fixtures for the same season, matchweek and teams.
- Users can submit score predictions for fixtures.
- Prediction records store timestamps showing when predictions were created and last updated.
- Predictions are automatically locked once the fixture kickoff time has passed to ensure fairness.

---
## Permissions

- Visitors can browse fixtures and view leaderboard information.
- Registered users must be logged in to create and manage predictions.
- Administrators can manage teams, fixtures and results through the Django admin panel.


---

## 📂 Planned Features

- User authentication (signup/login)
- Fixture list organised by matchweek
- Fixture detail pages
- Prediction creation and editing
- Prediction locking after kickoff
- Leaderboard displaying user scores
- Admin panel for managing teams, fixtures and results
- Prediction confirmation screen allowing users to review their selections before final submission.

---

## 🎨 UX Design

_To be completed during development._

---

## 🧩 Wireframes

_To be completed during the design stage._

---

## 🗄 Database Schema

The application uses a relational database structure with the following core models:

- Team – stores football clubs participating in the Championship.
- Fixture – represents a scheduled match between two teams.
- Result – stores the final score of a fixture.
- Prediction – stores a user’s predicted score for a fixture.

### Relationships

- A **User** can create multiple **Predictions**
- Each **Prediction** belongs to one **Fixture**
- Each **Fixture** has one **Result**
- Each **Fixture** references two **Teams** (home and away)

This relational structure ensures fixtures and predictions remain consistent and prevents duplicated team data.

---

## 🧪 Testing

### Unit Testing

- Tested prediction points calculation with an exact score match and confirmed the method returned 3 points.
- Tested prediction points calculation with a correct result but incorrect score and confirmed the method returned 1 point.
- Tested prediction points calculation with an incorrect result and confirmed the method returned 0 points.
- Tested prediction points calculation where no result existed and confirmed the method returned None.

---

## 🚀 Deployment

This application is deployed using **Heroku**.

### Deployment Steps

1. Install deployment dependencies including Gunicorn, WhiteNoise and dj-database-url.
2. Create a `Procfile` to define the web process:
```
web: gunicorn champpredict.wsgi
```
3. Configure environment variables such as `SECRET_KEY` and `DEBUG` using Heroku config variables.
4. Add a Heroku PostgreSQL database add-on.
5. Push the project to Heroku using: 
```
git push heroku main
```
6. Run database migrations on Heroku:
```
heroku run python manage.py migrate
```
7. The application can then be accessed via the Heroku app URL.

---

### Development Workflow

1. Changes are committed locally using Git.
2. Code is pushed to GitHub for version control.
3. The application is deployed to Heroku using:

```
git push heroku main
```

---

## 🌐 Live Application

The deployed application can be accessed here:

[ChampPredict Live Site](https://champ-predict-app-fa154106af37.herokuapp.com/)

---

## 🔐 Security

_To be documented during development._

---

## 🙏 Credits

_To be added during development._

---

## 🔮 Future Features

- Football Pontoon prediction game
- Private prediction leagues
- Prediction statistics and insights
- Email confirmation receipts providing users with a timestamped summary of their submitted predictions.


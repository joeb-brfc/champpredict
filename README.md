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

- Allow users to predict Championship match results.
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

Core features such as fixtures, predictions, and leaderboard functionality will be implemented during development.

---

## ⭐ Features

- Teams are stored once in the database and reused across fixtures.
- Fixtures link two teams together using relational database relationships.
- Fixtures are organised by season and matchweek.
- Validation prevents the same team being selected as both the home and away team in a fixture.
- Fixtures are automatically ordered by kickoff time.
- Database constraints prevent duplicate fixtures for the same season, matchweek and teams.

---

## 📂 Planned Features

- User authentication (signup/login)
- Fixture list organised by matchweek
- Fixture detail pages
- Prediction creation and editing
- Prediction locking after kickoff
- Leaderboard displaying user scores
- Admin panel for managing teams, fixtures and results

---

## 🎨 UX Design

_To be completed during development._

---

## 🧩 Wireframes

_To be completed during the design stage._

---

## 🗄 Database Schema

_To be completed once models are implemented._

---

## 🧪 Testing

_To be documented during development._

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


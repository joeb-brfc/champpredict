# ⚽ ChampPredict

ChampPredict is a Django web application that allows users to predict football scores for fixtures in the English Football League Championship.

The Championship is one of the most competitive football leagues in the world but is often overlooked by prediction platforms that focus on the Premier League, Champions League or international tournaments. ChampPredict aims to provide a dedicated prediction platform specifically for Championship supporters.

Users submit predictions before kickoff and earn points based on the accuracy of their predictions once match results are entered.

---


## 🌐 Live Application

The deployed application can be accessed here:

[ChampPredict Live Site](https://champ-predict-app-fa154106af37.herokuapp.com/)

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
- [Permissions](#permissions)
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

## 🚀 Key Features (Recent Improvements)

### Matchweek-Based Fixture Organisation

Fixtures are grouped by matchweek instead of displayed as a flat list.

This improves:
- clarity when browsing fixtures
- alignment with real football scheduling
- scalability as more fixtures are added

Each matchweek now includes a direct link to submit predictions.

---

### Bulk Matchweek Predictions

Users can submit predictions for all fixtures in a matchweek from a single page.

- multiple fixtures displayed together
- existing predictions preloaded
- locked fixtures cannot be edited
- users can clear predictions before kickoff

This removes the need to enter predictions one fixture at a time.

---

### My Predictions Page Improvements

Predictions are grouped into:

- Upcoming (editable)
- Awaiting Results
- Completed (scored)

This makes it easier to understand prediction status at a glance.

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

The application now supports:

- browsing Championship fixtures
- viewing fixture details
- submitting score predictions
- updating predictions before kickoff
- viewing a leaderboard ranking users by prediction points
- viewing a personal **My Predictions** page showing submitted predictions and earned points
- submitting **bulk predictions for an entire matchweek** from a single page
- receiving confirmation messages when predictions are created or updated
- authentication pages (login and signup) customised using Django template overrides and Bootstrap styling

---

## ⭐ Features

### Fixture Management

- Teams are stored once in the database and reused across fixtures.
- Fixtures link two teams together using relational database relationships.
- Fixtures are organised by season and matchweek.
- Fixtures are automatically ordered by kickoff time.
- Validation prevents the same team being selected as both the home and away team.
- Database constraints prevent duplicate fixtures for the same season, matchweek and teams.

### Championship Dataset

The database currently contains the full set of English Championship teams.

Fixtures are organised by season and matchweek to reflect a realistic football schedule.  
This allows predictions and leaderboard scoring to operate using real-world match scenarios.

### Fixture Pages

- Users can browse a list of upcoming fixtures.
- Clicking a fixture opens a **fixture detail page**.
- The fixture detail page displays match information and allows logged-in users to submit predictions.
- Fixtures are grouped by matchweek to improve navigation and user experience.

### Fixture Navigation Enhancements

- The fixtures page acts as the primary entry point for submitting predictions.
- Logged-in users are presented with dynamic prediction links for each matchweek shown on the fixtures page.
- Logged-out users are shown a prompt to log in before making predictions.
- This removes the need for hardcoded navigation links and ensures matchweek selection is always based on live fixture data.

This creates a smoother flow, taking users from browsing fixtures straight into submitting their predictions.

Matchweek prediction links are dynamically generated per matchweek rather than relying on a single "current matchweek" value.

### Matchweek Predictions

To improve the user experience, the application allows users to submit predictions for an entire matchweek from a single page.

Instead of navigating into each fixture individually, users can now enter predictions for all fixtures in a matchweek simultaneously.

Key functionality includes:

- A dedicated **Matchweek Predictions** page displaying all fixtures within a selected matchweek.
- Each fixture contains its own prediction form fields.
- Existing predictions are automatically preloaded into the form if they already exist.
- Blank fixtures can be skipped without affecting other predictions.
- Fixtures that have passed their kickoff time are automatically locked and cannot be edited.
- A confirmation message is displayed when predictions are successfully saved.

This removes the need to go in and out of individual fixtures, making the process much quicker and easier for the user.

Access to matchweek predictions is integrated into the fixtures page rather than the global navigation. 

The application dynamically generates a "Predict all Matchweek X games" link based on fixture data, ensuring the correct matchweek is passed to the prediction view without hardcoding values.

This approach improves scalability and ensures users always access the correct matchweek when submitting bulk predictions.

- Users can clear their saved predictions for a selected matchweek before kickoff if they want to start again.

### Authentication

- Visitors can browse fixtures and view leaderboard data without logging in.
- Navigation links are conditionally displayed based on authentication status.
- Only authenticated users can access prediction-related features such as:
  - submitting predictions
  - editing predictions
  - viewing personal predictions
- Logged-out users are prompted to log in when attempting to access prediction functionality.

This ensures a clear separation between public browsing and authenticated interaction.

## 🔄 Prediction Workflow

1. A visitor browses the fixture list.
2. Selecting a fixture opens the fixture detail page.
3. Logged-in users can submit a predicted score.
4. If a prediction already exists, the form automatically loads the saved prediction.
5. Submitting the form saves or updates the user's prediction.
6. A confirmation message is displayed to inform the user that their prediction has been saved.
7. Once kickoff time has passed, predictions become locked and cannot be modified.

### Prediction System

- Registered users can submit score predictions for fixtures.
- Each user can submit **one prediction per fixture**.
- Users can **edit their prediction before kickoff**.
- Existing predictions are automatically loaded into the form when revisiting a fixture.
- Predictions are saved with timestamps showing when they were created and last updated.
- Predictions are automatically **locked once kickoff time has passed** to ensure fairness.
- After submitting or updating a prediction, users receive a confirmation message indicating that their prediction has been successfully saved.
- Points are awarded based on prediction accuracy:
  - **3 points** for an exact score prediction
  - **1 point** for a correct match outcome
  - **0 points** for an incorrect prediction

### Data Validation

The application includes several validation rules to ensure data consistency:

- A fixture cannot be created where the home and away teams are the same.
- Each user can only submit one prediction per fixture.
- Predictions cannot be modified once the fixture kickoff time has passed.
- Database constraints prevent duplicate fixtures for the same season, matchweek and teams.

### Leaderboard

- A leaderboard page ranks users based on the total points earned from their predictions.
- Points are calculated using the `calculate_points()` method in the Prediction model.
- Only predictions for fixtures with recorded results contribute to leaderboard scores.
- Users are displayed in descending order based on total points.

### My Predictions

- Registered users can view a dedicated **My Predictions** page.
- Predictions are now grouped into three clear sections to improve usability:

  - **Upcoming Predictions**
    - Displays fixtures that have not yet kicked off
    - Predictions can still be edited

  - **Awaiting Results**
    - Displays fixtures that have kicked off but do not yet have a recorded result
    - Predictions are locked and cannot be modified

  - **Completed Predictions**
    - Displays fixtures with recorded results
    - Shows:
      - predicted score
      - actual result
      - points earned

- This grouping removes duplication and provides a clearer overview of prediction status.

### Admin Management

Administrators manage the core data of the application through the Django admin panel.

Administrators can:

- add Championship teams
- create fixtures between teams
- organise fixtures by matchweek
- record final match results
- review submitted user predictions

The admin interface allows the application to operate without requiring manual database changes.

### User Feedback Messages

The application uses Django's messaging framework to provide feedback when predictions are created or updated.

Users receive confirmation messages such as:

- "Prediction saved successfully."
- "Prediction updated successfully."
- "Matchweek predictions saved successfully."

This helps users understand when their actions have worked as expected.


---

## 📂 Planned Features

- Prediction statistics and insights
- Private prediction leagues for groups of users
- Email confirmation receipts for submitted predictions
- Improved UI styling and responsive layout enhancements
- Admin tools for managing full Championship fixture schedules

---

## 🎨 UX Design

### Navigation Design

The navigation structure was refined to improve usability and clarity:

- Global navigation provides access to core pages such as fixtures, leaderboard and user predictions.
- Context-specific actions, such as submitting matchweek predictions, are accessed through the fixtures page rather than the navigation bar.
- This prevents clutter and ensures users interact with features in a logical, data-driven flow.

This design choice aligns with real-world application patterns where actions are tied to relevant data views.

### My Predictions UX Improvements

The My Predictions page was redesigned to improve clarity and reduce repetition.

Previously, all predictions were displayed in a single table, which made it difficult for users to understand the status of each prediction.

The updated design separates predictions into:

- upcoming (editable)
- awaiting results
- completed (scored)

This approach aligns with real-world prediction platforms and improves usability by allowing users to quickly understand:

- which predictions they can still change
- which are waiting for results
- which have been scored

### Authentication UX Improvements

The default authentication pages provided by django-allauth were replaced with custom templates to ensure consistency with the rest of the application.

Improvements include:

- centred form layout using Bootstrap grid system
- clear headings and helper text to guide users
- consistent button styling and navigation links
- improved spacing and readability across screen sizes

This ensures users have a smoother and more intuitive experience when signing in or creating an account.

### Homepage and Fixture Page Improvements

The homepage was expanded from a simple placeholder into an introduction to the application, giving visitors a clearer understanding of the platform's purpose and planned direction.

The fixtures page was also redesigned using Bootstrap cards, buttons and grouped layout styling to improve readability and make matchweeks easier to browse.

These changes helped the interface feel more consistent and better aligned with a football-themed application.

---

## 📸 Screenshots

### Fixture List

Displays all upcoming fixtures organised by kickoff time.

*(Screenshot to be added)*

### Fixture Detail

Shows match information and allows logged-in users to submit predictions.

*(Screenshot to be added)*

### Leaderboard

Displays users ranked by the total points earned from their predictions.

*(Screenshot to be added)*

### My Predictions

Displays all predictions submitted by the logged-in user along with results and points earned.

*(Screenshot to be added)*

### Login Page

Displays the customised sign in page using Django allauth template overrides and Bootstrap styling.

*(Screenshot to be added)*

### Sign Up Page

Displays the customised registration page with consistent layout and styling.

*(Screenshot to be added)*

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

This structure keeps the data consistent and avoids duplicating team information across multiple fixtures.

---

## 🔐 Permissions

- Visitors can browse fixtures and view leaderboard information.
- Registered users must be logged in to create and manage predictions.
- Administrators can manage teams, fixtures and results through the Django admin panel.

---

## 🧪 Testing

### Unit Testing

- Tested prediction points calculation with an exact score match and confirmed the method returned 3 points.
- Tested prediction points calculation with a correct result but incorrect score and confirmed the method returned 1 point.
- Tested prediction points calculation with an incorrect result and confirmed the method returned 0 points.
- Tested prediction points calculation where no result existed and confirmed the method returned None.

### Prediction Form Testing

- Verified that logged-in users can submit predictions through the fixture detail page.
- Confirmed that users cannot create multiple predictions for the same fixture.
- Confirmed that existing predictions are automatically loaded into the form.
- Verified that submitting the form again updates the existing prediction instead of creating a duplicate.
- Confirmed that a success message is displayed when a prediction is saved or updated.

### Matchweek Prediction Testing

- Verified that users can open the Matchweek Predictions page for a selected matchweek.
- Confirmed that prediction input fields appear for every fixture in the matchweek.
- Confirmed that existing predictions are automatically loaded into the form.
- Verified that submitting the form saves multiple predictions simultaneously.
- Confirmed that fixtures with kickoff times in the past are locked and cannot be modified.
- Verified that a confirmation message is displayed when matchweek predictions are saved.
- Verified that the matchweek prediction link dynamically uses fixture data rather than a hardcoded value.
- Confirmed that logged-out users are prompted to log in instead of accessing prediction functionality.
- Verified that navigation links update correctly depending on authentication state.
- Verified that users can clear saved predictions for a selected matchweek.
- Confirmed that only unlocked predictions are cleared.
- Verified that a confirmation message is displayed after clearing predictions.

### Leaderboard Testing

- Verified that users appear on the leaderboard after submitting predictions.
- Confirmed that leaderboard rankings update based on total points earned.
- Confirmed that predictions without results do not contribute to leaderboard scores.

### Validation and Workflow Testing

- Verified that a fixture cannot be created where the home and away team are the same.
- Confirmed that a team cannot be assigned to more than one fixture in the same matchweek.
- Verified that predictions cannot be updated after fixture kickoff.
- Confirmed that bulk matchweek prediction entry validates incomplete score pairs.
- Verified that matchweek predictions can be saved for multiple fixtures in a single submission.
- A validation bug was identified in the Fixture.clean() method where one team check was incorrectly placed outside the loop iterating through existing fixtures. This caused an UnboundLocalError when adding fixtures through the admin panel. The issue was resolved by moving both validation checks inside the loop.

### My Predictions Grouping Testing

- Verified that predictions are correctly grouped into:
  - upcoming (pre-kickoff)
  - awaiting results (post-kickoff, no result)
  - completed (result available)

- Confirmed that:
  - predictions appear in only one section at a time
  - predictions move between sections as fixture status changes
  - completed predictions display correct match results and calculated points

- Tested behaviour across multiple fixtures with different kickoff times and result states to ensure accurate grouping logic.

### Deployment Testing

- After deploying new code to Heroku, the application initially returned a **500 server error** on fixture pages because the production database schema had not yet been updated. This was resolved by running:
  `heroku run python manage.py migrate`

- When moving local fixture data to Heroku using `dumpdata` and `loaddata`, an encoding issue occurred because the exported JSON file was not saved in the correct UTF-8 format. This was resolved by resaving the fixture file as **UTF-8 without BOM** before loading it into Heroku.

- This highlighted that the **local database and Heroku production database are separate**, so data must either be entered manually in production or transferred using fixture files.

- The Django admin interface appeared unstyled in the local development environment, with missing CSS and layout issues. This was caused by the `DEBUG` setting being evaluated as `False`, which prevented Django from serving static files during development.

- The issue was resolved by updating the `DEBUG` setting to default to `True` locally unless explicitly overridden by an environment variable. Additionally, the `STATIC_URL` setting was corrected to include a leading slash (`/static/`), ensuring static file paths were resolved correctly.

- This highlighted the importance of clearly separating development and production configuration, particularly when using environment variables.

- Verified that fixture grouping and matchweek prediction links display correctly in production after deployment.


### Development vs Production Database

Local development uses a **SQLite database**, while the production application on Heroku uses a **PostgreSQL database**.

Because these environments are separate, predictions created locally do not appear on the live application. Users must submit predictions through the deployed Heroku application for them to be stored in the production database.

This separation allows development changes to be tested locally without affecting live user data.

### Frontend and Responsiveness Testing

- The **My Predictions** page was tested across different screen sizes using browser developer tools.
- Bootstrap’s responsive grid system and `table-responsive` class were used to ensure tables remain usable on smaller screens.
- Verified that:
  - tables scroll horizontally on mobile devices instead of breaking layout
  - text remains readable without overlapping
  - navigation and headings scale correctly across screen sizes
- Tested pages on desktop and simulated mobile view to confirm consistent layout and usability.
- Login and signup pages were tested after overriding django-allauth templates to ensure:
  - custom templates render instead of default allauth pages  
  - base layout and navigation are consistent across authentication pages  
  - forms display correctly using Bootstrap styling  
- Verified that authentication pages remain usable on smaller screen sizes  
- Fixture list and homepage were also visually tested after styling updates to ensure consistent spacing, alignment and readability
- Verified that Bootstrap components (cards, buttons and layout grid) render correctly across pages

- Verified that links between login and signup pages work correctly after custom template overrides were added

---

## ⚠️ Development Challenges

### Form Handling Challenges

While building the bulk matchweek predictions feature, I initially tried to handle both saving and clearing predictions within the same form. 

This caused issues because the backend could not clearly distinguish which action the user intended, leading to unreliable behaviour.

To resolve this, I separated the functionality into two forms:
- one for saving predictions
- one for clearing predictions

This made the request handling much clearer and ensured that each action triggered the correct logic in the view.

### Improving Prediction Visibility

During development, the My Predictions page initially displayed all predictions in a single table.

This created a poor user experience, as users could not easily distinguish between:

- editable predictions
- locked predictions
- completed predictions

To improve this, the page was redesigned to group predictions based on fixture status.

This required:

- updating backend logic to categorise predictions
- restructuring the template into multiple sections

This significantly improved usability and reduced confusion when reviewing predictions.

### Environment and Data Sync Challenges

Several real-world issues were encountered and resolved during development:

- Local and production databases were not synchronised, resulting in missing fixtures locally. This was resolved using `dumpdata` and `loaddata`.

- Fixture import initially failed due to encoding issues. This was fixed by saving the JSON file as UTF-8.

- Static files failed to load locally due to incorrect DEBUG configuration. This was resolved by ensuring DEBUG=True in development.

- A validation bug in the Fixture model caused an UnboundLocalError. This was fixed by correcting the loop structure.

These challenges improved understanding of deployment environments, data handling and debugging in Django.

### Static Files and CSS Issue

During development, an issue occurred where custom CSS was not being applied to the application.

### Issue

- The application appeared unstyled despite linking the stylesheet in the base template.
- Inline styles worked, confirming that templates were rendering correctly.
- Attempting to access the stylesheet directly initially returned a 404 error.

### Investigation

- Checked that `{% load static %}` and the `<link>` tag were correctly set in the template.
- Tested inline CSS to confirm styling could be applied.
- Used Django’s static file lookup command:

```bash
python manage.py findstatic predictor/style.css --verbosity 2
```

This confirmed that Django could not locate the stylesheet.

### Resolution

The issue was caused by an incorrect static file structure.

The stylesheet was originally stored in:

```text
predictor/static/css/style.css
```

It was moved to a namespaced location:

```text
predictor/static/predictor/css/style.css
```

The template was updated accordingly:

```html
<link rel="stylesheet" href="{% static 'predictor/css/style.css' %}">
```

After restarting the server, the CSS loaded correctly.

### Outcome

- Custom styling now applies across all pages
- Improved understanding of Django static file structure and debugging process

### Authentication Template Override (Allauth)

During development, the default django-allauth login and signup pages were displayed instead of the custom templates.

### Issue

- Custom templates were created but not being used
- The default allauth "Menu: Sign In / Sign Up" layout continued to appear
- This indicated that Django was not locating the override templates

### Investigation

- Confirmed that template inheritance (`{% extends "predictor/base.html" %}`) was correct
- Reviewed Django template loading behaviour and how third-party templates are resolved
- Identified that allauth uses the template path `account/login.html` and `account/signup.html`

### Resolution

Custom templates were moved to match the expected structure:

```
templates/account/login.html
templates/account/signup.html
```

This ensured Django could override the default allauth templates correctly.

### Outcome

- Custom login and signup pages now render using the main site layout
- Styling is consistent with the rest of the application
- Improved understanding of how Django resolves templates for third-party apps

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

## 🔐 Security

_To be documented during development._

---

## 🙏 Credits

Leaderboard ranking logic uses Python’s built-in `sorted()` function with a lambda expression to order users by total prediction points.

Python documentation reference:  
https://docs.python.org/3/library/functions.html#sorted

### Form Validation

Prediction form validation follows standard Django `ModelForm` validation patterns to ensure that both home and away scores are entered together when submitting predictions.

Reference:  
https://docs.djangoproject.com/en/stable/ref/forms/validation/

### Bootstrap

This project uses the Bootstrap framework to provide responsive layout and UI components such as:

- grid system for layout structure  
- tables for displaying prediction data  
- cards for grouping content  
- badges for visual status indicators  

Bootstrap classes were used and adapted to fit the ChampPredict design rather than writing all styling from scratch.

Reference:  
https://getbootstrap.com/

Bootstrap was also used to enhance the layout and styling of authentication pages by applying its grid system and form components to Django allauth templates.

---

## 🔮 Future Features

- Football Pontoon prediction game
- Private prediction leagues
- Prediction statistics and insights
- Expand the fixture detail page into a richer match preview area, including team form, league position, head-to-head records, and notable fixture facts to help users make more informed predictions.
- Email confirmation receipts providing users with a timestamped summary of their submitted predictions.


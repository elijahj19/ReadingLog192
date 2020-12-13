# ReadingLog192
By Elijah Jasso & Subin Kim

## How to Run

1. pip install all necessary packages
2. Run the command 'python manage.py runserver' in the terminal
3. Open up the local server link found in the terminal

## Routes and Description

- **admin/** : allows for administrative management of app
- **/** : (implicit slash) shows the landing page with basic introduction to the app and invitation to login/ sign up
- **accounts/** : shows not-logged-in users the signup/login page and shows logged-in users the option to logout
- **login/** : logs in the user with specified username and password in the request.POST
- **signup/** : signs up the user with specified email, username, and password in the request.POST
- **logout/** : logs out the currently logged-in user
- **dashboard/** : routes user to homepage showing a graph with the number of pages they should read per day, a form to log daily reading progress, a form to create a new reading, and charts of upcoming and finished readings
- **classes/** : routes user to page containing all courses they have readings for
- **classReadings/** : routes user to page containing all readings that are for the request.GET-specified "course." If none is specified, the user is redirected to classes/
- **authors/** : routes user to page containing all authors they have readings for
- **authorReadings/** : routes user to page containing all readings that are for the request.GET-specified "author." If none is specified, the user is redirected to authors/
- **readingProgress/** : routes user to page containing graphs for number of pages to read per day in total and for each class they have readings for
- **readingStats/** : routes user to page containing some statistics about their readings, including number of papers read, number of pages read, average paper length, number of readings assigned per author, and number of pages assigned by course
- **about/** : splash/about page detailing information about the app for the user

## Design
#### 1: Account Creation

-   Users  [create an account](http://127.0.0.1:8000/accounts)  with an email, username, and password
-   Users receive an error message if they use an already in-use email or username
-   Signed-in users cannot create another account (until they sign out)

#### 2: Account Login

-   Users  [login](http://127.0.0.1:8000/accounts)  with their username and password
-   Failed sign-in attempts are rejected and users are notified
-   Logged-in users cannot login again

#### 3: Papers

-   Users can create papers from [dashboard](http://127.0.0.1:8000/dashboard)
-   Users can view their upcoming papers and completed papers also from [dashboard](http://127.0.0.1:8000/dashboard)
-   Papers are always sorted in the order of closer deadlines
-   Each user can only see their own papers that they inputted
-   Each paper shows the due date, title, author (optional), pages read out of total pages, class assigned for, and a link to the paper (optional)

#### 4: Courses

-   A list of all [courses](http://127.0.0.1:8000/classes) for which there are assigned readings is available for viewing
-   All courses can be clicked on, leading to a list of all papers assigned for that course
-   Courses in all papers are linked to their respective course readings page

#### 5: Authors

-   A list of all [authors](http://127.0.0.1:8000/authors)  is available for viewing
-   All authors can be clicked on, leading to a list of all papers assigned for that author
-   Authors in all papers are linked to their respective author readings page

#### 6: Users
-   Whenever a user adds a paper, the paper and the course for which the paper is assigned for is added to the user's paper and courses
-   The user can only see their own papers and courses that they added

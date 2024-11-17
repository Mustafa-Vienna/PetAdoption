# Pet Adoption - Testing

## Manual Testing

### Test Scenarios for User Stories

#### US01: As a new user, I can create an account so that I can access the pet adoption platform’s features, such as viewing and posting pets for adoption.
[Kanban Board (USER STORY: User Registration)](https://github.com/users/Mustafa-Vienna/projects/6/views/1?pane=issue&itemId=86604167&issue=Mustafa-Vienna%7CPetAdoption%7C5)

| **Test Scenario ID** | **Test Scenario**  | **Steps to Test** | **Expected Result** | **Pass/Fail** |
|----------------------|--------------------|-------------------|---------------------|---------------|
| US01-TS01 | Verify the registration form loads correctly | Open the registration page and confirm that username, email, and password fields are displayed. Verify the form uses `crispy` forms for layout. | The form is displayed with all fields, using a consistent and responsive layout. | Pass |
| US01-TS02 | Test successful registration flow | Submit the form with a valid username, email, and password. | The user is successfully registered, logged in, and redirected to the main page. | Pass |
| US01-TS03 | Test duplicate username or email validation | Submit the form with an existing username and/or email. | Error messages are displayed indicating duplicate username or email. | Pass |
| US01-TS04 | Test weak password validation | Submit the form with a weak password (e.g., `12345`). | Error message indicates the password is too weak, and registration is rejected. | Pass |
| US01-TS05 | Test invalid email format validation | Submit the form with an invalid email (e.g., `user@com` or `user@` or `user@gmailcom`). | Error message indicates an invalid email format, and registration is rejected. | Pass |
| US01-TS06 | Test password mismatch validation | Submit the form with mismatched passwords in `password111` and `password222`. | Error message indicates passwords do not match, and registration is rejected. | Pass |
| US01-TS07 | Check edge cases | Submit the form with empty fields, long strings, or special characters in the username/email fields. | Error messages are displayed for empty fields. Long strings are handled gracefully without breaking the application. | Pass |
| US01-TS08 | Verify user name display on navbar after registration | Complete the registration form as a new user (e.g., `user1`). After redirection to the main page, check the navbar. | The navbar should display "Welcome: user1" for the logged-in user. | Pass |
---

#### US02: As a registered user, I can log in to my account so that I can access the platform's features of the application.
[Kanban Board (USER STORY: User Login)](https://github.com/users/Mustafa-Vienna/projects/6/views/1?pane=issue&itemId=86604170&issue=Mustafa-Vienna%7CPetAdoption%7C6)

| **Test Scenario ID** | **Test Scenario** | **Steps to Test** | **Expected Result** | **Pass/Fail** |
|----------------------|-------------------|-------------------|---------------------|---------------|
| US02-TS01 | Verify the login form loads correctly | Open the login page and confirm that username and password fields are displayed. Verify the form uses `crispy` forms for layout. | The form is displayed with both fields, using a consistent and responsive layout. | Pass |
| US02-TS02 | Test successful login flow | Submit the form with valid credentials (correct username and password). | The user is successfully logged in, redirected to the main page, and their username is displayed in the navbar. | Pass |
| US02-TS03 | Test invalid login attempts | Submit the form with incorrect credentials (e.g., wrong password, non-existent username, empty fields). | Error messages are displayed for invalid credentials or empty fields, and login is rejected. | Pass |
| US02-TS04 | Test case sensitivity of username and password | Enter a valid username in uppercase/lowercase and verify login behavior. | Login behavior should be case-insensitive for the username but case-sensitive for the password. | Pass |
---

#### US03: As a logged-in user, I can log out of my account so that I can securely end my session and prevent unauthorized access to my account.
[Kanban Board (USER STORY: Basic User Logout)](https://github.com/users/Mustafa-Vienna/projects/6/views/1?pane=issue&itemId=86604171&issue=Mustafa-Vienna%7CPetAdoption%7C4)

|**Test Scenario ID**|**Test Scenario**|**Steps to Test**|**Expected Result**|**Pass/Fail**|
|--------------------|-----------------|-----------------|-------------------|-------------|
|US03-TS01|Verify the logout option is available|Log in and navigate to any page. Confirm that a "Sign Out" link is visible in the navigation bar.|The "Sign Out" link is visible on all pages when the user is logged in.|Pass|
|US03-TS02|Test successful logout flow|Click the "Sign Out" link in the navigation bar.|The user is redirected to the logout confirmation page and sees the "You Have Been Logged Out" message.|Pass|
|US03-TS03|Test navbar updates after logout|Log out and check the navigation bar. Verify that "Sign In" and "Sign Up" links replace the "Welcome: username" and "Sign Out" links.|The navigation bar updates correctly to display "Sign In" and "Sign Up" links after logout.|Pass|
|US03-TS04|Test access to protected pages after logout|Log out and try accessing a protected page by entering its URL directly.|The user is redirected to the login page and cannot access protected pages.|Pass|
|US03-TS05|Verify session data is cleared|Log out and inspect session storage or cookies in the browser.|Session data is cleared, ensuring no unauthorized access.|Pass|
|US03-TS06|Verify login option on logout page|On the logout page, check for the presence of a link to log in again.|A "Log in again" link is visible and functional on the logout page.|Pass|
---

#### US04: As a registered user, I can interact with a consistent layout with a navigation bar, header, and footer on every page.
[Kanban Board (USER STORY: Consistent Site Layout and Dynamic Navigation Bar)](https://github.com/users/Mustafa-Vienna/projects/6/views/1?pane=issue&itemId=86604166&issue=Mustafa-Vienna%7CPetAdoption%7C7)

| **Test Scenario ID** | **Test Scenario** | **Steps to Test** | **Expected Result** | **Pass/Fail** |
|----------------------|-------------------|-------------------|---------------------|---------------|
| US04-TS01 | Verify the consistent layout across pages | Navigate to all pages and check for the presence of the navigation bar, header, and footer. | The navigation bar, header, and footer are consistently displayed across all pages. | Pass |
| US04-TS02 | Verify the personalized welcome message for logged-in users | Log in and navigate to any page. Check that the navigation bar displays a personalized welcome message (e.g., "Welcome, [username]"). | The welcome message is displayed in the navigation bar for logged-in users. | Pass |
| US04-TS03 | Test navigation bar links | Click on navigation bar links (e.g., "Home," "Posts," "Add Post") and verify that they navigate to the correct pages. | All navigation bar links function correctly and navigate to the appropriate pages. | Pass |
---

#### US05: As a user, I can experience a visually cohesive and branded website so that I feel confident in the website’s professionalism and recognize its identity.
[Kanban Board (USER STORY: Consistent Branding and Visual Design)](https://github.com/users/Mustafa-Vienna/projects/6/views/1?pane=issue&itemId=86604164&issue=Mustafa-Vienna%7CPetAdoption%7C9)

| **Test Scenario ID** | **Test Scenario** | **Steps to Test** | **Expected Result** | **Pass/Fail** |
|----------------------|-------------------|-------------------|---------------------|---------------|
| US05-TS01 | Verify the favicon displays correctly | Open the website in a browser and verify the presence of a favicon in the browser tab for all pages. | The favicon is displayed correctly in the browser tab for all pages. | Pass |
| US05-TS02 | Verify consistent site-wide styling | Navigate through all pages and check that the styles are consistent and cohesive. | All pages have consistent styling, ensuring a branded and professional appearance. | Pass |
---

#### US06: As a user, I want to navigate the website easily using a navigation bar so that I can access the main pages, including home, posts, and the option to add a new post.
[Kanban Board (USER STORY: Navigation Bar with Dynamic Links)](https://github.com/users/Mustafa-Vienna/projects/6/views/1?pane=issue&itemId=86604165&issue=Mustafa-Vienna%7CPetAdoption%7C10)

| **Test Scenario ID** | **Test Scenario** | **Steps to Test** | **Expected Result** | **Pass/Fail** |
|----------------------|-------------------|-------------------|---------------------|---------------|
| US06-TS01 | Verify the navigation bar displays correctly | Open the website and confirm that the navigation bar includes links to "Home," "All Posts," and "Add Post." | The navigation bar displays links to "Home," "All Posts," and "Add Post." | Pass |
| US06-TS02 | Test navigation bar link functionality | Click on each navigation link and verify that it navigates to the correct page. | All navigation links function correctly and navigate to the appropriate pages. | Pass |
---
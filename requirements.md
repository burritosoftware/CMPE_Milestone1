## Functional Requirements
1. A visitor can create an account by providing a username, email, and password.  
2. Registered users can log in using their email and password.  
3. Logged-in users can log out of their account securely.  
4. Logged-in users can add new recipes with title, description, ingredients, and instructions.  
5. Users can update their own recipes after creation.  
6. Users can delete their own recipes.  
7. Anyone can view the details of a recipe including ingredients and instructions.  
8. Users can search recipes by title or ingredient keywords.  
9. Users can rate a recipe from 1 to 5 stars.  
10. Users can leave comments on a recipe.  
11. Users can view their own profile, including their submitted recipes.  
12. Users can update their display name, email, or password.  
13. Users can save or 'favorite' recipes for quick access later.  
14. Homepage or main recipe list shows all recipes available in the database.  
15. Users can filter recipes by tags like 'vegan', 'dessert', etc.

TODO: add screenshots of webpages later

## Non-functional Requirements
1. non-functional: html should have css to increase readibility  
2. non-functional: user can use accessibility option to select dyslexic font

## Use Cases
1. User Registration (Zyjay)
- **Pre-condition:** User must be on the index page
- **Trigger:** Visitor clicks on login/register button
- **Primary Sequence:**
  1. Visitor inputs valid username, email, and password into registration form
  2. Visitor submits registration form
  3. System validates the provided information
  4. System creates the account
  5. System notifies user that an account has been successfully created
  6. System redirects visitor to login page
- **Primary Postconditions:** Account is created and user is redirected to login
- **Alternate Sequence:**
  1. User provides invalid data
  2. System displays appropriate error messages

2. User Login (Zyjay)
- **Pre-condition:** User must be on the login/register page
- **Trigger:** User clicks on login button
- **Primary Sequence:**
  1. User inputs valid username and password
  2. User submits login form
  3. System validates login information
  4. System redirects user to dashboard
- **Primary Postconditions:** User is logged in and on dashboard

3. User Logout (Zyjay)
- **Pre-condition:** User must be logged in
- **Trigger:** User clicks logout button
- **Primary Sequence:**
  1. System receives logout request
  2. System clears session
  3. User is redirected to login page
- **Primary Postconditions:** Session terminated

4. Create Recipe (Zyjay)
- **Pre-condition:** User must be logged in and on index page
- **Trigger:** User clicks on create recipe button
- **Primary Sequence:**
  1. User is redirected to new recipe form
  2. User fills out recipe form
  3. System validates recipe
  4. System saves and links recipe to user
  5. User is returned to index
- **Primary Postconditions:** Recipe saved and linked to user

5. Edit Recipe (Zyjay)
- **Pre-condition:** User must be logged in and creator of the recipe
- **Trigger:** User clicks on edit recipe
- **Primary Sequence:**
  1. User is redirected to edit recipe page
  2. User makes changes
  3. User clicks done
  4. System validates and saves changes
  5. User is redirected to view recipe
- **Primary Postconditions:** Recipe updated

6. Delete Recipe (Noah)
- **Pre-condition:** User is logged in and the recipe's creator
- **Trigger:** User clicks delete in the edit page
- **Primary Sequence:**
  1. User confirms deletion
  2. System validates confirmation
  3. System deletes recipe from database
  4. User is redirected to index
- **Primary Postconditions:** Recipe removed

7. View Recipe (Noah)
- **Pre-condition:** Visitor is on index page
- **Trigger:** Visitor clicks "View Recipe" button
- **Primary Sequence:**
  1. Visitor selects a recipe
  2. System redirects to selected recipe’s detail view
- **Primary Postconditions:** Recipe displayed

8. Search Recipe (Noah)
- **Pre-condition:** Visitor is on index page
- **Trigger:** Visitor clicks search bar and types
- **Primary Sequence:**
  1. System performs fuzzy search by title
  2. Matching recipes are shown sorted by relevance
- **Primary Postconditions:** Search results shown

9. Rate Recipe (Noah)
- **Pre-condition:** User is logged in and viewing a recipe
- **Trigger:** User clicks "Rate Recipe"
- **Primary Sequence:**
  1. Rating interface appears
  2. User selects a rating
  3. Optional text comment is entered
  4. User submits rating
  5. System validates and stores it
  6. User is redirected to recipe view
- **Primary Postconditions:** Rating saved

10. Comment on Recipe (Noah)
- **Pre-condition:** User is logged in and viewing a recipe
- **Trigger:** User clicks "Comment" button
- **Primary Sequence:**
  1. Comment box appears
  2. User types and submits comment
  3. System validates and stores comment
- **Primary Postconditions:** Comment stored in database

11. View User Profile (Stevie)
- **Pre-condition:** User is logged in
- **Trigger:** User clicks "My Profile"
- **Primary Sequence:**
  1. System redirects to profile page
  2. Profile details are rendered
- **Primary Postconditions:** Profile viewed

12. Edit User Profile (Stevie)
- **Pre-condition:** User is logged in
- **Trigger:** User clicks "Edit Profile"
- **Primary Sequence:**
  1. Form displays current username and email
  2. Password reset fields shown
  3. User updates fields and submits
  4. System saves changes and redirects back
- **Primary Postconditions:** Profile updated

13. Save Recipe (Favorites) (Stevie)
- **Pre-condition:** User is logged in
- **Trigger:** User clicks "Save" on a recipe
- **Primary Sequence:**
  1. Recipe is saved to user’s favorites
  2. System shows confirmation
- **Primary Postconditions:** Recipe marked as favorite

14. View All Recipes (Stevie)
- **Pre-condition:** Visitor is on index page
- **Trigger:** Visitor clicks "View All Recipes"
- **Primary Sequence:**
  1. Recipe list page is rendered
  2. Scrollable list of recipes shown
- **Primary Postconditions:** All recipes shown

15. Filter Recipes (Stevie)
- **Pre-condition:** Recipes are pre-tagged
- **Trigger:** Visitor filters on “View All Recipes” page
- **Primary Sequence:**
  1. Visitor clicks filter and selects tags
  2. Recipes with matching tags are shown
- **Primary Postconditions:** Filtered recipes displayed

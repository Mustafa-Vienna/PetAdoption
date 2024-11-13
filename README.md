# Pet Adoption

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Mustafa-Vienna/PetAdoption)](https://github.com/Mustafa-Vienna/PetAdoption/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Mustafa-Vienna/PetAdoption)](https://github.com/Mustafa-Vienna/PetAdoption/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Mustafa-Vienna/PetAdoption)](https://github.com/Mustafa-Vienna/PetAdoption)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Mustafa-Vienna&repo=PetAdoption&layout=compact)

## Pet Adoption Platform

**Pet Adoption** is a Django-based platform for pet adoption, designed to connect people who are looking to re-home pets with potential adopters. This web application offers an easy and user-friendly way for users to post pet listings, browse available pets, and manage inquiries. Our goal is to support pet adoption, encourage responsible pet ownership, and help every pet find a loving home.

### Project Overview

The Pet Adoption application enables users to view available pets, post pet listings, and interact with potential adopters. Built with Django and Bootstrap, the project focuses on creating an intuitive experience that makes it simple for users to connect with pets in need of a new home.

[Live Demo](https://pet-adoptions-9841a93e0575.herokuapp.com/)

![Responsive Design Screenshot]()

### Key Features

- **User Registration and Authentication**

  - Users can register, log in, and manage their profiles, including uploading profile pictures and displaying user-specific information.

- **Pet Listing with Add, Update, and Delete Options**

  - Users can create, update, and delete posts for pets they wish to give away.
  - Each post includes images, descriptions, and tags, helping adopters find pets that match their preferences.

- **Detailed Pet Profiles with Images, Descriptions, and Interaction Options**

  - Each pet listing provides a detailed profile view with images, descriptive tags, and user comments.
  - Users can "like" posts by clicking a heart icon to show interest, and they can leave comments for further inquiries.

- **Enhanced User Interaction on Posts**

  - Users can engage with posts through likes and comments, creating a more interactive platform for pet adoption.
  - Comments allow potential adopters to ask questions directly under each post, facilitating communication between pet owners and adopters.

- **Admin Panel for Monitoring and Management**

  - An admin panel enables administrators to manage user posts, monitor platform activity, and ensure content quality and compliance.

- **Responsive Design**
  - The platform is optimized for both mobile and desktop devices, ensuring a seamless experience across different screen sizes.

## contents

1. [Features](#features)
2. [User Experience (UX)](#user-experience-ux)
3. [Technologies Used](#technologies-used)
4. [Agile Methodology](#agile-methodology)
5. [Version Control](#version-control)
6. [Deployment](#deployment)
7. [Testing](#testing)
8. [Known Issues and Future Features](#known-issues-and-future-features)
9. [Credits](#credits)

## Features

### Existing Features

1. **User Registration and Authentication**

   - Users can sign up, log in, and log out of their accounts with the help of `crispy_form_tag` for a smooth registration experience.
   - User profiles display a list of posted pets associated with each account, but there are no options to edit, reset, or change account details.

2. **Pet Listing Management**

   - Authors (the users who create posts) can add detailed pet profiles with properties including `title`, `pet_name`, `pet_age`, `excerpt`, `image`, and `content`.
   - Only the author of a post can edit or delete their own listings. These options are not available to other registered users or visitors.

3. **Post Interactions (Likes and Comments)**

   - Registered users and authors can like posts by clicking a heart icon to show interest.
   - Both authors and registered users can leave comments on posts to facilitate discussions and inquiries.
   - Visitors (non-registered users) can view posts but cannot interact through likes or comments.

4. **Admin Dashboard**

   - Admin users have access to a dashboard where they can monitor listings, manage posts, and oversee user activity to ensure a safe and supportive platform.

5. **Responsive Design**
   - The website is fully responsive, ensuring an optimal user experience across all devices, including mobile and desktop views.

### Future Features

- **User Account Management**

  - Add functionality for users to edit their profiles, including resetting or updating their password. This will provide users with greater control over their account information and security.

- **Enhanced Comment Section**

  - Allow users to edit and delete their comments on posts, giving them flexibility in managing their interactions on the platform.

- **Direct Contact Form for Adoption**

  - Implement a direct contact form that enables potential adopters to reach out to the author of a pet post. This feature aims to streamline the adoption process by facilitating direct communication.

- **Favorites List**

  - Enable users to save posts to a “Favorites” list for easy access to pets they are interested in, allowing them to quickly revisit and manage potential adoption options.

- **Draft Post Feature**

  - Allow users to save posts as drafts in case they are unable to complete the listing in one session. A “Drafts” section will be available in the navigation bar, enabling users to continue and publish their saved posts when ready.

- **Adoption Status Tracking**
  - Add an adoption status indicator on each pet listing to inform users if the pet is still available or has been adopted. This feature will help users know the availability of each pet more clearly.
- **User Activity Dashboard**
  - Implement a dashboard where users can view all their recent activities, such as posts, comments, and interactions. This feature would provide users with a centralized overview of their contributions and engagement on the platform.

[Go to Contents](#contents)

## User Experience (UX)

### Design Choices

#### Color Scheme

The color palette is crafted to evoke a warm, friendly, and welcoming atmosphere for users, with shades that convey trust, approachability, and growth. The primary colors include deep blues and greens to establish reliability, with coral red accents for calls-to-action that stand out, and soft neutral tones to create a calm backdrop. Each color was selected to enhance readability and visual appeal while maintaining a cohesive and approachable aesthetic.

#### Typography

The primary font is **Roboto**, chosen for its readability and modern feel, providing a clean and professional look. **Open Sans** and **Lato** are used as secondary fonts, lending versatility across different text elements to enhance user experience.

#### Imagery

Images of pets are central to the platform, as they capture users' attention and provide key information about each pet.

### User Stories

#### New Users

- As a new user, I want to register an account so I can list pets for adoption.
- As a new user, I want to browse pet listings so I can find pets available for adoption.

#### Admin Users

- As an admin, I want to review all pet listings and user interactions to ensure a safe and welcoming environment.

[Go to Contents](#contents)

## Technologies Used

### Languages and Frameworks

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.

- [![HTML](https://img.shields.io/badge/HTML-5-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML5) used for structuring the website.

- [![CSS](https://img.shields.io/badge/CSS-3-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for styling and layout.

- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.

- [![Python](https://img.shields.io/badge/Python-3.x-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.

- [![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.

- [![Django](https://img.shields.io/badge/Django-5.1.1-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.

- [![Django Crispy Forms](https://img.shields.io/badge/Django_Crispy_Forms-2.3-grey?logo=django&logoColor=092E20)](https://django-crispy-forms.readthedocs.io/) used to build customizable, responsive forms.

- [![Crispy Bootstrap5](https://img.shields.io/badge/Crispy_Bootstrap5-2024.10-grey?logo=bootstrap&logoColor=7952B3)](https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_form_helper.html) used for styling forms with Bootstrap 5 in Django.

- [![AOS Library](https://img.shields.io/badge/AOS_Library-grey?logo=javascript&logoColor=528DD7)](https://michalsnik.github.io/aos/) used for adding smooth scroll animations to elements on my website.

### Databases

- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as (production) - For reliable, scalable production data storage.

### Other Tools

- [![Git](https://img.shields.io/badge/Git-2.46.0-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`, `git status`)

- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.

- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.

- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for simplify deployment, manage scaling, and streamline environment setup for my Django app with minimal configuration.

- [![Cloudinary](https://img.shields.io/badge/Cloudinary-1.41.0-grey?logo=cloudinary&logoColor=FFFFFF)](https://cloudinary.com) used for hosting and managing image and video files.

- [![Django Cloudinary Storage](https://img.shields.io/badge/Django_Cloudinary_Storage-0.3.0-grey?logo=cloudinary&logoColor=FFFFFF)](https://github.com/klis87/django-cloudinary-storage) used for managing and serving media files via Cloudinary.

- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, README.md design and explain things.

- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used Font Awesome for easily adding scalable icons and styling them in my project.

- [![Favicon](https://img.shields.io/badge/Favicon-grey?logo=data:image/png;base64,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&logoColor=528DD7)](https://favicon.io) used a favicon for adding a recognizable icon in browser tabs and bookmarks.

- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-6.7.0-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files directly from my Django app on Heroku, simplifying file management and boosting loading speed.

- [![Google Fonts](https://img.shields.io/badge/Google_Fonts-grey?logo=google&logoColor=4285F4)](https://fonts.google.com/) used to import the "Lato" and "Open Sans" fonts for consistent typography and styling.

[Go to Contents](#contents)


## Agile Methodology

This project followed an Agile approach, using GitHub Projects and Issues to manage development tasks and adapt to changes effectively. User stories were prioritized according to the MoSCoW method to focus development efforts:

- **Must Have**: Core requirements essential for project success
- **Should Have**: Important features, prioritized after core requirements
- **Could Have**: Additional features to enhance functionality if time allows
- **Won't Have**: Deferred features for future consideration

### Kanban Workflow

The Kanban board was structured to track tasks across three main stages, allowing for a straightforward development flow:

1. **To Do**: Tasks identified and planned for the project.
2. **In Progress**: Tasks currently being developed.
3. **Done**: Tasks that have been fully tested and merged.

- **Link to Project Board**: [Kanban Board](https://github.com/users/Mustafa-Vienna/projects/6)

### Project Evolution

As the project progressed, the initial scope and plan changed significantly. Originally, I had a simpler and shorter project scope, but I made many edits and added new features along the way, leading to a different end result. Additionally, some specific functionalities I initially considered were ultimately not included in the final version. 

Because Agile methodology was applied retrospectively at the end of the project, I placed all tasks directly in the **Done** section rather than tracking them through each stage. This approach helped document the project effectively, even though Agile was only introduced toward the project's completion.

[Go to Contents](#contents)


## Version Control

For version control, I used Git to efficiently track and manage code changes throughout my project. Working in Visual Studio Code on a MacOS setup, I utilized Git's basic commands to maintain a clear version history. My workflow included the following steps:

1. **Development in VS Code**: 
   I used Visual Studio Code as my primary development environment, taking advantage of its integrated terminal to run Git commands directly while working on the project.

2. **Commit Workflow**:
   To keep the project organized and maintain a coherent history, I used a simple commit strategy, frequently staging and committing changes after completing a feature or making improvements. This allowed me to capture the progression of my work and made it easier to review project updates over time.

3. **Basic Git Commands**:
   My Git workflow relied on a few essential commands:
   - `git add <file>` or `git add .`: To stage individual files or all modified files for a commit.
   - `git commit -m "descriptive message"`: To create a commit with a clear message, summarizing the changes made.
   - `git push`: To upload the commits to the remote repository.
   - `git status`: To check the status of staged and unstaged changes, helping ensure no modifications were overlooked.

By sticking to these basic commands, I was able to keep my version history manageable and transparent, capturing meaningful updates without unnecessary complexity.

[Go to Contents](#contents)


## Deployment

This Django application was deployed on Heroku, leveraging its GitHub integration for smooth, automatic deployments. Below is a summary of the deployment process:

1. **Heroku App Creation**:  
   I logged into my Heroku dashboard, selected "New" > "Create new app," and provided a unique app name along with the appropriate region.

2. **GitHub Integration**:  
   In the "Deploy" tab of the Heroku dashboard, I chose GitHub as the deployment method, connected my GitHub account, and selected the repository for this Django app.

3. **Automatic Deployment**:  
   I enabled automatic deployment from the `main` branch. This allows Heroku to redeploy the app automatically whenever changes are pushed to the main branch in GitHub.

4. **Environment Configuration**:  
   In the "Settings" tab, I clicked "Reveal Config Vars" and added essential environment variables for security and functionality:

   - `SECRET_KEY`: My Django secret key
   - `DATABASE_URL`: The database connection URL
   - `CLOUDINARY_URL`: Cloudinary URL for managing images, with `secure=true` to ensure HTTPS delivery
   - `DEVELOPMENT`: Set in the local environment to enable `DEBUG=True` during development
  
   > **Note**: The `DEVELOPMENT` variable is used to control `DEBUG` mode in local environments, allowing safe testing and debugging without affecting production settings.

5. **Buildpack Configuration**:  
   In the "Settings" tab, I configured the buildpack by selecting "heroku/python" to support the Django application.

6. **Automatic Collection of Static Files**:  
   Heroku automatically runs `python manage.py collectstatic` during each deployment to gather all static files into a single directory. This ensures that static assets, like CSS and JavaScript files, are ready to be served in production. During the build, 157 static files were successfully copied to the static file directory.

7. **Verify Deployment**:  
   Once set up, I tested the deployment by clicking "Open App" in Heroku to ensure the application loaded and functioned as expected.

- **Link to Project Board**: [Kanban Board](https://github.com/users/Mustafa-Vienna/projects/6)

---

### Forking and Local Setup

If you’d like to fork this repository and set it up locally, follow these steps:

1. **Fork the Repository**:  
   - Go to the GitHub repository and click on "Fork" to create a copy in your account.

2. **Clone Your Fork**:  
   - Click "Code" on your forked repository, copy the URL, then open your terminal and run:
     ```
     git clone [URL you copied]
     ```

3. **Set Up Virtual Environment**:  
   - Navigate to the project directory:
     ```
     cd [project directory name]
     ```
   - Create a virtual environment:
     ```
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS and Linux: `source venv/bin/activate`

4. **Install Dependencies**:  
   - With the virtual environment activated, install the required packages:
     ```
     pip install -r requirements.txt
     ```

5. **Set Up Environment Variables**:  
   - Create an `env.py` file in the root directory and add the following environment variables based on `settings.py` requirements:
     ```python
     SECRET_KEY = 'your_secret_key'
     DATABASE_URL = 'your_database_url'
     CLOUDINARY_URL = 'your_cloudinary_url?secure=true'
     DEVELOPMENT = 'True'
     ```
   - Setting `DEVELOPMENT = 'True'` enables `DEBUG=True` in local development, allowing you to test and debug safely.
   - Adding `secure=true` to the `CLOUDINARY_URL` ensures media files are delivered over HTTPS, providing secure access to images and assets.

6. **Apply Migrations**:  
   - Run migrations to set up the database schema:
     ```
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

7. **Collect Static Files (Optional for Local Testing)**:  
   - If you want to test static files locally in a production-like setup, you can run:
     ```bash
     python3 manage.py collectstatic
     ```
   - This is typically required in production but can be helpful to verify static files locally.

8. **Run the Development Server**:  
   - Start the server locally:
     ```
     python3 manage.py runserver 8001
     ```
   - Note: This project initially used port `8000` but now uses port `8001` to avoid conflicts with other services.
   - Open a browser and go to `http://127.0.0.1:8001/` to view the application locally.

---

This enhanced setup provides a clear process for cloning, setting up environment variables, and preparing the local environment based on your project’s specific configuration requirements.

---

[Go to Contents](#contents)
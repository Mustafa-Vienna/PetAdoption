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

## Technologies Used

### Languages and Frameworks

- **HTML5** - For structuring the website.
- **CSS3** - For styling and layout.
- **JavaScript** - For interactivity and dynamic elements.
- **Python (Django)** - For backend functionality.
- **Bootstrap** - For responsive design.

### Databases

- **PostgreSQL** (production) - For reliable, scalable production data storage.

### Other Tools

- **Git** - Version control.
- **GitHub** - Remote repository hosting.
- **Heroku** - Deployment platform.
- **Cloudinary** - For hosting and managing images.

## Agile Methodology

**GitHub Projects** and **Issues** were used to organize the development process. User stories were assigned priorities (Must Have, Should Have, Could Have) based on the MoSCoW method to focus development efforts.

### Kanban Workflow

1. **To Do** - Tasks planned for the current sprint.
2. **In Progress** - Tasks currently being worked on.
3. **Done** - Tasks that have been fully tested and merged.

## Version Control

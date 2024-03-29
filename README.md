<div align="center">
  <img src="https://res.cloudinary.com/dzxjg4vwg/image/upload/v1696938620/Screenshot_2023-10-10_at_12.48.12_wwubqt.png" style="background-color: black" alt="The Golfers Photo">
</div>

[The Golfers](https://the-golfers-blog-ed907c4b0918.herokuapp.com/) The Golfers Blog serves as the ultimate resource for uncovering Ireland's top golf courses. Here, users can seamlessly integrate their personal blogs into their profiles, giving them full control over their content. With the ability to update or delete their blogs, users of all skill levels, from seasoned pros to novices, are encouraged to delve into our platform. Our goal is to ignite your passion for golfing and encourage exploration of Ireland's most prestigious golf destinations. Join our welcoming community today and embark on a golfing journey brimming with inspiration and camaraderie.

## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colors](#colors)
    - [Images](#images)
    - [Styling](#styling)
    </details></li>
    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [Landing Page](#landing-page)
    - [About Us](#about-us-page)
    - [Create A Blog](#create-a-blog)
    - [Popular Courses](#popular-courses)
    - [My Golg Blog](#my-golf-blog)
    - [Log Out](#log-out)
    - [Messages](#messages)
    </details></li>

    <li><details>
    <summary><a href="#additional-features">Additional Features</a></summary>


    <li><details>
    <summary><a href="#feature-ideas">Feature Ideas</a></summary>

    - [Basic](#basic)
    - [Content](#content)
    </details></li>
    </ul>
</details>

3. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>

    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Other Tools](#other-tools)
</details>

4. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#methods">Methods</a></summary>

    - [Validation](#validation)
    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details></li>
    </ul>
</details>

5. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    <ul>
    <li><details>
    <summary><a href="#local-deployment">Local Deployment</a></summary>

    - [Local Preparation](#local-preparation)
    - [Local Instructions](#local-instructions)
    </details></li>

    <li><details>
    <summary><a href="#github-deployment">Github Deployment</a></summary>

    - [Github Preparation](#github-preparation)
    - [Github Instructions](#github-instructions)
    </details></li>
    </ul>
</details>

6. <details open>
    <summary><a href="#credit-and-contact">Credit and Contact</a></summary>

    - [Content](#content)
    - [Contact](#contact)
</details>

----

# UX
## Goals
### Visitor Goals
The target audience for The Golfers are:
- Explore reviews and info about Ireland's best golf courses.
- Connect with fellow golf enthusiasts through comments and discussions.
- Post tips and recommendations, fostering knowledge exchange.
- Find courses for beginners and pros alike, catering to diverse skill levels.
- Get the latest news, events, and trends in the Irish golfing scene.

User goals are:
- Users can plan their golf vacations by accessing detailed information about courses, facilities, and nearby amenities.
- Golfers can read user reviews to make informed decisions about which courses align with their preferences and playing style.
- Beginners can seek advice from experienced golfers, creating a supportive environment for skill development.
- Golf enthusiasts can find suitable courses and facilities to organize and host golf tournaments with friends or colleagues.


The Golfers Blog fills these needs by:
- The Golfers Blog provides details about various golf courses, helping users plan their golfing trips effectively.
- Users can view popular courses to make informed decisions, ensuring they choose courses that align with their preferences and skill levels.
- The blog fosters a sense of community, allowing beginners to connect with experienced golfers, facilitating mentorship and skill development.
- Providing social media links to follow The Golfer Blog



### User Stories
1. I expect a user-friendly interface for effortless exploration and easy access to relevant golfing information.
0. I want to seek a lively platform for saving my own golfing experiences
0. I will look for engaging stories, tips, and reviews shared by golfers, motivating them to improve their skills and explore new courses..
0. I desire interactive elements like creating, viewing, and updating my own blogs.
0. As a user I need a responsive design for seamless access on various devices, ensuring convenience while on smartphones or tablets..
0. I expect to be able to follow the Golfers Blog through social media.

-----
# Database

- The graph layout model was created below via the terminal by installing django-extensions and adding it to installed apps.
- I then ran this command - python3 manage.py graph_models -a > mydotfile.dot
- It created the dot file which I copy and pasted it into this site https://dreampuf.github.io/GraphvizOnline/
- I converted it to a png image which is below. 
### Database Model
<div align="center">
  <img src="./docs/readme images/graphviz (1).png" alt="DatabaseModel">
</div>

----

# Agile Methodology

- For streamlined project management, I used GitHub Projects which serves as the central hub, organizing user stories and tasks as GitHub issues. Utilizing the GitHub project board provides a visual representation, effectively tracking progress throughout the workflow.
- Translating user stories into GitHub issues captures user-centric functionalities, linking them to their respective user stories for simplified access to criteria, tasks, and discussions.

### Issues
<div align="center">
  <img src="./docs/readme images/issues_github.png" alt="Issues">
</div>

### Project Board
<div align="center">
  <img src="./docs/readme images/project_board.png" alt="project_board">
</div>


## Visual Design
### Wireframes
<div align="center">
  <img src="./docs/readme images/landing_page_wf.png" alt="landing_page">
</div>

<div align="center">
  <img src="./docs/readme images/about_us_wf.png" alt="about_us">
</div>

<div align="center">
  <img src="./docs/readme images/login,signup,create,update and delete.png" alt="wireframes">
</div>

### Fonts
<div align="center">
  <img src="https://res.cloudinary.com/dzxjg4vwg/image/upload/v1696941472/Screenshot_2023-10-10_at_13.37.17_nlpubg.png" alt="Fonts">
</div>

- The primary font, San-Serif was selected due to its standard, straightforward, and informative nature, striking a balance between approachability and professionalism. It exudes a friendly and conversational tone while maintaining a sense of seriousness.


### Icons
<div align="center">
  <img src="https://res.cloudinary.com/dzxjg4vwg/image/upload/v1696941819/Screenshot_2023-10-10_at_13.43.22_wzo9i5.png" alt="Icons">
</div>

- Icons are taken from the [Fontawesome](https://fontawesome.com/) Icon library and are utilised as classes in the `<i>` tag.
- Since they function as classes, they can be effortlessly customized using other classes or IDs within the same tag. I frequently employed Bootstrap classes to ensure consistent styling a 
  across different elements.
- Icons are employed in the footer for social media accounts.

### Colors
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92331821-a64d1500-f079-11ea-9ceb-a9b1b85872bd.png" alt="Color Pallette">
</div>

- I aimed for a minimal look on the site, using simple and clean colors to accentuate the photos.
- Using dark green as the primary color creates sharp contrast with the photos, drawing focus without distractions, aligning with theater practices. Unlike white, which relates to lighting, dark green enhances visual impact on screens emitting light.
- White text is used to stand out against the vibrant backgrounds of primary and accent colors.
- I incorporated orange in specific text and buttons to complement the green elements harmoniously.


### Images
<div align="center">
  <img src="https://res.cloudinary.com/dzxjg4vwg/image/upload/v1696947045/the_golfers_images_readme_acv3gy.png" alt="Images">
</div>

----

# Features
## Page Elements

### Landing Page

<div align="center">
  <img src="docs/readme images/the_golfers_landing.png" alt="Medium Footer">
</div>

- This is the home page, where every it showcases a sign up button for golfing enthusiasts 
- As soon as you land on the  website, you're greeted with a captivating image carefully selected to engage users senses and set the tone for their journey. 


### About Us

<div align="center">
  <img src="./docs/readme images/about_us.png" alt="Medium Footer">
</div>

- This page is the About section of The Golfers Blog, your go-to hub for exploring Ireland's stunning golf courses. Whether you're a seasoned pro or a beginner, join our community to share experiences, find inspiration, and tee off on an unforgettable golfing journey!

### Create A Blog

<div align="center">
  <img src="./docs/readme images/create_a_blog.png" alt="Medium Footer">
</div>

- This page serves as the "Create a Blog" feature on The Golfers Blog, allowing users to craft their own posts and save them to their personal golf blog


### Popular Courses

<div align="center">
  <img src="./docs/readme images/popular_courses.png" alt="Medium Footer">
</div>

- This page showcases the "Popular Courses" selected by our admins, featuring the top-rated golf courses in Ireland along with reviews, posting dates, and the names of the admins who posted them. Explore these renowned destinations, curated by our team, and discover the finest golfing experiences Ireland has to offer.


### My Golf Blog

<div align="center">
  <img src="./docs/readme images/my_golf_blog.png" alt="Medium Footer">
</div>

- This page is your personal "My Golf Blog" space, where you can view and manage the content you've created. Easily access your blogs, update them with new experiences or insights, and delete them if desired.

### Log Out

<div align="center">
  <img src="./docs/readme images/log_out.png" alt="Medium Footer">
</div>

- This page is the "Logout" feature, allowing users to effortlessly sign out of their accounts. After logging out, users are prompted with a message confirming their successful logout. Experience seamless navigation and enhanced security with our easy-to-use logout functionality

### Messages

<div align="center">
  <img src="./docs/readme images/messages.png" alt="Medium Footer">
</div>

- After your action, such as logging in, signing out, creating a blog, updating, or deleting, you'll receive a confirmation message to keep you informed.

----

### Responivness

<div align="center">
  <img src="./docs/readme images/Responsiveness_For_Smaller_Devices.png" alt="Medium Footer">
</div>

- This image demonstrates the responsiveness of the app, ensuring optimal display and functionality even on smaller screens

----



# Testing

- The Golfer's Blog has undergone rigorous testing, including validation for HTML and CSS. Python files were thoroughly checked using Pep8 standards from Code Institute. All assessments returned positive results, ensuring an optimized user experience during website browsing. Additionally, it's worth noting that no JavaScript was required for the website, so no specific testing was carried out in that regard

- All testing was carried out and documented in [TESTING.md](TESTING.md). 
---
# Technologies Used



### Languages
- HTML
- CSS
- Python

### Frameworks
- Django: Utilizing Django, a high-level Python web framework, to construct the Golfersblog web application.
- Crispy Forms: Employing Crispy Forms, a Django package, to render forms with enhanced efficiency and customization options.
- Bootstrap v5.0: Harnessing Bootstrap v5.0, a widely adopted CSS framework, to craft visually captivating and responsive user interfaces.
- Cloudinary: Leveraging Cloudinary, a cloud-based media management platform, for storing and delivering images within the Blog Collective project.

### Database
- ElephantSQL is a PostgreSQL database service, serving as the database for the Blog Collective project. It offers a dependable and scalable storage solution for the application's data.

# Deployment
## Local Deployment
### Local Preparation
**Requirements:**
- An IDE of your choice, such as [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)

# Deployment

### App Deployment
For deploying Your app, Heroku is used. Follow these steps:

 **Create a New App:**
   - Create a new app on Heroku dashboard.

 **Configure Settings:**
   - Navigate to "Settings" in new app.

 **Config Vars Setup:**
   - In "Config Vars," add `PORT` as the key and `8000` as its value.

 **Add PostgreSQL Database:**
   - Choose PostgreSQL as database.

        Example "ElephantSQL" was used in this project

 **Configure DATABASE_URL:**
   - In "Config Vars," add `DATABASE_URL` and copy the URL from PostgreSQL dashboard.

     Note: If using ElephantSQL as PostgreSQL provider, you can use the URL provided by ElephantSQL.

 **Environment Variable Setup:**
   - Create a new file in workspace called `env.py`.
   - Import the `os` library and set the environment variable for `DATABASE_URL` to the Heroku address (or ElephantSQL URL)
   - Add a secret key using `os.environ["SECRET_KEY"] = "your secret key here"`.

 **Heroku Config Vars:**
   - Add the secret key to the Heroku app's config vars in the settings.

 **Django Settings:**
   - In `settings.py` of Django app, import `Path` from `pathlib`, `os`, and `dj_database_url`.
   - Add `if os.path.isfile("env.py"): import env` to the file.
   - Replace the SECRET_KEY with `SECRET_KEY = os.environ.get('SECRET_KEY')`.
   - Replace the database section with `DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`.

 **Migrate Models:**
   - In workspace terminal, migrate the models to the new database connection.

### Cloudinary
To integrate Cloudinary into project, follow these steps:

 **Cloudinary Account:**
   - Log in to Cloudinary account or create one.

 **Copy CLOUDINARY_URL:**
   - Copy `CLOUDINARY_URL`.

 **Environment Variable Setup:**
   - In `env.py`, add `os.environ["CLOUDINARY_URL"] = "add cloudinary_url here"`.

 **Heroku Config Vars:**
   - In Heroku settings, add `CLOUDINARY_URL` to config vars.

 **Django Settings:**
   - In `INSTALLED_APPS`, add `cloudinary_storage`, `Django.contrib.staticfiles`, and `cloudinary` in this order.
   - Configure static file settings in `settings.py`: URL, storage path, directory path, root path, media URL, and default file storage.

 **Templates Directory Link:**
   - Link the file to the templates directory in Heroku with `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`.

 **Change Templates Directory:**
   - Change the templates directory to `TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]`.

 **Additional Folders:**
   - Create three new folders: `media`, `static`, and `templates`.

 **Procfile Creation:**
   - Create a `Procfile`.
   - Add the following line inside the Procfile: `web: gunicorn project_name_here.wsgi`.

 **Push Changes:**
    - Push all changes to GitHub.

 **Manual Deployment:**
    - In the Heroku deployment tab, deploy to Heroku manually the first time and closely monitor the process.
    - Once successful, set up automatic deployments.

### Local Instructions
1.  You can clone the repository with:
    ```
    git clone https://github.com/phillywhitty/The_Golfers.git
    ```
    To disconnect it from the master repository, use:
    ```
    git remote rm origin
    ```
2. Open your IDE and choose the base directory.



3. Run the project with your chosen method. You can drop index.html into a web browser and it should run fine, open a local port and access it or, if you have python installed, run it on an HTTP server with python with a command such as:
    ```
    python3 -m http.server
    ```
4. Enjoy the site!

## Github Deployment
### Github Preparation

**Requirements:**
- A free GitHub account.

### Github Instructions
1. Log in to your GitHub account.
navigate to [https://github.com/phillywhitty/The_Golfers]
1. You can set up your own repository and copy or clone it, or you fork the repository.
2. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
3. GitHub pages will update from the master branch by default.
4. Go to the **Settings** page of the repository.
5. Scroll down to the **Github Pages** section.
7. Select the Master Branch as the source and **Confirm** the selection.
8. Wait a minute or two and it should be live for viewing.


### Future Features

- **Email Confirmation for Account Creation:**  
Implement email confirmation as part of the account creation process to bolster security measures and ensure effective user identity verification

- **Enhanced Interaction Through User Profiles:**  
Develop user profiles accessible to all, facilitating user interaction through features such as liking, commenting, and sharing interests. This cultivates a sense of community and connectivity among users

## Credits and Contact
### Content
Nearly all text content was generated by the AI, GPT-4. Especially for blog text. It certainly helps and found it great at explaining certain terms but it can be very undependable in certain circumstances and I always double checked any text I generated using it.
Images were screenshots of the golfing websites and then I also used Canva.


### Acknowledgements
- A huge shoutout to Rory Patrick Sheridan for being an amazing mentor throughout the course.
  He's fantastic at breaking down concepts, and I learned a ton from him, especially considering I came in without any IT background.
  Whenever I had questions, he was quick to respond, and he made our online sessions really enjoyable. His support really boosted my confidence.
  A pure gentleman !!
- I also want to give a big shoutout to Kera Cudmore on Slack. 
  Whenever I encountered issues, I reached out to her, and her guidance along with the resources she shared always proved incredibly helpful.
  Kera is actively engaged on Slack, offering assistance to numerous individuals. 
  Her dedication and wealth of knowledge are truly inspiring.
- I'd also like to extend my gratitude to everyone I interacted with at student support. 
  Their outstanding support greatly contributed to my learning journey and helped me immensely in navigating challenges.

### Contact
Please feel free to contact me at `philipwhitty92@yahoo.ie`
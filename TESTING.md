Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)




## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| LandingPage |![landing_page](./docs/testing_images/landing_page_html_check.png) | <mark>PASS<mark> |
| About Us |![about](./docs/testing_images/about_us_html_check.png) | <mark>PASS<mark> |
| Popular Courses|![popular_courses](./docs/testing_images/popular_courses_html_check.png) | <mark>PASS<mark> |
| Sign Up |![sign_up](./docs/testing_images/sign_up_html_check.png) | <mark>PASS<mark> |
| Log In |![log_in](./docs/testing_images/log_in_html_check.png) | <mark>PASS<mark> |
| My Profile |![my_profile](./docs/testing_images/profile_html_check.png) | <mark>PASS<mark> |
| Create Blog |![create_blog](./docs/testing_images/create_blog_html_check.png) | <mark>PASS<mark> |
| My Blogs|![my_golf_blog](./docs/testing_images/my_golf_blogs_html_check.png) | <mark>PASS<mark> |
| Update Blog |![update_blog](./docs/testing_images/update_blog_html_check.png) | <mark>PASS<mark> |
| Delete Blog |![delete_blog](./docs/testing_images/delete_blog_html_check.png) | <mark>PASS<mark> |
| Log Out |![log_out](./docs/testing_images/log_out_html_check.png) | <mark>PASS<mark> |



### CSS
|file|Validator|Result|
| --- | --- | --- |
| style.css |![style](./docs/testing_images/style.css_check.png) | <mark>PASS<mark> |


## JavaScript
|file|Validator|Result|Comment|
| --- | --- | --- |----|

| profile.js |![js](./assets/testing/js/profiles_js_checker.png) | <mark>PASS<mark> |This is js script from CI's walkthrough. I did not want to change this as the function is working. It has two warnings and shows $ as undefined variable |


## Python

|File|App|Image|Result|Comment|
| --- |----| --- | --- |----|
| urls | the_golfers |![python](./docs/testing_images/the_golfers_urls_pep8.png) | <mark>PASS<mark> ||
| admin | blog |![python](./docs/testing_images/blog_admin_pep8.png) | <mark>PASS<mark> ||
| apps | blog |![python](./docs/testing_images/blog_apps_pep8.png) | <mark>PASS<mark> ||
| forms | blog |![python](./docs/testing_images/blogs_forms_pep8.png) | <mark>PASS<mark> ||
| models | blog |![python](./docs/testing_images/blog_models_pep8.png) | <mark>PASS<mark> ||
| urls | blog |![python](./docs/testing_images/blog_urls_pep8.png) | <mark>PASS<mark> ||
| views | blog |![python](./docs/testing_images/blog_views_pep8.png) | <mark>PASS<mark> ||





## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | ---|

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Landing Page Desktop |![landing_page](./docs/testing_images/landing_page_lighthouse.png) | <mark>PASS<mark> |
| Sign-Up Desktop |![signup](./docs/testing_images/signup_lighthouse.png) | <mark>PASS<mark> |
| Log-In Desktop |![login](./docs/testing_images/login_lighthouse.png) | <mark>PASS<mark> |
| My Profile Desktop |![profile](./docs/testing_images/profile_lighthouse.png) | <mark>PASS<mark> |
| Popular Courses |![popular](./docs/testing_images/popular_courses_lighthouse.png) | <mark>PASS<mark> |
| Create Blog |![create](./docs/testing_images/create_blog_lighthouse.png) | <mark>PASS<mark> |
| My Golf Blogs |![golfblog](./docs/testing_images/my_golf_blog_lighthouse.png) | <mark>PASS<mark> |
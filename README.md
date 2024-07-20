# ***TraderBase - Colin Breakell - Portfolio Project 4***

- TraderBase is a website for Forex traders who would like to follow along with a Funded ICT Trader. I decided to make this website for all ICT traders out there who would like to gain information and knowledge, while following my journey via a Journal blog. In my Journal I will be providing daily and weekly analysis. (ICT trading is a style of trading from a trader called ICT) Each blog post will contain chart examples and text explaining what my thought proccess is for each day and each week. I will be showing trade examples, useful information, and trading models for users who signup. I wanted to give a 'Money Heist' vibe to my website beacuse I believe trading is like a money heist. We are entering the market ready to start a heist and take money out of the market for ourselves. Alongside the Journal, there is a checklist feature for all users who have signed up. This checklist is to be used for your trades. Each user has their own indivdual checklist they can use. All users have to do is go to the checklist page, and enter in what they believe needs to be checked off before they enter a trade.


![Am I responsive image](documentation/am_i_responsive_pp4.png)

# **2. Table of content**

# **3. User Experience (UX)**

## **3.1. The Strategy Plane**

### **3.1.1 The Idea**
The idea for TraderBase is simple. I wanted a website that allowed like minded Traders to be able to view my analysis for free. A place for ICT traders to learn some trading education and to compare there analysis to mine. My idea was for me to post Journal entries - these Journal entries would involve weekly, and daily analsyis. People can sign up and view my Journal entires and hopefully learn something!

### **3.1.2 The Ideal User**
My target audience is like minded traders.

- Ideal user likes Forex Trading 
- Ideal user like Indices trading
- Ideal user likes ICT style of content and analysis


### **3.1.3 Site Goals**
- Offer users the ability to learn from my analysis 
- Allow users to view my Journal entries in a clear and easy to read way
- Allow users to ask questions via a comment section
- Get users to use the  Traders checklist to help them organize their trades with a list of things that should happen on the charts before they enter a trade.


### **3.1.4 Epics**
After thinking about my project, 8 Epics were created for this project. These Epics were the main sections of the TraderBase project. You can view the Epics via the KanBan board for this project. The Epics consisted of :

- EPIC 1 : Getting started/Organization
- EPIC 2 : User Authentication and Authorization
- EPIC 3 : App Creation
- EPIC 4 : Database Models
- EPIC 5 : Trading Journal 
- EPIC 6 : User Interaction on Posts 
- EPIC 7 : Style and Design of UI
- EPIC 8 : Documentation


 - ![Epics](documentation/epics.png)

### **3.1.5 User stories**

I had a total of 31 User Stoires for this project. I categorized them via Must-Have -- Should-have -- Could have -- & Wont have.
Must haves were Crucial for this project. Should-haves were I should have this but it is not the end of the world if I do not. Could haves were if I thought something could be in my project, It would be nice to have it but it does not need it. Wont haves were user stories that I wont have in my project due to time restraints or the skills to be able to do it as of now.

**MoSCoW prioritization technique stands for**:

**Must-Have**: Critical requirements that must be implemented for the project to be considered successful.

**Should-Have**: Important requirements that are not critical but add significant value.

**Could-Haves**: Desirable features that would be nice to have but are not crucial.

**Won't-Have**: Features that are explicitly excluded from the project scope.

### List of user stories sorted by Epic :

<details>
<summary>
View User Stories for EPIC 1 : Getting started/Organization
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 1](https://github.com/BreakellrZ/trader_base/issues/12) | User Story - Setting up my Github Repoistory   | As a Developer I can setup a github Repository so that I can push all my work to it from my IDE and have the use of a KanBan Board.      |
| [# 2](https://github.com/BreakellrZ/trader_base/issues/13) | User Story - Creating my Django project | As a Developer I can create a Django project in my IDE so that I can start my pp4 project.  |
| [# 3](https://github.com/BreakellrZ/trader_base/issues/17) | User Story - Deploy and set up to Heroku |  As a Developer I can setup heroku so that I can deploy my project on Heroku |
| [# 4](https://github.com/BreakellrZ/trader_base/issues/30) | User Story - Deploy and set up to Heroku |  As a Developer I can setup heroku so that I can deploy my project on Heroku |

</details>


<details>
<summary>
View User Stories for EPIC 2 : User Authorization and Authentication
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 5](https://github.com/BreakellrZ/trader_base/issues/9) | User Story - Register    | As a Site User I am able to register to create a new account and to be able to select a username and passsword.      |
| [# 6](https://github.com/BreakellrZ/trader_base/issues/10) | User Story - Login | As a Site User I am able to Log in to see registerd user sections. |
| [# 7](https://github.com/BreakellrZ/trader_base/issues/11) | User Story - Logout | As a Site User, I can Log out so that I am no longer Logged in. |
| [# 8](https://github.com/BreakellrZ/trader_base/issues/21) | User Story - Create Superuser |  As a developer, I can create a superuser so that I can control and view my database. |
| [# 9](https://github.com/BreakellrZ/trader_base/issues/35) | User Story - Journal page can only be seen if user is logged in |  As a developer I can  make it so users only see the Journal page if they sign up  so that it gets people to sign up and gets them to comment on journal posts |
| [# 10](https://github.com/BreakellrZ/trader_base/issues/34) | User Story : User can see if they are logged in or not |  As a user I can see if I am logged in so that I know if I need to log in or not |
| [# 11](https://github.com/BreakellrZ/trader_base/issues/42) | User Story : User Story : Only be allowed to use Checklist if logged in |  As a user I can login so that I can use checklist |

</details>

<details>
<summary>
View User Stories for EPIC 3 : App Creation
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 12](https://github.com/BreakellrZ/trader_base/issues/14) | User Story - Create Home app | As a Developer I can Create my first django app so that I can use this app for my home page     |
| [# 13](https://github.com/BreakellrZ/trader_base/issues/16) | User Story - Create Trading Blog app | As a Developer I can create a rescource app so that I can use the app for an extra page on my website to display my trading blog/Journal data from my journal database. |
| [# 14](https://github.com/BreakellrZ/trader_base/issues/41) |  User Story : Create Checklist app| As a developer I can create a checklist app so that users can use a checklist for their trades. |


</details>


<details>
<summary>
View User Stories for EPIC 4 : DataBase Models
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 15](https://github.com/BreakellrZ/trader_base/issues/19) | User Story : Create database with PostgreSQL | As a Developer I can create a postgre datbase so that I can store my data here.     |
| [# 16](https://github.com/BreakellrZ/trader_base/issues/20) |User Story : Connect PostgreSQL database to code | As a Developer, I can connect my database to my code so that I can store my data to my database. |
| [# 17](https://github.com/BreakellrZ/trader_base/issues/23) | User Story : Create a Journal Model| As a developer I can create a Journal model so that I can log my Journal data into my database |
| [# 18](https://github.com/BreakellrZ/trader_base/issues/24) | User Story : Create a Comment Model| As a Developer I can create a comment datbase model so that Users can comment on Journal blog posts |

</details>

<details>
<summary>
View User Stories for EPIC 5 : Trading Journal 
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 19](https://github.com/BreakellrZ/trader_base/issues/32) | User Story : View Post Journal Content | As a user I can view the Journal content so that I can enjoy and read up on the Journal entry. |
| [# 20](https://github.com/BreakellrZ/trader_base/issues/25) | User Story : Create Views for trading_blog app| As a developer I can code my views.py file so that I can import my models to my views and then see my database via a generic listview on live website. |
| [# 21](https://github.com/BreakellrZ/trader_base/issues/18) | User Story : View paginated list of posts| As a site user, I can view a paginated list of posts so that I can select which post I want to view. |
| [# 22](https://github.com/BreakellrZ/trader_base/issues/29) | User Story : Open a Journal post| As a user I can click on a Journal post so that it opens the post and shows me the posts content |

</details>

<details>
<summary>
View User Stories for EPIC 6 : User Interaction on Features
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 23](https://github.com/BreakellrZ/trader_base/issues/33) | User Story : User can Create Comments  | As a user I can have crud capabilities so that the user can create, update and delete their comments |
| [# 24](https://github.com/BreakellrZ/trader_base/issues/38) | User Story : User can Update Comments | As a user I can have crud capabilities so that the user can create their comments |
| [# 25](https://github.com/BreakellrZ/trader_base/issues/39) | User Story : User can Delete Comments | As a user I can have crud capabilities so that the user can delete their comments |
| [# 26](https://github.com/BreakellrZ/trader_base/issues/43) | User Story : Users are allowed to use CRUD operations on checklist | As a user I can use crud operations so that I can update or delte items in my checklist|

</details>

<details>
<summary>
View User Stories for EPIC 7 : Style and Design of UI 
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 27](https://github.com/BreakellrZ/trader_base/issues/27) | User Story : Design Home page with Bootstrap | As a developer I can design the home page nicely so that the users can enjoy a nice UI and understand what the website is all about |
| [# 28](https://github.com/BreakellrZ/trader_base/issues/28) | User Story : Design Journal page with Bootstrap|As a developer I can style the Journal page so that the users will have a nice Journal page to look at |
| [# 29](https://github.com/BreakellrZ/trader_base/issues/37) | User Story : Custom Styling using CSS | As a developer I can use css so that I can use custom styles for my project |
| [# 30](https://github.com/BreakellrZ/trader_base/issues/26) | User Story : Admin Panel Power Up | As a developer I can download summernote so that superusers have a better layout and format on the admin page. |

</details>

<details>
<summary>
View User Stories for EPIC 8 : Documentation
</summary>

| Issue                                                               | Title                                  | User Story                                                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [# 31](https://github.com/BreakellrZ/trader_base/issues/40) | User Story : Document everything I can | As a developer I can document everything so that users can see what TraderBase is about & get a deeper insight into the making of TraderBase |

</details>

---


## **3.2. The Scope Plane**

The scope plans contained the following features to be added.

### 3.2.1. Features to be implemented

- **User Authentication** : Users can Register, Login and Logout.

- **User Interaction for comments** : Users can interact with Journal entries via Comments.

- **User Interaction via checklist** : Users can use a checklist to organize their trades.

- **FAQ** : Users can view the FAQ accordian for answers to the most asked questions about TraderBase.

- **Notifications** : Users will be notified if they have commented on a post, deleted a post, updated a post & they will be able to see if they are logged in or not.


## **3.3. The Structure Plane**

**The structure of TraderBase is consistent, predictable, learnable, and visible, all in the best way using Bootstrap for styling and layout.**

It involves a clean header at the top of the page with the TraderBase logo to the left and the navbar links to the right. The footer is at the bottom of the page, it is clean, provoding users with a Telegram link for more trades from me, and also a disclamier to users that all content shown is not financial advice.

Then on the Home page we have a lovely hero image with text filling up the full screen. As the user scrools down there is another two sections, one with cards showcasing what the users can expect from TraderBase, and the last section is a FAQ area.

On the Journal page, we have the same Header and footer. The main section then involves a hero image and my Journal entry blog posts via cards. These cards are evenly spaced out and there is a Next and Previous buttons to press to go through the Journal entires. These buttons are structured just below the cards.

Inside the journal entries we have the title shown, then under we have the watchlists and news events for this Journal entry, below that we have the main post content and then a comment section for users to interact with the posts. Comments are shown on the left while the comment form is structured on the right. Header and Footer are the same on all pages.

Lastly we have the checklist page, with an update and delete page. All are stuctured very similar. Same Navbar and footer as all othe pages, and a main section in the middle of the page with forms for each page.

The headers structure changes based on if the user is logged in or not. If logged in it will show 'JOURNAL', 'CHECKLIST' & 'LOGOUT'. If not logged in it will show 'LOGIN' & 'REGISTER'.

### **Database Schemas** ###
NEED TO DO LUCIDCHART


## **3.4. The Skeleton Plane**

### 3.4.1. Wire-frames

**I used Balsamiq for my wireframes. This is what I came up for TradeBase :**

<details>
<summary>
Main section of Home page 
</summary>

![Home page wireframe](/documentation//home_balsamiq_pp4.png) ![Mobile Home wireframe](/documentation/mobile_home_balsamiq_pp4.png)

</details>

<details>
<summary>
What to expect & FAQ Sections
</summary>

![Home page part 2](/documentation/home_2_balsamiq_pp4.png) ![Home page part 2 mobile](/documentation/home_2_phone_balsamiq_pp4.png) ![Mobile home part 3](/documentation/mobile_home_3_balsamiq_pp4.png)

</details>

<details>
<summary>
Journal page
</summary>

![Journal page wireframes](/documentation/journal_balsamiq_pp4.png) ![Mobile Journal page wireframes](/documentation/journal_mobile_balsamiq_pp4.png)

</details>

<details>
<summary>
Inside Journal Page
</summary>

![Journal detail page wireframes](/documentation/journal_post_balsamiq_pp4.png) ![Journal detail post wireframes mobile](/documentation/journal_post_mobile_balsamiq_pp4.png)

</details>

<details>
<summary>
Comment Section
</summary>

![Comment section wireframes](/documentation/journal_comments_balsamiq_pp4.png) ![Comment section wireframes Mobile](/documentation/journal_comments_mobile_balsamiq_pp4.png)

</details>

<details>
<summary>
Checklist Page
</summary>

![Checklist wireframes](/documentation/checklist.png) ![Checklist wireframes Mobile](/documentation/checklist_phone.png)

</details>


## **3.5. The Surface Plane**
I went for a 'Money heist' theme for the surface plane. I used a lot of Money Hiest pictures for the hero images on the home page and Journal page and also for the cards on the home page. (Sourced from [Unsplash](https://unsplash.com/). All free images to use).
The reason for this type of design was because I felt like it fits into the trading theme. People Trade to make money and to get rich. To break free from the 'RatRace'. Money heist brings this vibe. Money Hiest is a spanish TV show based on robbers robbing a bank, getting their money and leaving. Just like the trading Markets people take a risk, enter the market, get there money and leave. 

- *The logo* :
 I used was from Font Awesome. It is a icon of a money note with an up arrow indicating money growth. I used a straight line between the icon and the text 'Traderbase'. 
 
 ![Icon](/documentation/logo.png)

- *Color Pallette* :
 The main colors I used were blue, white, black, green, and red. These colors were all used using bootstraps color classes.
Text was either black or white. Giving it a clean aesthetic. I used Blue for the main words, like the name of the website 'TraderBase', the names of the Journal entires on the cards, and the title of the Journal entry. Green was used sparingly, mainly to show users some sort of notification such as if they are logged in or not, or if they have deleted a comment or edited a comment they would get it shown in green text. I used green here so it would stand out to the user. Red was only used for delete buttons, to show users that their comments will be waiting for approval, and to let users know this website is not financial advice as these are all very important for the users to see. (Shown left hand side of the footer)

- *Images* :
 Images were a big part of this project. As said previously I tried to stick with a money heist theme for all my images. I wanted to give a Rebellious vibe to this project. [Unsplash](https://unsplash.com/)

[Back to top]()

---

# **4. Features**



## **4.1. Future Features**
I have a lot of Ideas for future features for TraderBase. My main two ideas include :

- An api that links a calender of all the high impact news events for users to see such as - [ForexFactory](https://www.forexfactory.com/)

-  A chat room for all users to chat and share Trade ideas with eachother.



[Back to top]()

---

# **5. Validation, Testing & Bugs**

## **5.1. Validation**
- Pep 8 CI Validator tests: 

| Directory      | File            | Result                                                   |
| -------------- | --------------- | -------------------------------------------------------- |
| pp4_project    | \`settings.py\` | <span style="color:red;">Fail (Line to long line 122)</span>|
| pp4_project    | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| pp4_project    | \`init.py\`     | <span style="color:green;">PASS</span>                   |
| pp4_project    | \`asgi.py\`     | <span style="color:green;">PASS</span>                   |
| pp4_project    | \`wsgi.py\`     | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`tests.py\`    | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`forms.py\`    | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`apps.py\`     | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| trading_blog   | \`init.py\`     | <span style="color:green;">PASS</span>                   |
| home           | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| home           | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| home           | \`tests.py\`    | <span style="color:green;">PASS</span>                   |
| home           | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| home           | \`apps.py\`     | <span style="color:green;">PASS</span>                   |
| home           | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| home           | \`init.py\`     | <span style="color:green;">PASS</span>                   |
| checklist      | \`views.py\`    | <span style="color:green;">PASS</span>                   |
| checklist      | \`urls.py\`     | <span style="color:green;">PASS</span>                   |
| checklist      | \`tests.py\`    | <span style="color:green;">PASS</span>                   |
| checklist      | \`models.py\`   | <span style="color:green;">PASS</span>                   |
| checklist      | \`apps.py\`     | <span style="color:green;">PASS</span>                   |
| checklist      | \`admin.py\`    | <span style="color:green;">PASS</span>                   |
| checklist      | \`init.py\`     | <span style="color:green;">PASS</span>                   |


- W3C CSS VALIDAOR : 
No errors found.

- W3C HTML Validator :

- JS Validation 

- Lighthouse scores


## **5.2. Testing**
|Epic|What the test is|How I done the test|Outcome|
|-------------|------------------|-----------|-------|
||||| 
|Getting started/Organization|Tested to see if the deployed project works|Clicked on Heroku live project url.|Works as expected|
|Getting started/Organization|Tested to see if PostgreSQL database was connected to Heroku|Logged in as superuser and Checked admin panel on Heroku live site to see if database was connected successfully|Works as expected|
|Getting started/Organization|Tested if I registered to Cloudinary and is it working as an image hosting provider for superusers.|Uploaded a image to my Journal posts via the admin panel using cloudinary, checked if It was displayed on my post_detail page|Works as expected|
|User Authentication and Authorization|Tested to see if users can register|Try create a new account, entered username and password correctly|Works as expected|
|User Authentication and Authorization|Tested to see if an error pops up when users dont add a username and/or password when registering|Leave out a password and/or username when registering|Works as expected|
|User Authentication and Authorization|Can users Login and does an error show if unsuccessful?|Logged in correctly - then logged in with wrong credentials to see if an error message shows|Works as expected|
|User Authentication and Authorization|Can users logout?|Clicked logout button|Works as expected|
|User Authentication and Authorization|Does the correct links show when Logged in/out|Clicked login button - to see if Journal page shows and logout shows - Then clicked logout to see if Journal page was invisible and login/register links were visible|Works as expected|
|User Authentication and Authorization|Tested to see if users can see if they are logged in or not|Logged in and logged out to see if a message showed that the user is logged in or logged out|Works as expected|
|Trading Blog|Tested to see if user can click each Journal post, and it brings them directly to that post|Clicked on each trading Journal post to see if each post sent me to the correct post_detail page|Works as expected|
|Trading Blog|Tested to see if user can view all Journal posts posted via a paginiated list of posts|Clicked on next & previous buttons on post page to go between the most recent posts to older posts|Works as expected|
|Admin Panel|Tested to see if Superuser can successfully use the admin panel to upload Jounral blog posts |Went to admin panel- clicked on Journals - clicked add Journal - Added content to all neccessary fields and clicked save|Works as expected|
|Admin Panel|Tested to see if Journal blog posts were not uploaded to the journal page if status was set to 'draft' |Went to admin panel - clicked on add Journals - Added content to Journal - Put status as draft - hit save - checked to see if post was uploaded or not to journal page. Post was not uploaded |Works as expected|
|Admin Panel|Tested to see if each part of my Journal model worked and was visible for users to see once published. These include Excerpt, title, and watchlist on post.html Journal page - Title, main content, watchlist, news events,specific news, and images on post_detail.html page|Created new Journal post and included each part of Journal model. Clicked on Journal page and clicked into new post.|Works as expected|
|Admin Panel|Tested to see if Superuser can successfully approve comments made by users |Went to admin panel- clicked on Comments - clicked on each comment - Clicked the approve box to approve the comment - clicked save -  checked comment section on live site to see if comment had been approved|Works as expected|
|User Interaction on features|Tested to see if users can comment on Journal posts|Clicked into a Journal post, scrolled down to comment section - Typed in a comment and clicked submit|Works as expected|
|User Interaction on features|Tested to see if users can update their comment on Journal posts|Clicked into a Journal post, scrolled down to comment section - Typed in a comment and clicked submit, then clicked edit button on comment - typed in new comment and clicked update button - comment updated |Works as expected|
|User Interaction on features|Tested to see if users can delete their comment on Journal posts and if a modal pops up when user clicks delete to confirm deletion|Clicked into a Journal post, scrolled down to comment section - Typed in a comment and clicked submit - Found comment and clicked delete - modal pops up, clicked delete button to confirm deletion |Works as expected|
|User Interaction on features|Tested to see if text shows when a user deletes a post |Clicked into a Journal post, scrolled down to comment section - Typed in a comment and clicked submit - deleted comment - Text then shows to the user that the comment was deleted|Works as expected|
|User Interaction on features|Tested to see if text shows when a user comments on a post |Clicked into a Journal post, scrolled down to comment section - Typed in a comment and clicked submit. Text shown that the comment was submitted and is awaiting approval |Works as expected|
|User Interaction on features|Tested to see if text shows when a user updates a comment on a post |Clicked into a Journal post, scrolled down to comment section - Typed in a comment and clicked submit. - Click edit button and update comment, then click update. - Text then shown saying comment updated! |Works as expected|
|User Interaction on features|Tested to see if users can use checklist when not logged in |typed checklist url in. Did not see any option to add, update, or delete. Did not see any checklist |Works as expected|
|User Interaction on features|Tested to see if Update and delete buttons work |In checklist clicked update button, went to update page clicked update to confirm. Went back to checklist page clicked delete button on a checklist input. Went into delete page clicked delete button to confirm deletion. Went back to checklist page, checklist items was updated and deleted |Works as expected|
|User Interaction on features|Tested to see if users can add new inputs to checklist | Went to checklist page as a logged in user, Clicked input bar and put in a new input, clicked submit. |Works as expected|
|User Interaction on features|Tested to see if each individual user had their own checklist | Logged in as two seperate users, went to checklist page, added new inputs to checklist seperatly for each user, updated and deleted some inputs. Both users had different checklists. |Works as expected|


## **5.3. Bugs**
 There was some bugs throughout creating my project. Some of these bugs were basic errors such as not turning debug on or off.
Others were more complex.

- One bug involved buttons on top of my hero images. At one stage during development buttons and anchors stopped working and were not clickable for me in sections where I included styles to a hero image. I realised this was a z-index issue. For my hero images to blend in to the background I had to use a z-index of -1 as part of my styling. This caused an issue with the buttons and anchor tags in that section. I had to style buttons and anchor tags on their own and change their z-index for them to function correctly again. 
<details>
<summary> Z-index button & anchor tags bug </summary>

![Z-index bug](documentation/z-index_bug.png)
</details>


- Server 500 error when Deployed to Heroku. I kept getting a server 500 error when I deployed to Heroku and treid to open my post_detail.html Journal entries. After some help I realised that I did not add my cloudinary URL to config vars in Heroku settings and the images I was uploading was not being registered by Heroku.
<details>
<summary> Server 500 bug</summary>

![Server 500 error](documentation/value_error_bug.png)
</details>

- For the checklist, It took me a while to figure out a bug as to why the checklist was not seperate for each individual user. I tried using checklist = Checkbox.objects.filter(author=request.user) in my Checklist function, which was correct but I needed to not save and commit the changes for all users, it needed to be for each individual user. I did this by using - 
    if form.is_valid():
        checkbox = form.save(commit=False)
        checkbox.author = request.user
        checkbox.save()


---

# **6. Deployment**

### Deployment with Heroku ###
These are the steps I took to deploy my project to Heroku.

- Log into Heroku or create an account.
- Via main page click 'new' in the top right corner and select "Create new app".
- Enter a unique App name, choose your region and "Create app".
- In settings click 'Reveal config vars'. (I added a DATABASE_URL, SECRET_KEY, and CLOUDINARY_URL as my "Keys" - I put in my postgres database URL that I got from Code Institute at ( [Database](https://dbs.ci-dbs.net/) ), & a new secret key, as my values.)
- Just under config vars I Clicked Add "buildback" and put in heroku/python.
- I clicked "Resources" and made sure Eco Dynos was set to 'Eco'
- Go to the 'Deploy' tab and under 'Deployment Method' click on 'GitHub'.
-From the 'Connect to GitHub' section ensure the correct repository is selected and then search for the repository you want to connect to and click 'Connect'.
- You can choose an automatic deploy or a manual deploy. I chose a manual deploy. With a manual deploy I made sure the main branch was selected and clicked 'deploy branch'.
- Once the build is finished there should be a message saying 'Your app was successfully deployed' with a 'View' button.
When I click on 'View' this opened the application.

### Database setup ###
- Went to [Code Institutes Database provider](https://dbs.ci-dbs.net/).
- Submitted email address. 
- Got Database URL via email. 
- set it as environ variable in env.py file.
- Updated database in settings.py file to DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
- Put DATABASE_URL key and database url as value in Heroku Config Vars.

### Fork The Repository

1. Go to the GitHub repository
2. Click on Fork button in the upper right-hand corner
3. Edit the repository name and description if desired
4. Click the green create fork button
 
 ### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/BreakellrZ/trader_base?tab=readme-ov-file)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

[Back to top]()

---

## **7. Technologies & Credits**

### 7.1. Technologies used to develop and deploy this project

- [Bootstrap](https://getbootstrap.com/) was used to style and make website responsive.
- [VS Code](https://code.visualstudio.com/) was used to code the website locally.
- [Balsamiq - Wireframe](https://balsamiq.com/wireframes/) was used to create quick and precise wireframes.
- [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon.
- [Font Awesome](https://fontawesome.com/) was used for all icons on the website.
- [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used for testing the websites performance, accessibility, Best practices, and SEO during the testing phase.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Wave Accessibility Tool](https://wave.webaim.org/) was used during testing to check accessibility
- [CI Python Pep8 Checker](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Cloudinary](https://cloudinary.com/) was used to store static files and images.
- [Heroku](https://heroku.com/) was the hosting provider used.

### Languages Used

- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django

### 7.2. Python Modules Imported 

- [Django-allauth](https://pypi.org/project/django-allauth/) 

- [Dj-database-url](https://pypi.org/project/dj-database-url/) 

- [Gunicorn](https://pypi.org/project/gunicorn/) 

- [Psycopg2](https://pypi.org/project/psycopg2/) 

- [Django Summernote](https://pypi.org/project/django-summernote/) 

- [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/) 

- [Dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) 

- [Cloudinary](https://pypi.org/project/cloudinary/1.27.0/) 


### 7.3. Credits
- I would first like to thank my code institute mentor, Brian O'Hare, for guiding me providing tips and feedback during this project.

- I would like to credit Code Institute and I think therefore I blog Django walkthrough. Code Institute provided all of my education for this project. I think therefore I blog was used to help guide me throughout this project.

- I would like to credit Balsamiq for the creation of my wireframes.

- I would like to thank [**Luicdchart**](https://www.lucidchart.com/pages/) for the chart for my Database Schemas.

- I would like to credit [**Unsplash**](https://unsplash.com/) for providing all of my card and hero pictures.

-  I would like to credit [**Cloudinary**](https://console.cloudinary.com/) for the storage of static files/images.

- I would like to credit - [**FavIcon.io**](https://favicon.io/favicon-converter/). It was used to compress favicon.

- I would like to credit [**W3Schools**](https://www.w3schools.com/), for useful information.
 
 - I would like to credit [**Dennis Ivy YouTube**](https://www.youtube.com/watch?v=4RWFvXDUmjo&ab_channel=DennisIvy) for helping me with the checklist.
[Back to top]()

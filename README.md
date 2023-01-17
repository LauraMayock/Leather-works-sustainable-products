# **Leather Works**

[Live Website]()

[GitHub Repo]()

Leather works is a small company making and selling leather products from sustainably sourced leather. With consumers being more mindful than ever before our aim is to provode a high quality product that is both environmentally friendly, ethically sourced and will last a lifetime. 

**How does our product source ethical and enviromentally friendly leather?**


## **Table of Contents**

* [**Planning Phase**](#planning-phase)
  * [**Strategy**](#strategy)
    * [***Site Aims***](#site-aims)
    * [***Opportunities***](#opportunities)
    * [***Scope***](#scope)
    * [***Structure***](#structure)
      * [**User Stories:**](#user-stories)
        * [**EPIC 1 - Set up and Deployment:**](#epic-1---set-up-and-deployment)
        * [**EPIC 2 - Viewing and Navigation:**](#epic-2---viewing-and-navigation)
        * [**EPIC 3 - Registration and User Accounts:**](#epic-3---registration-and-user-accounts)
        * [**EPIC 4 - Sorting and Searching:**](#epic-4---sorting-and-searching)
        * [**EPIC 5 - Purchasing and Checkout:**](#epic-5---purchasing-and-checkout)
        * [**EPIC 6 - Admin and Store Management:**](#epic-6---admin-and-store-management)
        * [**EPIC 7 - Product Reviews:**](#epic-7---product-reviews)
        * [**EPIC 8 - Marketing:**](#epic-8---marketing)
      * [User Stories dropped as part of the AGILE process](#user-stories-dropped-as-part-of-the-agile-process)
        * [**Form Epic 3 - Registration and User Accounts:**](#form-epic-3---registration-and-user-accounts)
        * [**Form Epic 6 - Admin and Store Management:**](#form-epic-6---admin-and-store-management)
    * [**Skeleton**](#skeleton)
      * [**Wireframes:**](#wireframes)
        * [***Home Page:***](#home-page)
        * [***Products Page:***](#products-page)
        * [***Product Details Page:***](#product-details-page)
        * [***Shopping Cart Page:***](#shopping-cart-page)
        * [***Checkout Page:***](#checkout-page)
        * [***User Profile Page:***](#user-profile-page)
        * [***Order Confirmation Page:***](#order-confirmation-page)
      * [**Database Schema:**](#database-schema)
        * [***All Products Table***](#all-products-table)
        * [***Product Reviews Table***](#product-reviews-table)
        * [***Contact us Table***](#contact-us-table)
        * [***Order Tables***](#order-tables)
        * [***Profile Table***](#profile-table)
        * [***Full ERD from PgAdmin***](#full-erd-from-pgadmin)
    * [**SEO considerations**](#seo-considerations)
      * [***Keywords***](#keywords)
      * [***Page Titles***](#page-titles)
      * [***Robots.txt and sitemap.xml***](#robotstxt-and-sitemapxml)
    * [***Content***](#content)
    * [**Surface**](#surface)
      * [***Colour Scheme***](#colour-scheme)
      * [***Typography***](#typography)
  * [**Agile Development Process**](#agile-development-process)
  * [**E-commerce Application Type**](#e-commerce-application-type)
  * [**Marketing Stratergy**](#marketing-stratergy)
* [**Features**](#features)
  * [**Common to All Pages**](#common-to-all-pages)
    * [**Navbar**](#navbar)
      * [**Overall Appearance**](#overall-appearance)
        * [***Desktop***](#desktop)
        * [***Mobile***](#mobile)
      * [**Common Navbar Features for both Desktop and Mobile**](#common-navbar-features-for-both-desktop-and-mobile)
        * [***Logo***](#logo)
          * [***Desktop***](#desktop-1)
          * [***Mobile***](#mobile-1)
        * [***Search Bar***](#search-bar)
          * [***Desktop***](#desktop-2)
          * [***Mobile***](#mobile-2)
      * [**Account menu**](#account-menu)
        * [***Unauthenticated***](#unauthenticated)
        * [***Authenticated***](#authenticated)
      * [**Cart icon**](#cart-icon)
    * [**Footer**](#footer)
      * [***Desktop***](#desktop-3)
      * [***Mobile***](#mobile-3)
      * [**Common Features to both Desktop and Mobile**](#common-features-to-both-desktop-and-mobile)
        * [***Social Media Links***](#social-media-links)
        * [***Newsletter Sign Up***](#newsletter-sign-up)
        * [***Sitemap***](#sitemap)
    * [**Notifications**](#notifications)
  * [**Page content**](#page-content)
    * [**Home Page**](#home-page-1)
    * [**Products Page**](#products-page-1)
    * [**Product Details Page**](#product-details-page-1)
    * [**Reviews**](#reviews)
      * [***Unauthenticated***](#unauthenticated-1)
      * [***Authenticated***](#authenticated-1)
    * [**Edit product - frontend form**](#edit-product---frontend-form)
    * [**Shopping Cart**](#shopping-cart)
      * [***Desktop***](#desktop-4)
      * [***Mobile***](#mobile-4)
    * [**Checkout**](#checkout)
      * [***Desktop***](#desktop-5)
      * [***Mobile***](#mobile-5)
    * [**Checkout Success**](#checkout-success)
    * [**Profile**](#profile)
    * [***Contact us***](#contact-us)
    * [**Authentication**](#authentication)
    * [***Stock management system***](#stock-management-system)
    * [**Age verification pop-up**](#age-verification-pop-up)
    * [**Responsive Design**](#responsive-design)
  * [**Admin Panel for Shop Administration**](#admin-panel-for-shop-administration)
    * [**Admin Panel Overview**](#admin-panel-overview)
      * [***Products***](#products)
      * [**Messages**](#messages)
      * [**Orders**](#orders)
    * [**Future Features**](#future-features)
      * [***Automation of the stock system***](#automation-of-the-stock-system)
      * [***Dynamically add nav links for new categories/subcategories***](#dynamically-add-nav-links-for-new-categoriessubcategories)
      * [***Sales reports***](#sales-reports)
      * [***Additional shipping choices***](#additional-shipping-choices)
      * [***Additional payment methods***](#additional-payment-methods)
      * [***Additional user account features***](#additional-user-account-features)
      * [***Product options***](#product-options)
      * [***Ticketing Sytem***](#ticketing-sytem)
  * [**Testing Phase**](#testing-phase)
  * [**Deployment**](#deployment)
  * [**Technologies used**](#technologies-used)
  * [**Honorable Mentions**](#honorable-mentions)
  * [**Credits**](#credits)
    * [**Media**](#media)


# **Planning Phase**

## **Strategy**

### ***Site Aims***



### ***Opportunities***

In the course of providing a fully functioning E-commerce platform, the following opportunities are available: -

Opportunity | Importance | Viability/Feasibility
---|---|---
Age verification on first visit | 5 | 3
Mailing list | 5 | 5
Account profile | 5 | 5
Product Filters/searching | 5 | 5
SEO language throughout | 5 | 5
stripe payments | 5 | 5
User feedback for actions taken | 5 | 5
Check out system | 5 | 5
Guest checkout completion | 5 | 5
User login/register | 5 | 5 |
Vape Blog | 1 | 5
Video demo of products | 1 | 5
Delivery information | 3 | 5
User Role permissions | 5 | 5
Product reviews | 5 | 3
Full CRUD functionality | 5 | 5
Order History | 5 | 5
Stock management system | 5 | 3 |
Contact form | 3 | 5
Social Media pages | 5 | 5
Special offers | 5 | 5
Password Recovery | 5 | 5
Email confirmation of order | 5 | 5
Related products | 1 | 1
Saved customer details on checkout | 5 | 5
Admin can add/remove products via the front end | 3 | 5
Multiple currencies | 5 | 1
Trustpilot reviews | 5 | 1
Terms and conditions | 3 | 5
Generate sales reports | 5 | 1
Order Status | 2 | 5
Ability to edit order until status set to processing | 1 | 5
---------------------- | --- | ---  
Totals | 133 | 138

### ***Scope***


### ***Structure***

Using the above as a guide, I have created a flow diagram to help me visualize how the user will navigate through the core functionality of the web store. During the Agile process, minor tweaks may occur to this pre-planned user journey, but the overall structure will remain the same.

![UserFlow Journey flowchart](docs/flowcharts/userjourney.jpg)

#### **User Stories:**

To assist the AGILE process, I have created several user stories to help me plan and implement the project. These will help me prioritize the features and functionality of the site and ensure that I am delivering an MVP by the deadline. The below user stories are divided into EPICs and will be reviewed and updated after each sprint.

##### **EPIC 1 - Set up and Deployment:**



* As a **Developer** I can...
  * ...**Create a Git hub repository** so that I can **Store my project files online.**
  * ...**Create a virtual environment on my local machine** so that I can **avoid polluting my machine on a global level.**
  * ...**Install Django and required libraries** so that I can **work with a postgress Database and cloudbased images from my local development IDE.**
  * ...**Set up my local coding environment** so that I can **develop on my local machine and deploy securely without revealing sensitive information.**
  * ...**Create a Heroku app** so that I can **link to the a virtually hosted Postgres database for the deployed site.**
 


* As a **User**, I can **access a live url** so that I can **use the site on any device**.

##### **EPIC 2 - Viewing and Navigation:**

* As a **Shopper** I want to be able to...
  * ...**Clearly identity the sites purpose upon visiting** so that I can **determine if the site is what I am looking for.**
  * ...**View a list of products** so that I can **select some to purchase.**
  * ...**View individual product details** so that I can **identify the price, description, detailed reviews, and product image enabling me to compare how the product differs from other items.**
  * ...**View the total of my purchases at any time** so that I can **see and review how much I am spending at any time whilst building an order.**
  * ...**Leave a review** so that I can **share my opinion of a product and leave a star rating.**
  * ...**View reviews of a product** so that I can **see what other people think of a product.**
  * ...**Identify any promotions that are available** so that I can **take advantage of them and obtain the best value for money possible.**
  * ...**See clearly when something goes wrong on the site** so that I can **correct any errors and continue with my purchase.**
  * ... **See a pleasantly styled and easy to navigate site** so that I can **enjoy the experience of using the site.**
  * ...**Easily contact the store owner** so that I can **ask questions about the products or the site.**
 

##### **EPIC 3 - Registration and User Accounts:**

* As a **Site User** I want to be able to...
  * ...**Register for an account** so that I can **save my personal details, view my order history online.**
  * ...**Easily login or logout at any time** so that I can **access my personal account information and protect it from unauthorized viewing on shared devices.**
  * ...**Save my personal details to my profile from the checkout page** so that I **don’t have to enter them every time I make a purchase.**
  * ...**Amend my personal details from my profile** so that I can **update information should there be any changes.**
  * ...**Recover my password in case I forget it** so that I can **regain access to my account in the event I lose my password.**
  * ...**Receive an email confirmation upon registration** so that I can **confirm the registration process worked correctly.**

##### **EPIC 4 - Sorting and Searching:**

* As a **Shopper** I want to be able to...
  * ...**Sort the list of available products** so that I can **view them in different orders. and find the highest/lowest rating/prices and sort alphabetically to aid in finding the most suitable products to suit my needs.**
  * ...**Search for a product by name or content in the product description** so that I can **find a specific product I am looking for.**
  * ...**View a list of products in a specific category** so that I can **view all products in that category.**
  * ...**Identify what I have searched for easily and the number of results found** so that I can **easily see the availability of the item I searched for and quickly find the product I want.**

##### **EPIC 5 - Purchasing and Checkout:**

* As a **Shopper** I want to be able to...
  * ...**Select a quantity of a product** so that I can **buy the required amount of the product.**
  * ...**View items in my bag to be purchased** so that I can **identify the total cost of my purchases before checkout.**
  * ...**Adjust the quantity of individual items in my bag** so that I can **easily make changes to my bag.**
  * ...**Easily enter my payment information** so that I can **checkout quickly with no hassles by using information previously stored in the system.**
  * ...**View an order confirmation after checkout** so that I can **verify that I haven’t made any mistakes.**
  * ...**Receive an email confirmation after checking out** so that I can **keep a record of my order.**
  * ...**View my order history** so that I can **see the orders I have made previously.**
  * ...**Access the checkout page** so that I can **review my order whilst entering my payment/shipping details**
  * ...**securely submit my payment details** so that I can **rest assured my financial information is safe**

##### **EPIC 6 - Admin and Store Management:**

* As a **Store Owner** I want to be able to...
  * ...**Add a product** so that I can **add new products to the store.**
  * ...**Edit/update a product** so that I can **change product details.**
  * ...**Delete a product** so that I can **remove products that are no longer for sale.**
  * ...**Add a promotion** so that I can **add new promotions to the store.**
  * ...**manually manage the stock levels** so that I can **input received purchase orders and ensure that the stock levels are accurate in case of discrepancies or damages.**

##### **EPIC 7 - Product Reviews:**

* As a **Shopper** I want to be able to...
  * ...**Leave a review** so that I can **share my opinion of a product and leave a rating.**
  * ...**View reviews of a product** so that I can **see what other people think of a product.**
  * ...**Edit my reviews of a product** so that I can **update my public opinion should it ever change**
  * ...**delete my reviews of a product** so that I can **remove previous reviews should I see fit**.

##### **EPIC 8 - Marketing:**




##### **Form Epic 3 -**



  
### **Skeleton**

#### **Wireframes:**

Wireframes were created using Balsamiq wireframes to visualize how the site would look and function. Included below are the wireframes used to plan the site's layout. However, some changes/omissions were made during the development process due to time or practicality.

##### ***Home Page:***

[Home page wireframe](docs/wireframes/landing-page.png)

##### ***Products Page:***

[Products page wireframe](docs/wireframes/products-page.png)

##### ***Product Details Page:***

This page changed from the original design in the following ways:

* Multiple images were not implemented and so no accordion was needed.
* Buy now button was removed as it was not needed.

These will now be added as part of the future features.

[Product details page wireframe](docs/wireframes/product-detail-page.png)

##### ***Shopping Cart Page:***

[Shopping cart page wireframe](docs/wireframes/shopping-cart-page.png)

##### ***Checkout Page:***

[Checkout page wireframe](docs/wireframes/checkout-page.png)

##### ***User Profile Page:***

This page changed from the original design in the following ways:

* No multiple addresses.
* No delete account button.
* No image/avatar upload.

These will now be added as part of the future features.

[User profile page wireframe](docs/wireframes/user-profile.png)

##### ***Order Confirmation Page:***

[Order confirmation page wireframe](docs/wireframes/order-confirmation-page.png)

#### **Database Schema:**

The database table scheme was created using [drawsql.app](https://drawsql.app) and can be seen below.

##### ***All Products Table***

This table was designed for scalability, I didn't have time to leverage the full advantages of a polymorphic data set, but I have included the fields that would be needed to do so. In the future, I would automate many more processes allowing for products with sizes to be linked together and display the product options on a single product page. This database model also allows for quicker queries as the volume of products grows, so it was designed now to save a lot of restructuring later when the business popularity grows.

[All products table](docs/flowcharts/database/products.png)

[View online with notes](https://drawsql.app/teams/student-444/diagrams/pp5-vapor-town/embed)

##### ***Product Reviews Table***

[Product reviews table](docs/flowcharts/database/product-reviews.png)

[View online with notes](https://drawsql.app/teams/student-444/diagrams/reviews/embed)

##### ***Contact us Table***

[Contact us table](docs/flowcharts/database/contact-us.png)

[View online with notes](https://drawsql.app/teams/student-444/diagrams/reviews/embed)

##### ***Order Tables***

[Order tables](docs/flowcharts/database/checkout.png)

[View online with notes](https://drawsql.app/teams/student-444/diagrams/checkout-app/embed)

##### ***Profile Table***

[Profile table](docs/flowcharts/database/profiles.png)

[View online with notes](https://drawsql.app/teams/student-444/diagrams/profiles/embed)

##### ***Full ERD from PgAdmin***

The EDR from pgAdmin, connected directly to my instance of elephantSQL, shows the complete relationship of all tables. Including those which came from libraries such as all auth.

[Full ERD](docs/flowcharts/database/pgadmin-erd.png)

### **SEO considerations**

#### ***Keywords***

Unfortunately, the website word tracker never worked enough for me. I even subscribed and continued encountering the issue where I had no results or was told I had made too many searches. Speaking to their customer support, they advised this is a known issue and that they are working on it, but it's been a few months, and it's still not working for me. I have included a brain dump using keywords and google to return a list of long and short-tail keywords. The ones ticked were included in the site meta description.

![Key words Brain dump](docs/seo/keywords.JPG)

#### ***Page Titles***

Each page shows an extra title after the store name to assist help with SEO.

#### ***Robots.txt and sitemap.xml***

Sitemap and robots.txt files have been added to the site's root to help with SEO.

At first, I found that lighthouse was showing a fault with my robots.txt. The issue was that it was being read as an HTML file, not a text file. I fixed this by adding a URL path in the project level URLs.py. More about the method can be read [here](https://adamj.eu/tech/2020/02/10/robots-txt/).

Due to initializing the template in the path, I had to move the robots.txt into my templates folder to make it work.

### ***Content***

The site did not have many opportunities for content in terms of paragraphs and text. A lot of the keywords are products themselves, so I have tried to leverage the use of heading tags and other semantic tags correctly  so that the quality of my site's search rating is as high as possible.

### **Surface**

Once the project was planned I then had to decide on a theme. I wanted to keep it simple but have some color to help it stand out. I also wanted to keep it clean and easy to navigate. I have used a lot of white space and a simple color scheme to help with this.

#### ***Colour Scheme***

Black and white feature heavily throughout the site. However, I added color to help the content pop and to help with the branding. Below is the full-color grid I used to help me decide on the final color scheme. Some of my initial ideas changed due to contrasts, which are noted in [TESTING.md](TESTING.md).

The final color scheme can be seen below:
  
Online [here](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23007bff%2C%0D%0A%236c757d%2C%0D%0A%2328a745%2C%0D%0A%2317a2b8%2C%0D%0A%23ffc107%2C%0D%0A%23dc3545%2C%0D%0A%23f8f9fa%2C%0D%0A%23fff59a%2C%0D%0A%23343a40%2C%0D%0A%23ffffff%2C%0D%0A%235469d4%2C%0D%0A%23aab7c4%2C%0D%0A%23000000%2C%0D%0A%23004c9e%2C%0D%0A%23004c9e%0D%0A%23490049%0D%0A%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp)

And via GitHub [here](docs/color/contrast-grid.JPG)

#### ***Typography***

For this project, I have used the following fonts:

* [DM Sans](https://fonts.google.com/specimen/DM+Sans?query=dm+s) - This font is used for the main headings and the logo. It is a clean and simple font that is easy to read and stands out well.
* [Damion](https://fonts.google.com/specimen/Damion?query=damion) - This was for the logo. I initially wanted to make the V and the T cursive; however, I found this font perfect for all letters of the logo.

## **Agile Development Process**

I used [JIRA](https://dnlbowers.atlassian.net/jira/software/projects/PVS/boards/5/roadmap) to track and create issues/user stories. When submitting the project, I will provide login credentials for the above project space. However, you can find a summary of my agile process/learnings [here](AGILE.md).

## **E-commerce Application Type**

As already mentioned, Vapor Town is a B2C e-commerce application. Selling directly to consumers means that the site is designed to sell quickly, on impulse, and in smaller quantities. While wholesale is a possible future goal, the website was not yet intended to sell to other businesses. For this reason, a large amount of the functionality is focused on the user experience and the ability to purchase products quickly and effectively

## **Marketing Stratergy**

As Vapor Town is a start-up business, the budget for marketing is limited. However, there are several ways that Vapor town can market itself to help increase sales and brand awareness. Using Facebook to pump out content and drive traffic is the first and most straightforward. The use of paid ads allows the business to target specific demographics and increase brand awareness. The use of social media is also a great way to get feedback from customers and to help with customer service. There is an image of the Facebook page in the features section below and a link to the page [here](https://www.facebook.com/people/Vapor-Town/100087760702549/).

The second is the use of google ads which are a great way to increase brand awareness and help with SEO. The use of google ads can also help with the use of long-tail keywords and help with the ranking of the site.

The third is the use of influencers. Influences are a great way to increase brand awareness. Free samples could be sent to popular vape reviewers on youtube in exchange for a mention/hashtag/ link in the description. Further helps raise brand awareness because the video could be posted on Facebook and the influencer tagged in the post, which with the help of the algorithm gods at Facebook, would help bring an organic audience to the Facebook page and, hopefully, the store.

The final method would then be sending regular news letters to the mailing list obtained via the mailchimp form.  The newsletter would contain links to recent articles on vaping, the latest products and the highly sought after special offers and promotions. This would help with brand awareness building a community around the brand.

# **Features**

## **Common to All Pages**

### **Navbar**

The navigation bar is the core navigation for the site. It differs slightly from mobile to desktop; however, both include all the same components.

#### **Overall Appearance**

##### ***Desktop***

![Desktop Navbar](docs/features/desktop/navbar-desktop.JPG)

##### ***Mobile***

![Mobile Navbar](docs/features/mobile/navbar-mobile.JPG)

#### **Common Navbar Features for both Desktop and Mobile**

##### ***Logo***

The logo was designed to symbolize the brand. I made it myself using HTML and CSS (including bootstrap classes). The logo is then scattered around the website to add color and help develop brand familiarity and recognition.

The size of the logo is responsive to the screen size. On mobile, it is smaller; on desktop, it is more prominent. Hence, it was important that the color scheme be vivid and the image relatable to the store's name.

###### ***Desktop***

![Desktop Logo](docs/features/desktop/logo-desktop.JPG)

###### ***Mobile***

![Mobile Logo](docs/features/mobile/logo-mobile.JPG)

##### ***Search Bar***

The search bar changes location according to the screen size, and this was to prevent squashing it on mobile. On desktop, it is in the center of the navbar, and on mobile, it is below the logo.

###### ***Desktop***

![Desktop Search Bar](docs/features/desktop/search-desktop.JPG)

###### ***Mobile***

![Mobile Search Bar](docs/features/mobile/search-mobile.JPG)

The user can enter their search term, and the products page will return any products that match the search term. This function checks the product name and description; the search term is retained and displayed to the user next to the number of results displayed.

![Search Bar](docs/features/search-term.JPG)

#### **Account menu**

The account menu is a drop-down menu that appears when the user clicks on the account icon. The drop-down changes slightly depending on the authentication status of the user. The menu will show the option to log in or register if the user is not logged in. If the user is logged in, the menu will allow them to log out and go to their account, where they can amend the default shipping address and review their order history.

##### ***Unauthenticated***

![Unauthenticated Account Menu](docs/features/unauthenticated.JPG)

##### ***Authenticated***

![Authenticated Account Menu](docs/features/authenticated.JPG)

#### **Cart icon**

The cart icon is visible in the navbar on all pages. The icon indicates the current total of all the items in the cart and how many things make up this total.

![Cart Icon](docs/features/cart-icon.JPG)

A cart preview appears when the user adds an item to the cart. This cart preview relays the success message, gives a scrollable preview of the cart, the current total excluding delivery, and an informative message about how far the user is from the free delivery qualifier.

![Cart Preview](docs/features/cart-preview.JPG)

And the cart icon turns blue, and a small pill appears with the product count.

![Cart Icon with pill](docs/features/cart-icon-pill.JPG)

Clicking the cart icon any time will take the user to the shopping cart page described later.

### **Footer**

#### ***Desktop***

![Desktop Footer](docs/features/desktop/footer-desktop.JPG)

#### ***Mobile***

![Mobile Footer](docs/features/mobile/footer-mobile.JPG)

#### **Common Features to both Desktop and Mobile**

The footer is a simple footer that is present on all pages. It contains three main sections, a disclaimer and a copyright section at the bottom.

The three sections typical to both desktop and mobile are:

* Social Media Links
* Newsletter Sign Up
* Sitemap

##### ***Social Media Links***

I have included only one social media link for Facebook for the purposes of this project as it is the one I would like most to leverage in my marketing strategy. However, should this project ever grow further, it would also be expected to include Twitter and Instagram as a minimum.

The current Facebook link will take the user directly to [Facebook](https://www.facebook.com/people/Vapor-Town/100087760702549/) where the shop will share promotions and news about the shop's ad internal vaping community regularly. More will be discussed about this in the marketing section.

I have included a screenshot of the Facebook page in case Facebook decides to remove it because it is not a real business at this stage.

![facebook page](docs/features/facebook.JPG)

##### ***Newsletter Sign Up***

I contemplated creating my newsletter system. However, I decided to use [Mailchimp](https://mailchimp.com/) as it is a free service that is easy to use and has a good reputation with excellent analytics, which are vital for a new business when trying to understand the effectiveness of their marketing.

##### ***Sitemap***

The site map in the footer serves two purposes:

  * It allows the user to navigate the site quickly and easily.
  * It helps to increase the SEO of the site.

### **Notifications**

Similar to the cart preview, the notifications are a small pop-up appearing on the screen's top right. They are used to inform the user of the status of their actions. For example, if the user adds an item to the cart, they will see a notification that says, "Item added to cart." If the user tries to add an item to the cart that is out of stock, they will see a notification that says, "Item out of stock." Where ever possible, when the cart preview is not required, the notifications do not include it. 

These alerts are color-coded according to the default bootstrap colors/names below:

![Bootstrap Colors](docs/features/toasts-colors.JPG)

** Kindly note that bg-secondary was not used for the toasts as it did not fit any specific purpose and alert type.
## **Page content**

### **Home Page**

The home page is the first page on which a user lands. For this reason, it has to have a clearly defined purpose and be easy to navigate. The page will also be used to promote the shop and its products.

To make the site's purpose immediately apparent, I included a hero image that was both colorful and eye-catching with a slogan relevant to the theme. I also had a call to action button that takes the user to the products page.

Below, I have included four cards highlighting four popular product groupings. These demonstrate the site's purpose further and encourage the user to explore the site further.

![Home Page](docs/features/home-page.JPG)

### **Products Page**

The products page is the main page of the site. It is where the user will go to browse the products and add them to the cart. It is also where users will go when they filter the products by category. 6 objects paginate the page at a time, and the user can navigate between pages using the pagination buttons at the bottom of the page.

Wherever the filter set the user chooses, they can sort by price, rating, and name.

On the individual product cards, the user can see the product name, price, rating, image, and, if relevant, a sale price. The user can also add the product to the cart from this page. Users can even add the product directly to their cart in the desired quantity without accessing the product details page. This intends to make the user experience as smooth as possible and reduce the number of clicks required to add an item to the cart.

The product names are all displayed in h2 tags and resized using CSS to increase the SEO of the site.

A user accesses the product details by clicking on the product image.

![Products Page](docs/features/products-page.JPG)

Further to the above, when a user searches for a product and no results are returned, a message is displayed informing them that no results were found.

![No Results](docs/features/no-products.JPG)

### **Product Details Page**

Users can access the product details page when they need more information before committing to purchase an item. This page contains all the information the user needs to make an informed decision. The page is divided into four sections:

* Breadcrumbs - A user can look at various other products in the same category or jump back to the home page.
* Product Image
* Name, Price, Rating, and select quantity
* Tabs for product description and reviews.

![Product Details Page](docs/features/desktop/details-desktop.JPG)

The layout does change a little on a mobile view to improve the appearance

![Product Details Page Mobile](docs/features/mobile/details-mobile.JPG)

It is also worth noting that a superuser can see an edit and delete button on the details page to quickly improve certain felids and remove the product altogether should it be required. I decided to leverage the admin panel for most internal business functions; however, I will go into more detail later.

![Product edit and delete for super users](docs/features/product-edit-del.JPG)

### **Reviews**

The reviews tab was best suited to be on the product details page, making it easy to determine for which product the review was intended. The reviews are displayed in an accordion to save space; however, this tab has a few different ways of displaying them depending on the user's verifications status.

#### ***Unauthenticated***

The user can see all reviews when logged out; however, they cannot leave one. Above the accordion, they are prompted to log in or register to leave a review. The prompt also appears when there are no reviews, along with an invite to be the first to review the product.

![Reviews when logged out](docs/features/reviews-logged-out.JPG)

#### ***Authenticated***

If a product has no review and the user is logged in, they will see an inline review form. This review must have at least a title and a rating, and several checks are in place to ensure the rating is between 1 and 5, and the title is not empty.

![inline review form](docs/features/reviews-inline.JPG)

If there is already an existing review for a product, then the user has a button to take them to the same form but on a new page. Once the user submits the review, they are returned to the product details page of the product they were reviewing.

![review form](docs/features/review-form.JPG)

The last thing to mention here is that the review author (and the superuser in case of foul language) can delete or edit the review. Editing/deletion is performed by clicking the delete/edit button in the review body, visible only to them.

![review edit and delete](docs/features/edit-review.JPG)

From a programmatic perspective, the review calculation is amended each time a rating is added, edited, or deleted so that the overall rating is always accurate.

### **Edit product - frontend form**

As shown above, the product details page has an edit button for the super user to make a quick edit should they spot a typo or want to change a picture. This button takes the superuser to a form pre-populated with the current product information. The user can then make the changes they require and submit the form. The form is validated on the front and back end, and the user is informed of any errors. The user is then redirected to the product details page.

![Edit product form](docs/features/edit-product.JPG)

### **Shopping Cart**

The shopping cart page is where the user can review the items for purchase, and there is a link that will skip the list of items and take the user directly to the totals at the bottom. The intention here is that if the user has a long list of items, they can quickly get to the checkout.

The user can also amend the quantity of each update and click the update button to update the cart. The user can also remove an item from the cart by clicking the remove button. The user cannot add more of a product than is currently in stock.

Once the user is happy with the items in the cart, they can click the secure checkout button to proceed to the checkout page.

The layout on this page changes slightly on mobile to improve the responsive nature. The quantity selector goes under the item on smaller screens. 
#### ***Desktop***

![Shopping Cart](docs/features/desktop/cart-desktop.JPG)

#### ***Mobile***

![Shopping Cart](docs/features/mobile/cart-mobile.JPG)

Lastly, users will see the following message displayed if they try to access the shopping cart with no items.

![Shopping Cart](docs/features/empty-cart.JPG)

### **Checkout**

The checkout page is where the user will enter their payment details and shipping address. There is a chance to make one final review of the cart before proceeding to payment. The user can also go back to the cart to make any changes. If the user is logged in with details already saved to their profile from a previous order, then the form will be prefilled with this information.

The user can also save their details from the checkout page. However, this option is unchecked by default to prevent users from accidentally saving their details.

The card element is injected by the stripe API and uses a payment system that is fully PCI compliant. The same API also handles any errors using the allocated div to display them to the user. For a list of test card numbers, please see the [stripe documentation.](https://stripe.com/docs/testing).

When the form has been submitted, the pay now button converts into a spinner to show it is processing. Further to the spinner, there is a transparent overlay to prevent the user from clicking anything else and creating multiple orders.

The page is fully responsive, and the display order changes slightly from mobile to desktop.

#### ***Desktop***

![Shopping Cart](docs/features/desktop/checkout-desktop.JPG)

#### ***Mobile***

![Shopping Cart](docs/features/mobile/checkout-mobile.JPG)

Guests can also check out, and on the checkout page, they see the following in place of the save info checkbox.

![Shopping Cart](docs/features/guest-checkout.JPG)

If users are not logged in, there is no way to return to the checkout success page, as described below

The last stage of the check out if for the user to receive an email like the sample below:

![Shopping Cart](docs/features/confirmation-email.JPG)

### **Checkout Success**



![Checkout Success]()

### **Profile**

The profile page has a tab which is a form for the user to update their default shipping details

![Profile]()

And another tab to view the order history in a scrollable table

![Completed orders]()

The order number is truncated to save space, and when the user clicks on it, they are taken to a variation of the checkout success page. The only differences to the original checkout success page are the lack of a warning not to leave the page if not logged in and the button at the bottom, which takes the user back to the profile page.

![return to profile]()

### ***Contact us***

Finally, for the front end, I have created a simple contact form for the user to get in touch. I will discuss in detail shortly how this works from the point of view of replying. However, the form allows a platform for the user to send a message to the shop. The message will then be picked up from the admin panel and responded to via email, as is a standard convention.

![Contact us](docs/features/contact-us.JPG)

### **Authentication**

The user can log in and out using an adapted version of templates from the all-auth library.

![Login](docs/features/allauth/login.JPG) ![Sign out](docs/features/allauth/logout.JPG)

The user can reset their password via a form

![Reset password step 1](docs/features/allauth/pass-reset.JPG)

![Reset password - email sent](docs/features/allauth/pass-reset-2.JPG)

Then receive an email with a link to reset their password on the store site.

![reset email](docs/features/allauth/pass-reset-email.JPG)  

![change password form](docs/features/allauth/change-password.JPG)

Once changed, they will see the following message.

![password changed](docs/features/allauth/pass-reset-conf.JPG)

The user can also register for an account using the following form.

![Register](docs/features/allauth/register.JPG)

And will receive an email to verify their email, preventing spam accounts from being created.

![Verify email](docs/features/allauth/verify-email.JPG)

![Verify email](docs/features/allauth/email-verify.JPG)

The link in the email brings them to this screen

![Verify email](docs/features/allauth/conf-email.JPG)

And once the email is confirmed, the user is invited to log in with their new account.

### ***Stock management system***

![not enough stock]()


![out of stock]()


### **Responsive Design**


## **Admin Panel for Shop Administration**



### **Admin Panel Overview**



#### ***Products***



#### **Messages**




### **Future Features**


## **Testing Phase**


## **Deployment**


## **Technologies used**

* Python
  * The packages installed for the project can be found in [the requirements.txt](requirements.txt)
* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* Heroku PostgreSQL & ElephantSQL
  * Used for the database during deployment.
* SQLlite3
	* Was used during development as a database to test models.
* HTML
  * HTML was the base language used to lay out the skeleton of all templates.
* CSS
  * Custom CSS is used to style the page and make the appearance look a little more unique.
* Javascript
  * I have used Javascript to manipulate the DOM and communicate with the backend to create, read, update, and delete data from the database.
* Bootstrap 4.6
  * Used to style HTML, CSS, minor javascript. The more I used this framework the most I realized retrospectively how it could have saved me writing several parts of the code I had already written.
* Font awesome
  * All icons throughout the page.
* AWS S3
  * Used to store static and media files.
* Stripe
  * Used to handle payments.

## **Credits**

* [Code Institute](https://codeinstitute.net/) - For the course material and the support throughout.  Some of the project may reflect similarities to the course material, but I have tried to make it as unique as possible.
* Balsamiq was used to create the wireframes.
* GitHub was used to store my repository.
* I lived in the [django documentation](https://docs.djangoproject.com/en/3.2/) and [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) for the duration of the project live they were a bibles.
* [W3cschool](https://www.w3schools.com) used to remeber the syntax of various languages.
* [Stackoverflow](https://stackoverflow.com/) for debugging and finding solutions to problems.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* [For help pushing the footer to the bottom of the page](https://www.youtube.com/watch?v=yc2olxLgKLk)
* [favicon generator](https://www.favicon-generator.org/) was used to generate the favicon.


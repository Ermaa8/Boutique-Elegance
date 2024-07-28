# BOUTIQUE ELEGANCE

Boutique Elegance is a webshop desined for clothes, shoes, bath & bed, kitchen, active wear. This site is desined towards users that are interested in having everything on one place. Users can browse and purcase different types of items.

The payment system for this site uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site.

The live link can be found here - 

## User Experience (UX)

A visitor to Fresh Nest would be someone who is most likely an adult who is interested in buying clothes, homewear, activewear, kicthen devices etc.

### User Stories

#### EPIC | Viewing and Navigation
- As a site user I can intuitively navigate around the site so that I can find content.
- As a site user I can view a list of products so that I can select a product to view.
- As a shopper I can click on a product so that I can read the full product details.
- As a shopper I can view a specific category of products so I can browse the type of products I am interested in.
- As a shopper I can search all products so that I can find what I am looking for.
- As a shopper I can sort all products so that I can view products based on price or title.

#### EPIC | User Account and Profile
- As a site user, I can register an account so that I can have a personal account.
- As a site user, I can log in or log out of my account so that I can keep my account secure.
- As a site user, I can see my login status so that I know if I'm logged in or out.
- As a site user, I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- As a site user, I can view my order history so that I can remember what purchases I've made.
- As a site user, I can recover my password in case I forget it so that I can recover access to my account.

#### EPIC | Purchasing
- As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.
- As a shopper, I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.
- As a shopper, I can view the contents of my shopping bag at any time so I can see what is included and the total cost.
- As a shopper, I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.
- As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
-As a shoper I can choose different outfits and get a discount price on that.
- As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.
- As a shopper checkout as a guest so I don't have to sign up for an account.
- As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.
- As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.

#### EPIC | Admin & Store Management
- As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.
- As a site owner, I can add/delete images and location of previous design projects so that I can manage the site's contents.
- As a site owner, I can view and delete customer enquiries on the front-end without having to access the admin panel.

### Design
- Design of this website is elegant and clean. Colours of this website is combination of dark brown and beige colour.

#### Imagery
There is only one main static image on the site which is background picture of a webshop on a main page. All of the pictures are there to show a prduct.

#### Wireframes

## Security Features and Defensive Design
### User Authentication

Where I have used Django's Class-based-views; Django's LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page. Django's UserPassesTestMixin is used to limit access based on certain permissions i.e. to ensure users can only edit/delete Testimonials for which they are the author or if the user is the superuser. If the user doesn't pass the test they are shown an HTTP 403 Forbidden error.

Where I have used function based views I have used Django's login_required and user_passes_test decorators to restrict access as required. 

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error.

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. Stripe keys and wh secret are also stored in the env.py file. 

### Custom error pages:
Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

400 Bad Request - Boutique Elegance is unable to handle this request.
403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
404 Page Not Found - The page you're looking for doesn't exist.
500 Server Error - Due to an internal error we are unable to process this request.

## Features
### Header

**Navigation Bar**
- The navigation bar is visible at the top of every page and includes links to the other pages.

**Search Bar**
- The search bar displays above the nav bar.
- On smaller screens, this bar becomes a search icon which when clicked will drop down the full bar.
- Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.

### Home Page
- The home page includes a call to action section which encourages the user to 'shop now' and an image of stylish boutique.

### User Account Pages
**Sign Up**

![Sign Up]

**Sign In**

![Sign In]

**Log Out**

![Log Out]

### Profile
**Delivery Details**

![Delivery Details]
- The delivery details section shows user's adress and phone number.
- The information provided here is used to autofill the delivery address when placing an order.

**Order History**

![Order History]
- The order history section displays a list of every order the user has placed.
- The table displays the order number, date it was ordered and the order total.
- Clicking the order number will take the user to a summary page of that order.

### Product Detail

![Product Detail]
- When user clicks on the product, every detail of specific product is shown on the screen.
- If the user is a superuser, edit and delete buttons will appear below these details.

**Edit Product**
- The superuser can choose to edit a Product by clicking the edit button on the product card or on the product detail page. 
- The form opens with all fields populated with the original content.
- If a user tries to add a product (by changing the url) without being a superuser they are redirected to a custom 403 page.

**Delete Product**

![delete product]
- The superuser can choose to delete a Product by clicking the delete button on the product card or on the product detail page. 
- The superuser is asked to confirm if they wish to delete the product or cancel.
- If products are successfully deleted a superuser will recive a message. 

### Checkout 

![checkout]

**Details**
- In the details section the user can fill out their contact details, delivery address, and card number.
- If the user is a guest, a link to create an account or login will be present.
- If the user is signed in a checkbox to save the delivery information can be checked.
- If the user is signed in and has delivery information saved, the delivery details and email address will be automatically filled in.
- If a user leaves a required field empty, inputs whitespace in a required field or includes text in the phone number field an error message will prompt the user to 'Fill in the field' or 'match the format requested'.

**Order Summary**

- The order summary section details all the items about to be purchased, along with the quantity, subtotal and a grand total.
- Clicking the product image in the summary will take the user to that product's detail page.

**Payment**
- Payment options is handled by Stripe to ensure secure payment.
- Incorrect card numbers will automatically show an invalid card number error.
- A loading screen will appear when a payment is being processed to stop the user clicking away.
- Once the payment is processed, the webhook will search the database to confirm the order exists. If it cannot find it, it will create one using the payment information.

**Confirmation**

![Order_confirmation]
- Once order has been placed and processed the user is taken to the checkout success page.
This page summarises the completed order.
- An email will be sent to the user with their order confirmation
- At the end of the summary is a 'Keep Shopping' button.







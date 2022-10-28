# ASS 1 
==Total marks:  12%==

==Due date:  Both Task 1 and 2:  Saturday, 20 August 2022, 11:55 PM==

# Task 1: User stories and acceptance criteria
User stories are short, simple descriptions of a feature told from the perspective of the person who desires  the new capability. Acceptance criteria are a set of statements, each with a clear pass/fail result, that specify  both functional and non-functional requirements
![](pic/FIT5136_Informal_Client_Requirements_V6.2.pdf)
![](pic/FIT5136%20-%20Assignment%201%20%20Requirements%20-%20Detailed%20Assessment%20Info.pdf)
## 1.1. Identify all the features 
based on information provided on both Informal client Requirements and  ED forum interview
### Feature 1 Customer Registration/ Login / Logout REQ & QA

> Feature 1: Customer Registration/ Login / Logout  
● The system should allow customers (i.e., students) to create an account using their existing Monash email  address. The system needs to validate the email they have provided using the @student.monash.edu email  they provide. They can create their own password, and this can be different from their Okta login password


-   One e-mail address can only be used to create one account?
    
    -   Yes
        
-   What’s the form and limitation of the password? E.g. no more than 8 words; no special characters.
    
    -   The question has been answered in the previous post
        
-   Will these limitation instructions be shown beside the enter space for users to see?
    
    -   You need to elaborate further for this part, We are not sure what limitation instructions you are referring to.  
        

### Feature 2 Community Exchange Management REQ & QA
#### module 1 Post an ad

> For module 1 posting an ad:  
o The customers can choose either posting an item or services  
o The customer needs to enter the item/ service title  
o The customer needs to choose the category they prefer  
o The customer needs to choose the subcategory they prefer after the top category if applicable, for  example, Miscellaneous goods do not have a sub-category. For textbook sub category includes: Art,  Business & Economics, Education, Engineering, Information Technology, Law, Medicine/Nursing,  Pharmacy/ Pharmaceutical Sciences, Science   
o The customer needs to enter the price they would like to sell, also they can set what they would do  with the price-  
o The customer will also need to share the condition of the item (Used/ New), and a minimum 50-  character description of the item  
o The next option is to let the customer choose how they want the item to be traded.  
o The system will then display a set of details that customers entered when they register, and let  customers know that these details will be also displayed as part of the ad. If they refuse, they just need  to choose the option to skip the particular detail, and the detail will not show up inside the ad  
o The last thing system will display are a confirmation screen showing all the details that customers  entered, and if there is a change needed, the customer can pick one of the options to modify it. And  upon saving, the system will also capture the date listed in a format of dd/mm/yyyy hh:mm (e.g.,  27/07/2022 10:18)  
o When the customer chooses services, the customer can pick a category of cleaning or learning &  tutoring or Miscellaneous services.  
o The customer can choose their faculty and write areas of expertise after picking the category  
o And system will then do the same thing as when customer posting item at the end

Module 1

-   What’s the definition of “Miscellaneous goods”? What kind and state of goods can be included into this category?
    
    -   Miscellaneous goods are any goods that is not belongs to the category mentioned, the category details have been provided in earlier post
        
-   How many trade options can be chosen by the customers? Like face-to-face trade; deliver to door.
    
    -   The question has been answered in the previous post
        
-   Will the customers have choice to skip choosing their faculty and areas of expertise?
    
    -   No, they need to answer it
        

#### module 2: Browse the ad

> for module 2 Browse the ad:  
o The customer can choose to browse the ad from the category/subcategory they like. They also have  the option to view the top 10 newly posted items based on the date listed information.  
o After they finish choosing the option above (category/ subcategory/ top 10 newly posted items), they  will be able to browse the item based on the title  
o Then the customer can reach out to the person by looking at the contact details the person has left.  
This is not going to be part of the system  
o While customer is browsing the ad, they have the option to add the item to the watch list or be auto  captured by the system. More details will be explained in Feature 4

-   Will the option to view the top 10 newly posted items be on the same page with the category/subcategory?
    
    -   It is up to you, please choose the one that has the best usability experience.
        
-   How to arrange and classify the items based on the title (e.g. alphabetic)?
    
    -   Based on alphabetic order, If there are items posted at the same time, the item will be arranged in alphabetical order as well
        
-   What if the customers who posted the ad did not leave his/her personal contact details? How can the customer reach them?
    
    -   The customer cannot reach them, it is a dead ad, but as of now we do not consider about this kind of situation.
        

### Feature 3 REQ & QA

> The ad will have a valid date of 7 days. After that, the customer’s ad will be archived to the Exchange record  management feature under [Previously posted ad].  Customers can see their [previously posted ad] in the same way the customer browses for the ad, however,  they have the option to [reactivate the ad] so that the ad will go into Feature 2 again

-   The list of [previously posted ad] will be on the same page with category/subcategory and top 10?
    
    -   It is up to you, please choose the one that has the best usability experience.
        

### Feature 4 REQ & QA

> Feature 4: Watchlist management  
● The watchlist management has two modules, Module 1: Recently Viewed Items/ Services 2. Module 2:  Watchlist  
o For Module 1, this is auto captured by the system, when a customer chooses this option, they will see  the recently viewed item with some statistics.  
o For Module 2, this is added by the customer itself, if the customer chooses to add the item to the  watchlist, the item will show up here stating the time they added to the watchlist as well as the date  the item was listed

-   Will these two modules always be shown on the (up-right corner) user-interface?
    
    -   It is up to you, please choose the one that has the best usability experience.

## 1.2 user story for  features
You need to write at most 2 user story for each of these features

Week 2 lecture p52
![](pic/Week%202%20Lecture%20Slide%20(1%20Slide%20Per%20Page).pdf)

## 1.3. acceptance criteria
For each user story, write one acceptance criteria
Week 2 lecture p57

# Task 2: Software Prototype
Part 1: Creating a prototype using usability design principlesFile
https://lms.monash.edu/mod/resource/view.php?id=10631055

Part 2: Creating a prototype using Usability Design PrinciplesFile](https://lms.monash.edu/mod/resource/view.php?id=10631056)

Understanding Marking Rubric (https://lms.monash.edu/mod/resource/view.php?id=10631057)

you are using a prototype presentation to illustrate how the final product will be look like. Use visual design  tool Lucidchart to design the prototype of the software.  
Focus mostly on user experience (UX) and correct/appropriate flow of events.  
To align user interface better with real-world applications, ==use one of the design principles (Donald Norman  or Ben Shneiderman) from Week 2 lecture(Week 2 lecture p63) to revise your prototype==.  

During week 5 tutorial, you will present the prototype. The presentation should not be more than 15 minutes  long, and you should use PowerPoint slides to present the prototype

## presentation
As a team, you should make sure the content is readable. You will present this to one of your mentors. If  required, your mentor will ask questions related to your prototype. All the team members should contribute  to designing the UI screens and preparing for the presentation
1. Explain the UI screens  
2. Flow of events of the application  
3. How have you adhered to the selected usability design principles?

# Assessment Submission Requirements
File 1: Completed group coversheet (available on [Moodle] > [Assessments])  

File 2: You will submit a PDF document for task 1.  

File 3: You will submit a PowerPoint file for task 2.  

Please stick to the following naming convention to name your files:  

==FIT5136_Team_X_Task_Y, where X is the team number and Y is the task number==.  

Example:  
File 1: FIT5136_Team_404_group_coversheet.pdf  
File 2: FIT5136_Team_404_Task_1.pdf  
File 3: FIT5136_Team_404_Task_2.pptx

# Individual assessment in a group assignment
Feedback Fruit will be made available after the submission deadline. You must complete it only  after your team has made the submission on Moodle and have presented the prototype.  ==If the whole team did not complete Feedback fruit, it will result the entire assessment to be awarded 0  marks==


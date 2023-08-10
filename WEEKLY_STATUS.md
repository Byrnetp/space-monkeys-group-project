## Space Monkies Weekly Status Updates

### Meeting 1: 6/21/2023

Attendees: Michael Becker, Travis Byrne, Cyro Freire de Lima, David Hughes, Dylan Kayyem

Scrum Master: David Hughes

**Progress on the project from the previous sprint:**

1. Scheduled weekly meeting time and set up Zoom meeting: Thursdays @ 7:30PM MST

2. Created Slack workspace

3. Created Project Proposal Document

4. Created Github Repository

5. Created Trello Board

6. Created Google Drive folder

7. Shared Personal User Manuals for each team member via Slack

8. Created Project Scope Ideation document

9. Created Meeting Agenda template

10. Trello Board Snapshot

**What went well?**

Building out the tools to communicate and collaborate with each other (Trello, Slack, Github, Google Drive, Zoom)
User manuals - learning about each other’s work and communication styles
Everyone showed up to weekly meetings and participated

**What didn’t work?**

Having a clear path forward for next week
Kicking off coding for project

**How can the team improve?**

Maybe start to assign some tasks to people if everyone agrees so that we improve Communication and organization ahead of time

**Choose new scrum master for next sprint**

Mike!

**Initial project feature ideas:**

<u>Features:</u>
1. Store data

2. User retrieves data

3. Visualize data

<u>Architecture Brainstorm:</u>

Welcome Interface

1. Hospital Blood Transactions

   •	Blood donation entry

   •	Transfusion entry

2. Find available blood

   •	Search/View any hospital’s inventory

      a) Proceed to checkout
        
   •	Optimal match search

      a) Proceed to checkout
    
3. Complications

   •	Record
    
   •	Search


### Meeting 2: 6/29/2023

Attendees: Michael Becker, Travis Byrne, Cyro Freire de Lima, David Hughes, Dylan Kayyem

Scrum Master: Michael Becker

#### Weekly Info
Weekly Standup (~5 minutes total for all team members) Each team member must provide the following:

•	What did you do last week?

1. Project Mock 

2. Database Mock

3. Reviewed other mocks

4. Reached out to professor about services for front end and back end: do stuff locally

5. Updated Git to not have .ipynb file

•	What are you doing this week?

1. Markdown file in Git

2. Working on Milestone 3 due next week

3. Finalize outline for application architecture

4. Looking for user stories

•	Are any obstacles stopping you?

1. Waiting on decision for today’s meeting to start html

2. Watching course videos

#### End-of-Sprint Demonstration (~10 minutes)
<u>Progress on the project from the previous week:</u>

•	Work completed tonight will be updated in markdown file and pushed to Git

•	User stories, come up with your own before next week

<u>What we have achieved for the sprint:</u>

We finalized the initial application architecture, finalized the initial database architecture, decided who would be using the application, agreed on assumptions:

**Who would be using the site?**

1. Hospital/bank administrator

**Assumptions**

1. Assumed the application is stored on a server that only hospital/bank administrators can access application

2. Secure login is already established

3. All hospitals are already in database so no need to ever create a new one with our system

4. Automated dispose of expiration (list by date of donation, 42 days after donation shelf life)

5. Minimum stock levels (can’t go below a certain threshold)

6. Home button on every subsequent page

7. Each transaction is one unit

8. Assume multiple donations are different transactions and have doctor's approval


**Proposed Application Architecture**

Welcome Interface with About page (Who is eligible to donate blood?, etc.) - Dylan

1. Hospital Blood Transactions

    • Blood donation - David

    • Transfusion (need to make sure blood is in bank) - David

    • Sending blood from one hospital to another (checkout) - Mike

2. Find available blood

    • Show all hospitals in one visual - Dylan

    • More detailed view of specific hospitals inventory with search/list - Travis

        - Go to send to blood to another hospital page(button at bottom of page)
        
3. Complications

    • Report 

    • View reports for specific hospital and blood type - Cyro

    
**Proposed Database Architecture**

<u>Blood Banks and Hospitals Table</u>
    
    - Hospital ID
    - Type
    - Name
    - City
    - State
    - A+ Inventory
    - A- Inventory
    - B+ Inventory
    - B- Inventory
    - AB+ Inventory
    - AB- Inventory
    - O+ Inventory
    - O- Inventory

    
<u>Donor Table</u>
    
    - Donor ID
    - Name
    - Blood Type
    
    
<u>Patient Table</u>
    
    - Patient ID
    - Name
    - Blood Type
    
    
<u>Transaction Table</u>
    
    - Transaction ID
    - Donation
    - Transfusion
    - Transport
    - Date
    - Time
    - Donor ID
    - Patient ID
    - Medical Professional
    - Hospital ID
    
    
<u>Complication Table</u>
    
    - Transaction ID
    - Comments

#### Sprint Retrospective (~5 minutes)
What went well:

•	Everyone had great mock ups and attempted the project

•	Helpful to have visuals for everyone to discuss

What didn't work:

•	Different platforms made it more difficult for people to view others work

How can the team improve:
    
•	Keep working as a team

### Meeting 3: 7/6/2023

Attendees: Michael Becker, Travis Byrne, Cyro Freire de Lima, David Hughes, Dylan Kayyem

Scrum Master: Michael Becker

#### Weekly Info
Weekly Standup (~5 minutes total for all team members) Each team member must provide the following:

•	What did you do last week?

1. Created Weekly Status markdown and pushed

2. Initial Application Architecture

3. Usage Assumptions for the Application

4. Proposed User Stories

5. Initial Database Architecture

6. Page Template

•	What are you doing this week?

1. Submit Milestone 3

2. Scrum master for the week will submit the milestone

3. Dylan is scrum master for next week

•	Are any obstacles stopping you?

1. Nothing really other than learning things in the class as we progress 

2. Very proactive right now, will look to keep momentum going

#### End-of-Sprint Demonstration (~10 minutes)
<u>Progress on the project from the previous week:</u>

•	Focusing on user establishing stories, added to assumptions, column to database table. 

<u>What we have achieved for the sprint:</u>

We finalized the User Stories we will be using for constructing the application:

**User Stories**

1. Administrator logging a blood donation

2. Administrator logging a blood transfusion

3. Administrator requesting blood transfer

4. Administrator wants to view blood in all hospitals using visualization

5. Administrator wants to look at their own hospital's inventory

6. Administrator wants to see complications

7. Administrator wants to document complication

8. Administrator wants to know why this application was developed and what it does

**To attempt/complete for next week**

1. About page (Cyro)

2. Branch for each story, do not merge until the end (everyone)

3. Start to buildup database (Mike)

#### Sprint Retrospective (~5 minutes)
What went well:

•	Looks like we are well ahead of pace right now

•	Good discussions

What didn't work:

•	All was good this week

How can the team improve:
    
•	Keep working as a team



### Meeting 4: 7/13/2023

Attendees: Michael Becker, Travis Byrne, Cyro Freire de Lima, David Hughes, Dylan Kayyem

Scrum Master: Dylan Kayyem

### Weekly Updates:

- Updated templates for user stories
- Added user stories to Trello
- Templates for donation and transfusion input
- Create database design / collect data

#### End-of-Sprint Demonstration (~10 minutes)

- Went over Mike's database example
- Labeled primary key's for each table
-    yellow - primary key
-    green - foreign key

**To attempt/complete for next week**
  
Welcome Interface with About page (Who is eligible to donate blood?, etc.) - Dylan

1. Hospital Blood Transactions

    • Blood donation - David

    • Transfusion (need to make sure blood is in bank) - David

    • Sending blood from one hospital to another (checkout) - Mike

2. Find available blood

    • Show all hospitals in one visual - Dylan

    • More detailed view of specific hospitals inventory with search/list - Travis

        - Go to send to blood to another hospital page(button at bottom of page)
        
3. Complications

    • Report - Cyro

    • View reports for specific hospital and blood type - Cyro

- Add guidelines for pages/features
- Add mockup to image folder
  
#### Sprint Retrospective (~5 minutes)

**What went well?**
- Action planned to win

**What didn’t work?**
- Had a great week of collaboration 

**How can the team improve?**
- Keep it up monkeys!




### Meeting 5: 7/20/2023

Attendees: Michael Becker, Travis Byrne, Cyro Freire de Lima, David Hughes, Dylan Kayyem

Scrum Master: Dylan Kayyem

### Weekly Updates:

- Created mockups for pages
- Created database code

### Sprint Retrospective:

**What went well?**
- Setup sql/data used for each page
  
**What didn’t work?**
- Continued to have a great week of collaboration!
  
**How can the team improve?**

**What to do for next week?**
- Each team member add a desription of particular database/sql commands used for each page.

### Meeting 6: 7/27/2023

Attendees: Michael Becker, Travis Byrne, Cyro Freire de Lima, David Hughes, Dylan Kayyem

Scrum Master: Cyro Freire de Lima


### Weekly Updates:

### Sprint Retrospective:

**What went well?**
- The tasks and stories assigned for this week and extra stories were developed by the group.

**What didn’t work?**
- Everything worked well. 

**How can the team improve?**
- Just keep working. 

#### End-of-Sprint Demonstration (~10 minutes)

**To attempt/complete for next week**
- Complete all the mockup pages
- Complete the html, js, css files for the mockup pages. 

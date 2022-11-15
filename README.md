# Team_Member_Management

High Level Implementation 
Technology: 
- Django Framework 

API Structure:
/ = List Page 
/add = Add Page 
/edit = Edit Page 
/delete = Delete Page 



List page
This page shows a list of all team members. Note that the subtitle should reflect the number of team members. Also note that if the team member is an admin, that is listed next to their name. Clicking a team member should show the Edit page. Clicking the plus at the top should show the Add page.

![Screenshot from 2022-11-15 14-17-20](https://user-images.githubusercontent.com/67892332/202006474-f4affe5c-36b8-43a0-8ccc-9014aac58906.png)


Add page
The Add page appears when the user clicks the "+" on the List page. The user enters a team member's first & last name, their phone number, and email. Additionally, they can choose the team member's role (it defaults to regular). Hitting save adds the team member to the list and shows the List page.

![Screenshot from 2022-11-15 14-06-44](https://user-images.githubusercontent.com/67892332/202004661-7f1fcc10-2720-4790-a39d-fc0ade7f61fb.png)


Edit page
The Edit page appears when the user clicks a team member on the List page. This shows a form where the user can edit the details of the team member, including changing their role. Clicking save edits the team member information and shows the List page. Clicking Delete removes the team member and returns to the List page.

![Screenshot from 2022-11-15 14-07-07](https://user-images.githubusercontent.com/67892332/202004709-85d3c286-d1f1-4d50-9a6e-1dee1678ca8a.png)


Delete Page 
The Delete Page appears when the user clicks on delete button on the Edit Page. This shows the name of the member the user can delete. 

![Screenshot from 2022-11-15 14-07-20](https://user-images.githubusercontent.com/67892332/202004737-2f9eefed-93ef-4bb6-83ff-a85ac9891c24.png)


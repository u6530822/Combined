# Tech Launcher ME-CFS-Project

# Overview

Medical centres and clinics collect abundant records on patients that can be applied to health and medical research challenges. This is certainly the case with CFS Discovery in Melbourne, who have collected detailed data on ME/CFS patients for almost 20 years. ME/CFS is a mysterious and controversial disease, where Australian scientists are making excellent progress via cross-disciplinary research.

Patient data is stored as individual records, and as such it is very time consuming to physically extract the data for spreadsheets and databases, required for machine-learning and other analyses.

The project is: To automate the extraction of valuable ME/CFS patient data into aggregated form (via spreadsheets is fine), accurately and efficiently. The successful completion of this challenge will accelerate our research efforts towards understanding ME/CFS, by contributing to the construction of anonymous patient databases for pattern recognition interrogation, as well as in support for future biobanks.

# Project Administration
## Timeline
Week 2-3: Requirement gathering and technology assessment/exploration.  <br />
Week 4-5: Work on printed text conversion to raw text for multiple record types.<br />
Week 6-Teaching Break: WebApp development and porting of components.<br />
Teaching Break-Week 7: WebApp development and porting of components.<br />
Week 8-9: Code retrofitting and refactoring.<br />
Week 10-11: Full round of user acceptance testing and consolidation.<br />
Week 12: Reflection and improvements.<br />

# Milestone Chart  
![Capture](https://github.com/u6530822/ME-CFS-Project/blob/master/milestone_sem2.PNG)

# Deliverables
•	Modular well-structured code to carry out the following:<br />
o	New process to convert and store printed patient records from image documents. <br />
o	Build a usable web application for multiple users.<br />
o	Provide an easy to use and intuitive user interface. <br />
o	Allow sufficient space for scalability and further analytic needs. <br />

•	Documentation will be covered in the following:<br />
o	Well commented and modular code. <br />
o	High level documentation on code process in each iteration. <br />
o	A user guide to be handed to the stakeholders at the end of the project.<br />

[Product Backlog](https://drive.google.com/open?id=154SpNfr9QrG_j6Xw1HOSoIcJ5UUipYOH)<br />

## Version control and monitoring.<br />
All work will be tracked in github, and while the project deliverables on a high level will be constantly updated on the project wiki. <br />

# Team
|Member| UID|	Role|	Backup|	Email|
| --- | --- | --- | --- | --- |
|You Li|u6430173|Developer| 	Quality Assurance|	you.li@anu.edu.au|
|Nigel Tee|u6530834|Developer|	Quality Assurance|	nigel.tee@anu.edu.au|
|Chin Hun Young(Spokeperson)|u6530822|Quality Assurance|	Project Manager|	chin.young@anu.edu.au|
|Rufus Raja|u6275198	|Project Manager|	Developer|	rufus.raja@anu.edu.au|

Supervisor and product owner: Brett Lidbury  

## Team's Decision Making Steps
[Decision Making Document](https://drive.google.com/open?id=1iuMgKuiV72ic6ZybAdhszDJW5QMlwO6K)<br />

*Github is open to public for now, will set it to private once we start working on client sensitive materials

# Stakeholders
Our chief client is Dr. Brett Lidbury. We have a slack channel setup and will have weekly connects with him. Our secondary contact is Dr. Alice Richardson. 

# Project Artifacts
[Signed Statement of Work](https://drive.google.com/open?id=1ubx86LAXTK2ZrMt02hDcEY6cJ36JbsZL)<br />
[Approved DB Fields](https://drive.google.com/file/d/1NbsGXRXQ0QnQ8ItyiEVDQO5VlD8_Rv8t/view?usp=sharing)<br />
[Iteration Tracking](https://drive.google.com/open?id=1raXbQCZwbuC9pfEanfUcopBtbM6gnxxo)<br />
[WebApp Project wireframe](https://miro.com/welcomeonboard/ziBEuWqqLOSwyXJdsmGYMRkKrHZ7JT6zGQmFE7B6rDflGzvmb9Staj8C1FsMBxgi)<br />

# Communication 
[Meeting Minutes](https://drive.google.com/open?id=1DurYJGpZz_lg4WVPxudQ3C8tK4CBJhoG)<br />

# Quality Assurance
[Technical Specification](https://drive.google.com/open?id=1wfPwsIupVd4-8BWSAJ2hM75zIaerGfEm)<br />
[Issue Tracking](https://github.com/u6530822/ME-CFS-Project/issues)<br />
[Feedback Log](https://drive.google.com/open?id=15BJ5XNeOg506WVSW6oJ9KiIewVI6bu0y)<br />
[Testing Summaries](https://drive.google.com/open?id=1ZEOj7_jx3_S4uiXrAKP5AE71k3hNBPz8)<br />

# Support Documentation
[Project Documentation Folder](https://drive.google.com/open?id=1fHtWXQIDxyIFErwrestoyBETrUFVW-Yq)<br />

# Current Progress
#### [Progress Report Folder](https://drive.google.com/open?id=1nNwb4hMxnOc-OpS6_ZUqV_MOcdIcfRJb)<br />

# Technical Tools and Constraints
•	Off the shelf tools<br />
  ○ Optical Character Recognition software <br />
<br />
•	implementation from scratch<br />
  ○ Neural Network<br />
  ○ Code in Tesseract/TensorFlow<br />
<br />

•	Constraints:<br />
  ○ Current model does not support different file types.<br />
  ○ Documents containing handwritten and printed text.<br />
  ○ Sensitive issue related to disclosing patients' data<br />
  
  # Risk Management
  
  ![Capture](https://github.com/u6530822/ME-CFS-Project/blob/master/risk_list.PNG)
  
### Technical Risk
#### Time for the text conversion to be longer than client’s expectation
Likelihood: Unlikely<br />
Consequence: Catastrophic<br />
Priority: High<br />
Solutions: Obtain main stakeholder’s agreement on the time required for conversion to match expectation<br />
#### Limitation of knowledge in handwritten to text conversion
Likelihood: Possible<br />
Consequence: Moderate<br />
Priority: High<br />
Solutions: Obtain main stakeholder’s agreement on the possible removal of feature<br />
#### New record types to be considered apart from existing printed document samples
Likelihood: Certain<br />
Consequence: Major<br />
Priority: High<br /> 
Solutions: Clear scope of work agreed upon by the stakeholder, continuous analysis<br />

### Ethical Risk
#### Data security breach
Likelihood: Possible<br />
Consequence: Catastrophic<br />
Priority: Extreme<br />
Solutions: Access authorisation, multilevel security model in databases & encryption<br />
##### Data Privacy issues
Likelihood: Possible<br />
Consequence: Catastrophic<br />
Priority: Extreme<br />
Solutions: Signed Ethical form, Downgrading results, stakeholder’s agreement on storage method<br />

### Resources risk
#### Members fall sick & Unavailability of members
Likelihood: Possible<br />
Consequence: Minor<br />
Priority: Medium<br />
Solutions: Shadowing teammates, Daily stand-up to update on progress<br />
#### Unforeseen accident
Likelihood: Rare<br />
Consequence: Moderate<br />
Priority: Low<br />
Solutions: Shadowing teammates, Daily stand-up to update on progress<br />




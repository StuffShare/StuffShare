StuffShare allows users to create a catalogue of all their belongings, with specific details about each item. Users also select the visibility of each item, which defines which other users on StuffShare can access its details. The central idea of StuffShare is allowing users to lend out and borrow personal belongings to and from one another, and maintain a personal catalogue of their belongings they cannot track in person. Visibility allows users to define what items their friends can see and what items are available to the general public. By marking items as private, users can also simply use the website to maintain a record of their belongings.

Production Server: http://stuffshare.pythonanywhere.com/

Server running on pythonanywhere. 

Note: some functionalities are disabled as the application currently does not have a billing account associated with it

Using the Site:
- We have test data loaded onto the site as well as several accounts:
    - Our test data images should all be public domain
    - Our text was made by ourselves
    
USERNAME: ted@sfu.ca
PASSWORD: cmpt470

USERNAME: jbhaskar@sfu.ca
PASSWORD: cmpt470

- The two of you are friends and can see one each other' friend items
- Our application code is located at web2py/applications/StuffShare/, the other files are required by Web2Py, PythonAnywhere and PyCharm

Note* Our site features are also partially explained visually on the site under the Features section of the sidebar

- Model:
	- Our model files (in the Model folder) contain the database setup Web2Py queries that connect our application to our MySQL server

- View:
	- Our view files can be found in the Views folder as well as in the Static folder
	- Python code from the controller can be embedded into the different views for display

- Controller:
	- Controller files are in the controller folder and are written in Python files
	- They contain the logic underlying our application


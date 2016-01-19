This restaurant menu web application provides a list of menu items within different restaurants. Users should have the ability to post, edit, and delete the restaurants and menu items.

## Run the server-side application

Run the python file database_setup.py to initialize the database. After this, I can find a database named restaurantmenu.db in the current directory.

Run the python file operation.py to populate the database with some prepared restaurants and menu items(Optional).

Now, run the python file webserver.py to run the web server. In your browser visit **http://localhost:8080/restaurants** to view the restaurant menu app. You should be able to view, add, edit and delete restuarants and menu items.

To stop the web server, stop running the websever.py python file.


## Funcionalities of this application

To view the homepage of the application, visit **http://localhost:8080/restaurants** in your browser. You can view all created restaurants on this page. To click the name of one specific restaurant, you can view all menu items of this restuarant. 

You can create your own restaurant by clicking the *Add restaurant* button on the webpage. The new restaurant you created will be shown on the homepage. Also, you can edit, and delete it. And you can also add menu items into the restaurant.

To add menu items, get into the webpage of one of restaurant, and click *Add Menu Items* button. After you add one menu itme, you can view it on the webpage of the specific restaurant. Also, you can edit, and delete it. 



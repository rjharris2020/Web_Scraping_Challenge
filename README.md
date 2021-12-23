# Web_Scraping_Challenge
In this challenge, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did.

## Step 1 - Scraping
Complete the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of the scraping and analysis tasks. The following outlines what needs to be scraped.

### NASA Mars News
Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that can be referenced later.

### JPL Mars Space Images - Featured Image
Visit the url for the Featured Space Image site.
Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
Make sure to find the image url to the full size .jpg image.
Make sure to save a complete url string for this image.

### Mars Facts
Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres
Visit the astrogeology site to obtain high resolution images for each of Mar's hemispheres.
There will be a need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
Start by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.
Next, create a route called /scrape that will import the scrape_mars.py script and call t scrape function.
Store the return value in Mongo as a Python dictionary.
Create a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.
Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1 - Scraping\n",
    "\n",
    "Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.\n",
    "\n",
    "* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.\n",
    "\n",
    "### NASA Mars News\n",
    "\n",
    "* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.\n",
    "\n",
    "```python\n",
    "# Example:\n",
    "news_title = \"NASA's Next Mars Mission to Investigate Interior of Red Planet\"\n",
    "\n",
    "news_p = \"Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast.\"\n",
    "```\n",
    "\n",
    "### JPL Mars Space Images - Featured Image\n",
    "\n",
    "* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).\n",
    "\n",
    "* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.\n",
    "\n",
    "* Make sure to find the image url to the full size `.jpg` image.\n",
    "\n",
    "* Make sure to save a complete url string for this image.\n",
    "\n",
    "```python\n",
    "# Example:\n",
    "featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'\n",
    "```\n",
    "\n",
    "### Mars Weather\n",
    "\n",
    "* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.\n",
    "\n",
    "```python\n",
    "# Example:\n",
    "mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'\n",
    "```\n",
    "\n",
    "### Mars Facts\n",
    "\n",
    "* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.\n",
    "\n",
    "* Use Pandas to convert the data to a HTML table string.\n",
    "\n",
    "### Mars Hemispheres\n",
    "\n",
    "* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.\n",
    "\n",
    "* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.\n",
    "\n",
    "* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.\n",
    "\n",
    "* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.\n",
    "\n",
    "```python\n",
    "# Example:\n",
    "hemisphere_image_urls = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": \"...\"},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"...\"},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"...\"},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": \"...\"},\n",
    "]\n",
    "```\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "from splinter import Browser\n",
    "import os\n",
    "import urllib.request"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {\"executable_path\": \"/usr/local/bin/chromedriver\"}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "nasa_url = \"https://mars.nasa.gov/news\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(nasa_url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Treasure Map for Water Ice on Mars\n"
     ]
    }
   ],
   "source": [
    "# Print news title\n",
    "news_title = soup.find(\"div\", class_=\"content_title\").text\n",
    "print(news_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A new study identifies frozen water just below the Martian surface, where astronauts could easily dig it up.\n"
     ]
    }
   ],
   "source": [
    "# Print news paragraph\n",
    "news_p = soup.find('div', class_=\"article_teaser_body\").text\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#JPL Mars Space Images - Featured Image\n",
    "image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Charon in Enhanced Color\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "image_name= soup.find('article', class_='carousel_item')['alt'] \n",
    "print(image_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19968_ip.jpg\n"
     ]
    }
   ],
   "source": [
    "first_url = 'https://www.jpl.nasa.gov'\n",
    "img_url = soup.find(attrs={'data-title':image_name})[\"data-fancybox-href\"] \n",
    "featured_image_url = first_url + img_url\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather\n",
    "weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(weather_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 372 (2019-12-13) low -97.2ºC (-143.0ºF) high -21.2ºC (-6.2ºF)\n",
      "winds from the SSE at 5.9 m/s (13.3 mph) gusting to 20.2 m/s (45.2 mph)\n",
      "pressure at 6.60 hPapic.twitter.com/SXXKNyUaJu\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "mars_weather= soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days\n",
       "5            Temperature:    -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mars Facts\n",
    "facts_url = 'https://space-facts.com/mars/'\n",
    "browser.visit(facts_url)\n",
    "\n",
    "# Use Pandas to convert the data to a HTML table string.\n",
    "tables = pd.read_html(facts_url)\n",
    "\n",
    "# create a dataframe to show the table\n",
    "facts_df = tables[1]\n",
    "facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "facts_df.to_html('facts_table.html')\n",
    "!open facts_table.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Hemispheres\n",
    "hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(hemispheres_url)\n",
    "\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'image title': 'Cerberus Hemisphere Enhanced',\n",
       "  'image url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'image title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'image url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'image title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'image url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'image title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'image url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product = soup.find('div', class_=\"collapsible results\")\n",
    "hemisphere_items = product.find_all('div', class_=\"item\")\n",
    "hemisphere_img_urls = []\n",
    "\n",
    "for item in hemisphere_items:\n",
    "    try:\n",
    "        hemisphere_title  = item.find('h3').text\n",
    "        hemisphere_href = item.find('a')['href']\n",
    "        hemisphere_url = \"https://astrogeology.usgs.gov\"+hemisphere_href\n",
    "        hemisphere_page = requests.get(hemisphere_url).text\n",
    "        soup = BeautifulSoup(hemisphere_page, 'html.parser')\n",
    "\n",
    "        hemisphere_page_img = soup.select('#wide-image > div > ul > li:nth-child(1) > a')\n",
    "        hemisphere_img_url =  hemisphere_page_img[0]['href']\n",
    "        hemisphere_img_dict = { \"image title\": hemisphere_title, \"image url\": hemisphere_img_url }\n",
    "        hemisphere_img_urls.append(hemisphere_img_dict)\n",
    "\n",
    "    except Exception as e:\n",
    "        print(e)\n",
    "\n",
    "hemisphere_img_urls       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

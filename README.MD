The goal of this project is to launch a Falcon 9 B5 rocket into Low Earth Orbit (LEO) without colliding with the International Space Station (ISS) or any other Starlink satellite. The successful completion of this mission would demonstrate the ability to safely and accurately launch rockets into LEO, which is crucial for a variety of applications, including scientific research, commercial ventures, and national security.

As a first step, we obtained the historical data of Falcon 9 and Falcon Heavy launches from the file "Falcon_9_and_Falcon_Heavy_launches.csv". We selected the relevant columns including the launch date and time, rocket version, launch site, payload information, orbit, customer, launch outcome, and booster landing. The selected data was then stored in a pandas DataFrame for further analysis.

We want to analyze only the data related to the Falcon 9 Block 5 launches, which is the current rocket that SpaceX is using. To achieve this, we need to filter the original DataFrame and keep only the rows that correspond to this rocket. To do this, we use a filter condition that checks for all the rows containing the string 'F9 B5' in the 'Version, Booster' column. This way, we can obtain a new DataFrame that contains only the data related to the Falcon 9 Block 5 launches, allowing us to focus our analysis on this specific rocket.

We then visualize some key information regarding the Falcon 9 Block 5 launches using a bar plot. Specifically, we plot the counts of successful and unsuccessful booster landings, as well as the counts of successful and unsuccessful launches. We do this using a subplot with two columns, one for each plot. This helps us get a quick understanding of the success rates of these launches.

[Alt text](launch_landing.png)


To achieve this goal, we will need to carefully plan the rocket's trajectory to ensure that it avoids any potential collisions. This will involve taking into account a range of factors, including the rocket's speed, altitude, and position, as well as the location and trajectory of the ISS and Starlink satellites.

First we calculates the time that will take for a Falcon 9 B5 rocket to cross the Low Earth Orbit (LEO) without colliding with either the International Space Station (ISS) and a Starlink satellite. The parameters used for the calculation are the speed of the Falcon 9 rocket, the height of the ISS, the height of the Starlink satellite, the radius of the Earth, and the speed of the ISS and the Starlink satellite.

So we continue creating a function called 'get_iss_sl_positions' that retrieves the current positions of the International Space Station (ISS) and the Starlink satellites using their respective APIs. It takes in a parameter which represents the number of times to retrieve the positions of the ISS and Starlink satellites.

The function begins by defining the URLs for the ISS and Starlink satellite APIs, and initializing empty lists for the positions of the ISS and Starlink satellites.

Next, it uses the requests library to send HTTP GET requests to the ISS and Starlink satellite APIs to retrieve their current locations. Then, the function loops through each position of the ISS and checks if the latitude and longitude of the position match any of the coordinates of interest for collision avoidance. Similarly, the function loops through each Starlink satellite position and checks if the latitude and longitude of the position match any of the coordinates of interest for collision avoidance. That is a radius of 45km arround Cape Canaveral in Florida.

If a match is found for either the ISS or Starlink satellites, the function prints a message indicating that the path is not clear. If no match is found, the function prints a message indicating that the path is clear.
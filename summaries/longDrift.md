# Summary of results from Long Drift Data
I investigated the drift of the fringes over time in the chiral piezo project. 
My goal was to determine the length of time that a researcher needs to wait before collecting data so that the laser has "settled down."

# Methods
I turned the laser on, and after a short time began recorded an
image every 20 seconds. I let this go until the camera ran out
of battery.

The images were analyzed using the python image analysis program which Niko and I have been collaborating on.
This takes a portion of the image roughly centered in the laser spot and averages the pixel values in each column.
This is reffered to as the profile data. 
The algorithm finds the maximum value in the profile, then  searches for a minimum value within 400 pixels to the left and the right of this maximum.

# Results
The results of the long-term drift study are shown in the image below.

![image](https://user-images.githubusercontent.com/6043860/148697824-d48c1a2d-9add-48f0-9830-ddda9d18a15a.png)

As the fringes shift, the first and second minimums may have discontinuities as they pass through the maximum of the Gaussian envelope.
These are clearly seen in the graph above. 
I have rudimentally corrected these shifts for the sake of more clearly discussing the data. 
The altered data for the first minimum are shown below.

![image](https://user-images.githubusercontent.com/6043860/148698089-cd2ed37d-39b6-471c-ac2b-34807f92b737.png)

We see that even after 3 hours, there is still substantial drift in the fringes. 
At it's worst, the fringes shifted approximately 1000 pixels in 50 minutes. 
The drift was not monotonic, changing directions at least twice during the data collection period.
The shortest time period between different directions of the drift was approximately 10 minutes. 
At the 3 hour mark, it appears that the fringe drift is approximately linear.
It would be worthwhile to collect this data for a longer period of time with less frequent samples to see if after 3 hours the drifting would settle down, or at least continue at a constant rate.
# Supplemental material
## Additional Method Details
To collect data consistently for such an extended period of time, I connected my Nikon D3100 to a laptop running the program gphoto2. 
I can then write a shell script to run the gphoto2 program to collect an image using the camera.

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
An image representation of this process is shown below.

![image](https://camo.githubusercontent.com/771435dadf3f09a54b4e986677729abc3ba9fac50bdfb51fb45eeb1f38a22adf/68747470733a2f2f692e696d6775722e636f6d2f313259305359762e706e67)

# Results
The results of the long-term drift study are shown in the image below.

![image](https://user-images.githubusercontent.com/6043860/148697824-d48c1a2d-9add-48f0-9830-ddda9d18a15a.png)

As the fringes shift, the first and second minimums may have discontinuities as they pass through the maximum of the Gaussian envelope.
These are clearly seen in the graph above. 
I have rudimentally corrected these shifts for the sake of more clearly discussing the data. 
The altered data for the first minimum are shown below.

![image](https://user-images.githubusercontent.com/6043860/148698089-cd2ed37d-39b6-471c-ac2b-34807f92b737.png)

# Discussion
We see that even after 3 hours, there is still substantial drift in the fringes. 
At it's worst, the fringes shifted approximately 1000 pixels in 50 minutes. 
The drift was not monotonic, changing directions at least twice during the data collection period.
The shortest time period between different directions of the drift was approximately 10 minutes. 
At the 3 hour mark, it appears that the fringe drift is approximately linear.

It would be worthwhile to collect this data for a longer period of time with less frequent samples to see if after 3 hours the drifting would settle down, or at least continue at a constant rate.
If some sort of a steady state cannot be obtained, perhaps we could investigate other lasers to see if they are less susceptible to this sort of drift. 
If this doesn't help, a method of analyzing the data which factors in the fringe drift between images collected at the same voltage will need to be adopted.

# Supplemental material
## Additional Method Details
### Automated image collection from DSLR camera
To collect data consistently for such an extended period of time, I connected my Nikon D3100 to a laptop running the program gphoto2. 
I can then write a shell script to run the gphoto2 program to collect an image using the camera.

### Thoughts on profile data 
Shown below is an example of the profile collected from one of our images.

![DSC_0012_graph](https://user-images.githubusercontent.com/6043860/148698515-b7ca27fe-9b65-442c-aa29-81740abd290a.png)

We know that this profile should be a Gaussian convoluted with a Cos(theta)^2 function.
The Gaussian envelope, however, is saturated because the laser spot is too bright. 
It would be worth examining how the quality of the data changes if we modify the camera settings so that the red sensor's data is not maxed out. 
This will certainly need to be done if we want to fit to the Gaussian convoluted with the Cos^2.
A less intense image might just result in more noisy data though. 
Further investigation is needed. 

### Smoothing Algorithms
One additional investigation that I did was into whether it is sensible to use a "smoothing algorithm" or a moving average to make our data less noisy.
I view this as giving the same benefit that you get from fitting the data to some function, without the complexity overhead of finding a good fit funciton and implementing the algorithm.
There are, however, some obvious drawbacks that come with the ease of implementing this.
In any case, the image below shows how implementing the moving average alters the appearance of the data.

![image](https://user-images.githubusercontent.com/6043860/148824931-d89bc0d8-4865-4dfe-a5b1-71e4c5c64fee.png)

I'm actually surprised how little using the moving average smoothed out the data. 
There are still frequent jumps that can be seen throughout the data collection process. 
The obvious benefits of this method are seen near index 300, where noise in the data created a local minimum which suddenly jumped to another location. 
The minimum of the fringe would actually be in between these two points, which the moving average algorithm handles fairly nicely.
The profiles where this jump happens are shown in the two images below.

![image](https://user-images.githubusercontent.com/6043860/148825462-f762ed86-aa40-4dcc-b553-c0823dffbe62.png)

![image](https://user-images.githubusercontent.com/6043860/148825485-4b4a4fc7-3852-4e04-8d31-c96c802f4a0f.png)

Finally, I also want to show a comparison of how the moving average smooths the data.
I'll show the same two sets of profiles that are above, but with the moving average applied.

![DSC_0340_graph](https://user-images.githubusercontent.com/6043860/149027977-3c62a44f-05e3-40c0-82fd-a3564c2682ff.png)

![DSC_0342_graph](https://user-images.githubusercontent.com/6043860/149027978-36bdf7f7-57e3-43e9-9bee-787cb72d885c.png)

While the smoothing algorithm is a nice intermediate step, I think the end goal should still be fitting a function to the data.
In order for this to work, we can't have the profile be saturated, see above comments on profile data.
I would recommend doing a study where images are collected with different camera settings to see if it is feasible to still have usable data when the profile isn't saturated.
We might want to turn the lights off in the room to see if that improves the quality of the data.






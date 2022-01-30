Profile Width Effect on data smoothness
===
While I was troubleshooting automatically finding the vertical center of the 
beam, I stumbled across this piece of knowledge about smoothing the data
by including more of the profile.

With a small profile width under 200 as we have been using for our data 
colleciton, the intensity is fairly noisy and can result in jumps in the 
location of the minimum. This problem is mitigated by using a larger profile
which helps to average out the randomness. I show here two images, one 
analyzed with the small profile width of under 200 pixels (I can't remember if it
was 120 or 160 or 140) and the other is analyzed with a large profile width
of the entire image, roughly 3000 pixels.

150 pixels
---
![partial_image_profile](https://user-images.githubusercontent.com/6043860/151714186-bd487e1c-304f-4466-bb44-9c7d7f3bed11.png)

3000 pixels
---
![full_image_profile](https://user-images.githubusercontent.com/6043860/151714151-f8ad4ff0-1638-4d5b-8ed3-291a71e55541.png)

The drawback is of course computation time. The 150 pixel analysis took less
than 5 seconds, while the 3000 pixels took something like 27 seconds. 

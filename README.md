# Dendrogram clustering

This program clusters an image file into a dendrogram using the Astropy module

Upon running main.py, plots will be produced showing the original image, 
the image with the largest point circled, a dendrogram of the image, a dendrogram
with a structure highlighted (you can change the structure by changing the int value),
a contour of the structure (similarly, you can change the structure by chaning the value),
a contour with all of the leaves, print the statistics for the data.

The goal with this unsupervised learning would be to identify certain clusters of signals.
These clusters could be labeled, such as saying "a dendrogram with _____ characteristics 
represents a ______ formation". This could be used to process large amounts of 
data. Then, similar clusters could be identified and automatically labeled. 
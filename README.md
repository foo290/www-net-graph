# www-net-graph
Given a link, will draw all the connected web pages to that link and further more upto a threshold,
as one webpage can be connected to trillions of webpages.

The input of Href parser increases beyond the O(n!) because one webpage gives you at least 40 links, and those 40 will give 40 each and so on,
and because this is not some computational overhead but rather dependent on IO (for fetching the webpage),
this program uses threads to improve performance.

Where normal(without threading) can take upto 5-15 minutes to parse 1000 links, using threading this is achieved in less than 10 secs. (also dependent on your internet speed) 

## Sparse
<img width='700px' src="https://github.com/foo290/www-net-graph/blob/main/readme_images(Non-Project)/Screenshot%20from%202021-07-09%2017-45-25.png">

## Dense
<img width='700px' src="https://github.com/foo290/www-net-graph/blob/main/readme_images(Non-Project)/Screenshot%20from%202021-07-09%2013-39-36.png">


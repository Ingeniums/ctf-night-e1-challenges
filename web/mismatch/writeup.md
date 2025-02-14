# How to solve
This is a basic challenge that exploits a vulnerability in the application's code.
The challenge has a single page with a select, an image display, and an input,
changing the value of the select changes the displayed images, and the text in the adjacent input.

Changing any character in the quote associated with the name/the image (hence creating a __mismatch__ between 
the values), hides the image.

As per the second hint, viewing the source code for the HTML you can see that a new hidden input is added 
putting the values `nothing_to_s33_h3r3` in the input will take you to a new page.

The page contains an image of the person to which the first quote --in the description-- belongs.

You can find the flag in the meta-data of the image, using `exiftool` or any other similar tool.


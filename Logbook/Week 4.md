
# 100 Days of Code - Log For Week 4


### Day 20: June 12, 2017

**Today's Progress:** Not a lot to be honest. I went back to my weather app and wanted to add in some google maps features. What I did was break everything. 

**Thoughts:** This was a toughie! I've not used jQuery in a while and I made some really simple mistakes. It took me over an hour to get out of the bugs I'd put into my code. The positive result was that I'm now feeling quite refreshed with jQuery, but it's highlighted the importance of keeping up with everything. There's a jQuery section coming up on my treehouse track in a few days - I need to really practice that content when I get there.

**Link to Work:** (Day 20)["to fill in"]

---


### Day 21: June 13, 2017

**Today's Progress:** Today was one of my "study whatever I like days". I wanted to study some python, but I haven't used it in a while, so wasn't confident, and not sure what to do. I decided to check out the treehouse forums and find a question that would make a good challenge

**Thoughts:** This was a lot of fun! I found a couple of questions and really got to practice some advanced stuff! The main project was swapping keys and values in a dictionary. I had to identify potential problems - like mutable values, how the dictionary is formated, how external API's might change, etc. 

I learned about the .__hash__ method, the zip() function, dictionary comprehension and filter methods (previous question). It really helped keep my python fresh, and I'm becomming constantly more confident in python 3, not always thinking in python2.

**Link to Work:** [Day 21]("")


---



### Day 23: 15th June, 2017


**Today's Progress: **Today I refactored and optimised yesterday's random color project. I also added support for window resizing.

**Thoughs:** Wow, learnt so much! yesterday I was just seeing if I could do it, today, I've been reallyi g thinking about the design and researching how to do what I wanted. I've learnt a lot, and managed to massively inprove the complexity of my code - over 50% cpu time reduction and the ability to run smoothly at 5x the speed where my browser was struggling to keep up yesterday.

I achieved this by only populating the dom once, and pre-generating an array of colors to use. below 100 colors in length this is much faster, though inevitably as the length of the color pallet increases, the performance gain is lost until it becomes quicker to generate each random number again. however i found that at around 64 colors, the result is visually similar to the previous code, and allows me to use further restriction in color hue range. 

i think I'd like to return to this, i have an idea for a shimmer effect using a similar approach.
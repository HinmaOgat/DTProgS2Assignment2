Technologies
---
As the focus of the latest assignment was on developing a HTML webpage, the weeks leading up to it were focussed on developing knowledge of the languages needed to do so.

Week 1 was dedicated to learning HTML, a markup language used to create web pages. ‘Week1.html’ was developed using the various tags and properties in HTML that were learnt this week.
CSS was learnt in Week 2. CSS, or Cascading Style Sheets, is used to add styles and colour to a HTML webpage. CSS makes a webpage more appealing, resulting in a better user experience. It is important for webpages as it allows for more complex stylistic and structural choices to be implemented into a webpage. For example, a webpage without CSS is limited to the browser’s default fonts; this reduces the customisation possible.  
CSS was implemented into [week1.html](week1.html) to develop [week2.html](week2.html). [week2.html](week2.html) includes more components: it uses divs, to structure the webpage and make styling those different sections easy by applying a class to them. It also uses the style tag to hold the necessary CSS:

```
<style>
body{
    font-family: 'Trebuchet MS', sans-serif;
}

.topBar{ /*First row of header, containing logo*/
    background-color: rgb(66, 166, 66);
    color:rgb(240,240,240);
    height:auto;
    vertical-align: center; 
    font-family:monospace;
    text-align:center;
    user-select:none;
    overflow:visible;
}

.logo{
    color:rgb(240,240,240);
    font-size: 40px;
    font-family:monospace;
    font-weight:bold;
}

.menuBar{ /*Second row of header, containing links to all pages of website*/
    background-color: rgb(66, 166, 66);
    border-color:black;
    height:auto;
    display: flex;
    vertical-align: center;
    text-align:center;
    user-select:none;
</style>
}
```
This makes the elements in the website easy to apply properties onto; this is because all classes or (groups of elements) can be styled at once, instead of individually, by using their CSS rules. 

This progression in skill was important, as the final assessment submitted and the second provided document have multiple similarities; both have fillers on the side of the content, both have a one-column layout in the middle. This shows the skills gained from practising HTML assisted in the development of the assessment.

The final HTML task has added complexity, including more unique CSS properties such as the fixed property; this makes elements remain on a user’s screen as they scroll:

<img src="Resources/fixedPositions.gif" width="500" height="300" alt="Demonstration of how elements remain on a screen while being scrolled">

Additionally, Javascript was learnt in Week 3. It is used to add interactivity to a webpage, thus making the page more engaging and dynamic, and is easy to integrate. Javascript is a programming language unlike HTML and CSS (which are mark-up and style sheet languages respectively); this makes it useful as a server-side language, as it can manage the handling and manipulation of user data. One example of Javascript’s application in a web page is the hangman game implemented in the final HTML task submission, which would not be possible with just HTML and CSS (as logic is required).

<img src="Resources/hangmanDemo.gif" width="500" height="300" alt="Demonstration of the hangman game">

These show how, during the development of the HTML task, more technologies were learnt, existing ones were improved upon, and the skills gained were implemented to develop a more interesting and functional website.
 
___
Any application involving user interactivity will need a front-end, as mentioned above. Using HTML/CSS for this front-end purpose has numerous advantages:  
 - HTML is lightweight and fast to load, meaning if it is a front-end for a large application, it will not contribute to as many loading issues. 
 - It integrates easily with other languages such as JavaScript, CSS, etc. This means most back-end languages that may be used in future would be integrable with HTML. 
 - HTML is supported by most popular browsers. This increases user convenience, as the webpage will work regardless of the browser they use.
(GeeksforGeeks, 2020)
___

Additional study into Javascript was done after the basics. More advanced skills were learnt, in particular Object Oriented Programming (OOP); these skills will be beneficial for future projects requiring higher-level programming, such as complex apps or games. The knowledge gained from learning OOP was implemented into the program shown in the file [jsDemonstration.html](jsDemonstration.html), showing the use of classes and inheritance.
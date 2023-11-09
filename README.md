# MiniBuzz-News

Website presents an alternative game to the classic "Rock Paper Siccors" by adding two other elements including Lizard and Spock. Users can can play against computer for attempt to get 3 wins before the computer does.
This project has been done as my second portfolio project at Code Institue. JavaScript, HTML and CSS have been used in creating this web-based game.

The link to the website can be found below:
https://amiirsalimi.github.io/Rock-Paper-Scissors-Lizard-Spock/

<img src=screenshots/mockup.jpg>

# User Experience
## Owner goals
My main purpose of creating this website was to get my project done and present my learning outcomes from JavaScript, CSS and HTML,  I chose to create this game since it involved some simple math to design an algorithm which I found utterly interesting and helped me develop further knowledge on JS and made me dig deeper into the world of JS and algorithms which were not covered in the lessons.
## User goals
The user may enter the website to play the game against computer in order to be enterntained. They can learn about the logic of the game through the learn page as well.

# How the game works:

‚Ä¢	Each object wins against 2 and loses against other 2.

‚Ä¢	Rock smashes scissors and crushes lizard.

‚Ä¢	Paper covers rock and disproves Spock.

‚Ä¢	Scissors cuts paper and decapitates lizard.

‚Ä¢	Lizard eats paper and poisons Spock.

‚Ä¢	Spock smashes scissors and vaporizes rock.

Whomever between the user and the computer wins 3 round first is the winner.

# How to find the winner through an algorthm:

To find the winner, the first idea that comes to mind is to use a simple if statement and simply declare who won like this:
If userResult is ‚Äúrock‚Äù and cpuResult is paper, then cpu won, and so on and so forth.
The second solution that comes to mind is to use math in the process:
We assign a number for each object.
Rock is 0, paper is 1, scissors is 2, lizard is 3 and Spock is 4.
Then by using mod5,
Simply by dividing user value and computer value and finding the remainder of that number by 5, you can declare if the user won or computer. 
If you do this a few times, you‚Äôll understand that if computer wins, the value of it is always even, and if user wins, the value is always odd.
For example, if user chose lizard (4) and computer chose scissors (3),
(4-3) mod 5 = 4 : the result is even, so the computer won.



# Features and Structure of the Website
The website consists of 2 pages including : "Play" and "Learn"

## Play
At the top of the page, there is a navigation bar which lets the user navigate through the two pages of the website. Then in a container below the user can play the game and choose an option among the 5 choices they have which includes 


<img src=screenshots/play.jpg>

## Learn
At the top we have the same navigation bar as the play page.
Then there is a header with the title of the game and below it there is a paragraph which quotes "Sheldon Cooper" the famous charachter of the sitcom series "Big Bang Theory" in which he explains how the game works. Then, there is image consisting of the relation between each element of the game.

<img src=screenshots/learn.jpg>


# User Interface

## colors

I used minimaslistic colors with a good contrast. Both pages of the website have a background color of #ced0d6 which is a light bluish purple. For the fonts I chose the color black.

## Fonts
I used Roboto Condensed as the main font  and sans-serif as backup.

## Images
I used a sort of flow chart that I found on the web which indicates the effects the 5 elements of the game have on eachother.


## Icons
I used 5 icons in total for each element of the game. The icons were free png's downloaded from the web and are mentioned in the credits section. Though, it is worth mentioning that I added another icon for lizard which was the same but at a different angle for better design purposes given it would not look good at certain angles.

# Technologies used

### HTML5
As the structural language
### CSS3
As the styling language
### JAVASCRIPT
As the logic language
### GitHub
As a platform to keep the project files as well as hosting my website through GitHub pages.
### Codeanywhere
As a coding and development platform.
### Git
As a version-control system
### Google fonts
As a resource provider for fonts.


# Testing

## Responsiveness
I used Chrome developer tools all the way through the project this helped me with making my website responsive and figuring out styling issues so that I could fix them.

## Compatibility
I loaded the website hundreds of times on my macbook pro 14 inch as well as 27 inch 4K monitor to check for issues. On my iPhone 14 pro max. Additionally, I checked on a smaller iphone 11 and macbook air and asked friends to play with it as well.

## W3 html validator
I used this tool to validate my codes. Except for the fact that I had used paragraph elements as child elements of span elements which created some errors which then were fixed, there was not an issue.




## W3 CSS validator
There was not even a single mistake or error.

## JShint
Other than some little info which were given for clarity there weren't ant issues that would make any change to the way the code works.

# Issues found during the development

I had many issues with my IDE and since the institution I study at has started using it, it was a better choice for me to keep working with it. However, it went on going online and offline which was frustrating and I even could not load my work space for some very long hours. Therefore, for some bits of the code when I had no access. I had to use VScode on my computer and as I do not have access to CodeAnywhere again, I am writing this ReadMe file on GitPod.

The design of the Algorithms was a bit complicared too but since I am interested in math and algorithm, I digged the web to find a way to make an algorithm which would work.

I had many issues during the development of the JS bit. I had to a lot of reasearch on the web to find out how I could do certain stuff like switiching the pictures which helped me with further knowledge on JS.

I had to create a resposnive website so that the game and the learn page would look on any device. This was time consuming at times and had to be redone after slightest changes.


# Deployment

I used GitHub pages to deploy my website. Through this link:
https://amiirsalimi.github.io/Rock-Paper-Scissors-Lizard-Spock/

In addition, I used python3 -m http.server command to deploy the website while developing. I made the link public so I could use other devices as well.

The website could be run locally through the depositopry as well:
https://github.com/Amiirsalimi/Rock-Paper-Scissors-Lizard-Spock


# Credits

To complete this project I used Code Institute student template:
https://github.com/Code-Institute-Org/ci-full-template

I used Google fonts to import fonts.

I used the below icon resources:
https://thenounproject.com/icon/lizard-hand-389090/
https://www.flaticon.com/free-icon/fist_3562093
https://www.flaticon.com/free-icon/vulcan_4151704
https://www.flaticon.com/free-icon/scissor_4958094?term=scissors+hand&page=1&position=35&origin=search&related_id=4958094

Web and google were very helpful in finding resources for me to learn commands and bit of code that I had not learned about till then. I learned a lot on the web about designing algorithms so that I could create this game.
and of course, the materials that I studied on Code Institute LMS and some points learned on Slack, helped me as well.



# Screenshots

<img src=screenshots/1.jpg>
<img src=screenshots/2.jpg>
<img src=screenshots/3.jpg>
<img src=screenshots/4.jpg>
<img src=screenshots/5.jpg>
<img src=screenshots/6.jpg>






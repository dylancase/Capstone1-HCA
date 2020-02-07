Exploration of Home Court Advantage in the NBA
-----------------------------------------------

Questions to explore:

How big of an effect is Home Court Advantage (referred to as HCA from here on)?
Any noticeable trends? Is it getting stronger or weaker?
What game statistics are most/least affected by HCA?
Why might those statistics be affected by HCA?
Does attendance, average travel distance, or elevation have an effect?
If an NBA team wanted to maximize HCA and/or minimize Away Court Disadvantage what strategies might they employ?

-----------------------------------------------

Preliminary Hypotheses

-HCA is a well known phenomenon, so I imagine it will be noticeable and have a fairly significant effect.

-Perhaps HCA is declining, because teams may be trying to account for it, travel to away games sooner to
acclimate, nicer planes for more comfortable travel.

-Some statistics it may affect more than others: perhaps the number of fouls, people often complain about ‘home cooking’,
perceived bad calls in favor of the home team.

-Attendance may have an effect, louder fuller stadiums perhaps give the home team a bigger boost. Average
travel distance could certainly have an effect on a travelling team. Elevation is certainly known to have effects
on performance so it too would likely have an effect


-----------------------------------------------

Data Sources:

ESPN Standings (Home and Away records): 2002-2019
ESPN Attendance Stats: 2001-2019
ESPN Pace Statistics: 2002-2019
NBA - Game Statistics: 1996 - 2019

-----------------------------------------------

How the data was gathered:

ESPN
-------
Scraping ESPN was fairly straightforward using Pandas read HTML
Once I had a pandas dataframe, I had some minimal cleaning to do, occasionally needing to recast data types
Then I created any extra columns I needed (e.g. Home Win Percentage, Away Win Percentage, Season)

NBA
-------
Scraping the NBA data was a little trickier:
The tables with the data were done using javascript and as such the data was not present in the site’s html
So instead I inspected the page and selected XHR under the network tab and looked for a listing that might be the table. Then chose to copy as cURL.
I plugged that into a cURL to Python translator (https://curl.trillworks.com/)
And was then able use requests to get the java script. Exploring the javascript I was able to construct a Pandas Dataframe with the data

-----------------------------------------------

Findings:


Home Court Advantage has a very significant effect in the NBA. In the last 15 seasons Home win percentages have on average been no less than
15% higher than away win percentages, and have been as high as 22% higher.

Home Court Advantage seems to be declining in general. From averaging about a 20% win percentage difference from 2005 - 2013, to averaging only
about 17% in the last 5 years.

Assists seem to be most affected by home court advantage. Interesting because assists is one of the more subjective statistics. Perhaps this is indication
of home team statisticians giving out assists more generously for the home team.

Personal Fouls are only modestly affected, probably not enough of an effect for the home cooking theory to be the full picture of Home Court Advantage

Free Throw Percentage not really affected much, makes sense, not very demanding kind of play, even if players are fatigued from travel or elevation,
also not something a referee can affect

Why is HCA declining?

-One theory is that the increase in three point field goals attempted per game is leading to a decline in home court advantage

Could be several reasons for this:
-You’re less likely to be fouled on a three point shot, so fewer chances for foul calls or home cooking to have an effect
-A three point attempt is less physically demanding than most two point plays so it is perhaps not as affected by fatigue
potentially caused by travel or a difference in elevation
-More three point shots might lead to a higher margin of victory thus negating the effects of an extra couple free throws
(home cooking theory) or it puts the game out of reach before fatigue can really set in

So is HCA correlated with three point shots attempted?

HCA is most strongly correlated (inversely) with Rebounding and 3-point shot attempts, supporting the theory that
the three point shot might be at least in part responsible for the decline in HCA.

Why rebounding?

Well again that likely is due to the rise in the three point shot. Three point shots are missed more often that two point shots leading to more rebounds

Three point field goals attempted is also very strongly correlated with a rise in score differential or margin of victory, adding more
evidence to the theory that the rise in three point field goals are responsible for a decline in HCA


Does attendance have an effect?

No, avg attendance does not show correlation with HCA

Time Zone?

Teams from time zones further west were shown to experience slightly stronger effects of HCA

A possible theory for this is that teams on the west coast may have a slight advantage over east coast teams when travelling
The idea is that if you are playing a 7pm game on the west coast that feels like 10pm for the east coast team, and if you are playing
a 7pm game on the east coast, that feels like 4pm for the west coast team
If you are planning to compete in a physical activity I imagine you would prefer to compete at 4pm than at 10pm

Elevation?

Elevation has a strong effect for the two highest elevation teams: The Denver Nuggets and the Utah Jazz

For the rest of the teams it seems to have no effect

-----------------------------------------------

How might a team maximize HCA?

Build your stadium as high as possible, expansion teams look at Mexico City, or perhaps Provo, Utah

Defend the three point line, try to force the other team to settle for 2 point field goals

Maybe try a stadium in the Pacific or Central Time Zone, may not have an effect, but just in case…

How might an away team minimize HCA?

Practice/train in high altitude or simulated high altitude conditions

Shoot a lot of threes

Play at a fast pace, try to get a high score differential (put the game away before the 4th quarter


-----------------------------------------------

Skills Developed

Pandas
Matplotlib
Hypothesis Testing

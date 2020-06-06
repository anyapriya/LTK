# LTK

This is a tentative plan for getting the game up and running, but everything is just ideas and we can change stuff as we go 




-------------------------------

## I. Get Game working!  

#### <s>A. Do basic outline to figure out structure </s>

#### <s>B. Get something working </s>

#### C. Add in turns 
- no characters or equipment yet, and a few cards hardcoded in
- maybe first choose 3 cards like strike, dodge, peach and get game working for those


#### D. Add in non-equipment cards one at a time and make sure they each work (and write unit tests for each as well go) - this should be easy to divide up

#### E. Add in equipment functionality - might be a bit complicated

#### F. Set up database for cards and incorporate that into code (that way there can be multiple decks like base game, expansion, etc) - means can use SQL! Will be tedious.....
- might need to set up server first, see part III

#### G. Add in characters
- probably the most tedious part of getting the game up and running
- can start small with a few
- can use database to keep track of which characters are allowed in which game mode (i.e. if some are Kingdom Wars only), but will still have to hardcode them all in

-------------------------------

## II. Logging and Testing 
#### <s>A. Set up initial logging </s>
#### <s>B. Set up initial tests </s>
#### C. Add in testing / logging for everything we have so far 
- Make sure to keep adding tests / logs for additional stuff we write!
#### D. Set up automated testing / workflow
- Jenkins?
#### E. Error reporting
- If this is being run on other people's computers, will eventually need a method to do optional error reporting (ask for permission) by sending logs back to the server if something goes wrong

-------------------------------

## III. Set it up so game can be played remotely with people 
#### A. Figure out what specs we need
- Can probably use David's servers but he wants to know what specs we'll need so gotta figure that out
#### B. Work with David to set up server

-------------------------------

## IV. Figure out method of distribution for Game and UI

#### A. Are we doing web application (easier for others) or downloadable application (easier for us)
- web application might necessitate javascript
- if we do downloadable application, I think gui will be easier to do in straight python 
- if we do downloadable application, look into pyinstaller as well as other options


-------------------------------

## IV. Record data about games and make cool graphs!!!  

-------------------------------

## V. AI CPU for game


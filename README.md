tripadvisor.com

Country Specific Webscrape for Puerto Rico

Downloads 100-200 attractions with data:
	Activity
	Link
	Price
	Rating
	Reviews
	

Uses Selenium

Chrome Webdriver Required

Step 1 - Navigates to provide URL

This URL can be amended for different countries or attractions in the code

i.e. substitute https://www.getyourguide.com/puerto-rico-l169159/ with https://www.getyourguide.com/france-l169008/

Step 2 - Clicks on 'Show more' button ten times to add 100-200 attractions to page

Step 3 - Scrapes Page

Step 4 - Outputs .csv file


Note 1: If you download this code you need to update with your path for the output file

Note 2: TripAdvisor frequently updates their pages. If no output and get error stack traces like below then you may need to re-inspect the Website Structure:

Double-check the XPaths and CSS selectors being used to locate the elements. Make sure they accurately target the desired elements on the page.
Use browser developer tools to inspect the HTML structure and ensure the elements you're trying to access are present and have the correct attributes.




Error processing tour 174: Message: 
Stacktrace:
	GetHandleVerifier [0x00007FF62C8AB125+29573]
	(No symbol) [0x00007FF62C81FF50]
	(No symbol) [0x00007FF62C6DB6EA]
	(No symbol) [0x00007FF62C72F815]
	(No symbol) [0x00007FF62C72FA6C]
	(No symbol) [0x00007FF62C72312C]
	(No symbol) [0x00007FF62C75733F]
	(No symbol) [0x00007FF62C722FF6]
	(No symbol) [0x00007FF62C757510]
	(No symbol) [0x00007FF62C7786BC]
	(No symbol) [0x00007FF62C7570A3]
	(No symbol) [0x00007FF62C7212DF]
	(No symbol) [0x00007FF62C722441]
	GetHandleVerifier [0x00007FF62CBDC76D+3377613]
	GetHandleVerifier [0x00007FF62CC27B67+3685831]
	GetHandleVerifier [0x00007FF62CC1CF8B+3641835]
	GetHandleVerifier [0x00007FF62C96B2A6+816390]
	(No symbol) [0x00007FF62C82B25F]
	(No symbol) [0x00007FF62C827084]
	(No symbol) [0x00007FF62C827220]
	(No symbol) [0x00007FF62C81607F]
	BaseThreadInitThunk [0x00007FFF155B257D+29]
	RtlUserThreadStart [0x00007FFF1648AF08+40]

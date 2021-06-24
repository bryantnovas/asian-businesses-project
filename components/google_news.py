from pygooglenews import GoogleNews
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import requests
import numpy as np
import pandas as pd
gn = GoogleNews()


def app():
    st.write(
        '''
        # **Analyzing Google News Articles for Anti-Asian Crimes:**

        ## **Background & Introduction:**

        ### **Why Google News?**

        Unlike many other forms of News API and News library, we are able to identify all news sources rather than just one. Google News as a whole generates newsites based on headlines from worldwide groups that identify similar ideals.Google News helps us looker deeper into headlines.


        ### **Objective**

        The overall objective is to understand the relationship between negative connation surrounded with Anti-Asian crimes that was reported in the news. Many people who are Anti-Asian(Pacific Islander ) community did not feel comfortable disclosing hate crimes. Many people are unaware of were to report Hate Crimes, however news articles reflect real time data of the current news that is taken place. 

        ### **Hypothesis:**

        By looking for common words that were negatively associated within articles that were identified as Anti-Asian, we can determine the relationship between the Anti-Asian crimes that exist. We can also analyze how Anti-Asian crimes have shifted throughout the pandemic and currently are potrayed in the news to identify how badly impacted the Asian communities were harmed. My hypothesis is that the words that are negatively associated within the newspaper articles surrounding the news around Anti-Asian crimes has increased. Overall impacting the business traffic of Asian business and increasing hate crime surrounding Asian communities. 

        ## **What Libraries We Would Be Using For This Project?**
        We would be using a python library named pygooglenews.This library was created by Artem from the newscatcherapi  This library allows us to get top stories, top related news feed, and  geolocation news feed and do an extensive full search on the key terms needed on your news.

        ## **How this Differs From Other Libraries?**
        - There is an extensive search to simplify your searches.
        - You are able to parse through sub articles,containing a subset of 
        similar news for each artcle
        ### **Documentation:**
        https://github.com/kotartemiy/pygooglenews#installation

        ### **Downloading the Google News Library**
    ''')

    st.write('`pip install pygooglenews --upgrade`')
    st.write('`pip install gsutil`')
    st.write(
        '''`
        pip install feedparser 
        pip install feedparser --upgrade
    `''')

    st.write(
        '''
        ## **Link to Documentation** 
        https://pypi.org/project/GoogleNews/


        ## **Analysis on Our Data:** 

        ### **This is the Google News library being inatialized**
    ''')

    st.write('We are specifying what location of Google News we want our data to be in since we are analyzing data in NYC we only want to view News Articles  within NYC.')

    headquaters = gn.geo_headlines('New York City')

    st.write('We are identifying articles that occur with the top search of Anti-Asian Hate Crime within the last 16 months because Hate Crimes began the top search of Anti-Asian Americans.')

    search = gn.search('Anti-Asian Hate Crimes', when='16m')
    st.write(search)
    st.write('Parse through the entries because we want to specifically identify the titles of the loop.')
    st.write(search['entries'])

    st.write('We are storing our entries into a string because our information is in json format. Each line will be represented into a new line and printed within the titles only of our search')

    words = ""
    for entry in search['entries']:
        words += entry["title"] + '\n'
    st.write(str(words))

    st.write('Now we are going to take the links of our searches to be able to identify the key words that are asssociated inside of these articles. ')

    links = ""
    for entry in search['entries']:
        links += entry["link"] + '\n'
    st.write(str(links))

    st.write('We are installing the wordcloud library so we can take a greater look at the top searches and the common words that were identifed within the titles of the top searches.')

    st.write('pip install wordcloud')

    st.write('PIL import image library allows us to create an image.STOPWORDS highlights all the words.ImageColorGenerator allows to create an image with different colors.')

    st.write('We are going to take the string that we formatted and generate a wordcloud around it and display the generated image')

    wordcloud = WordCloud().generate(words)

    st.write('Display the generated image:')

    with sns.axes_style("white"):
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
    st.pyplot()

    st.write('Within the last couple months these have been the most common words that have been identified in the top search article titles, we can identify it based on the impact that the words have and how large the words are')

    st.write('Now I am making a dictionary of words that have been popping up in news articles that relate to a negative connotation towards the Anti-Asian community. All words are set to a value of 0, to increment the value as we iterate through all articles')

    x = {
        'shooting': 0,
        'assault': 0,
        'attack': 0,
        'death': 0,
        'fight': 0,
        'killed': 0,
        'hate': 0,
        'rape': 0,
        'harmed': 0,
        'harm': 0,
        'violence': 0,
        'violent': 0,
        'hate': 0
    }
    list_of_words = ['shooting', 'assault', 'attack', 'death', 'fight', 'killed', 'hate', 'rape', 'harmed', 'harm', 'violence',
                     'violent', 'hate']
    x = {
        i: 0 for i in list_of_words
    }
    st.write(x)

    st.write('We are importing requests to later get the text and then taking the urls from the search entries and parsing it into urls into a list')

    list_of_urls = [
        'https://www.boston25news.com/news/health/community-leaders-hold-forum-anti-asian-racism/RMU73KFI6VETJCMH2X6ZOZEEJE/',
        'https://www.cbs58.com/news/more-assaults-on-asian-american-women-reported-in-san-francisco-baltimore-and-new-york',
        'https://finance.yahoo.com/news/nfl-player-taylor-rapp-launching-200854041.html',
        'https://www.crfashionbook.com/beauty/a36202945/14-asian-owned-beauty-brands-to-support/',
        'https://www.daytondailynews.com/local/locals-call-to-end-hate-against-asian-americans/QFXUYEPGTRAS5GU473ZOERPUF4/',
        'https://www.daytondailynews.com/local/greene-county-activists-plan-one-year-memorial-event-for-george-floyd/D3ASLDPJNZELJHZYXHKASQPM6A/',
        'https://www.bbc.co.uk/news/live/world-us-canada-55629665',
        'https://www.ctvnews.ca/world/un-official-terrorists-using-pandemic-to-stoke-extremism-1.5264528',
        'https://www.hrw.org/news/2016/09/13/hungarys-xenophobic-anti-migrant-campaign',
        'https://finance.yahoo.com/news/vehicle-electrification-market-research-report-183400017.html',
        'https://www.justsecurity.org/70952/just-securitys-new-co-editor-in-chief/',
        'https://www.wect.com/2019/02/22/watch-puppy-cries-over-sad-lion-king-scene/',
        'https://www.bbc.com/news/world-us-canada-39732845',
        'https://www.independent.co.uk/news/world/americas/us-politics/trump-china-flu-coronavirus-asian-b1851518.html',
        'https://www.nytimes.com/2019/01/23/sports/lindsey-vonn-wont-retire.html',
        'https://www.ft.com/content/f793f132-96f8-11e7-b83c-9588e51488a0',
        'https://www.sun-sentinel.com/opinion/commentary/fl-op-com-hate-crimes-atlanta-shooting-20210329-fkcohptu2veyvkdpw42xc5jbl4-story.html',
        'https://www.orlandosentinel.com/news/nationworld/ct-aud-nw-nyt-biden-anti-asian-attacks-20210331-aysi4o44hngqnmaouxrrho25nm-story.html',
        'https://news.yahoo.com/man-charged-hate-crimes-kicking-160416510.html',
        'https://news.yahoo.com/entrepreneur-brothers-donate-100-t-203703166.html',
        'https://www.globalcitizen.org/en/content/marvel-introduces-asian-superhero-shang-chi/',
        'https://ph.news.yahoo.com/us-olympian-sakura-kokumai-describes-racist-attack-while-training-at-park-132107093.html',
        'https://news.yahoo.com/asian-american-artist-recorded-racist-133000585.html',
        'https://news.yahoo.com/racist-terrorizes-chinese-familys-children-233828892.html',
        'https://www.mercurynews.com/2021/03/19/tv-tonight-the-falcon-and-the-winter-soldier-blazes-onto-disney',
        'https://thehill.com/changing-america/enrichment/arts-culture/549050-marvel-introduces-asian-superhero-played-by-simu-liu',
        'https://www.pilotonline.com/nation-world/ct-aud-nw-nyt-chinese-grandmother-attacked-san-francisco-20210326-sbuo2ehn65cj7nfyrdg4fv6qme-story.html',
        'https://ph.news.yahoo.com/elderly-fil-am-violently-attacked-011320023.html',
        'https://ph.news.yahoo.com/stock-asian-owned-food-brands-151223463.html',
        'https://www.orlandosentinel.com/news/crime/os-prem-ne-central-florida-capitol-rioters-20210320-t25ecsgoyjddrmxxfgh7eocy2i-story.html',
        'https://money.yahoo.com/gates-opening-simu-liu-having-181059750.html',
        'https://globalnation.inquirer.net/195994/carpio-dutertes-betrayal-of-natl-interest-over-wps-an-impeachable-offense',
        'https://money.yahoo.com/why-costco-may-still-win-140539778.html',
        'https://www.arabnews.com/node/1817731/lifestyle',
        'https://ph.news.yahoo.com/bystander-effect-anti-asian-crime-173833831.html',
        'https://news.yahoo.com/teen-vogue-staffer-supported-mccammond-005806130.html',
        'https://ph.news.yahoo.com/global-tourist-arrivals-down-87-102100559.html',
        'https://ph.news.yahoo.com/lamborghini-kicking-off-electrification-plan-142746906.html',
        'https://www.middleeastmonitor.com/20210404-over-16m-coronavirus-vaccine-doses-administered-in-turkey/'
        'https://floridapolitics.com/archives/421587-sunburn-the-morning-read-of-whats-hot-in-florida-politics-4-20-21/',
        'https://money.yahoo.com/scaramucci-bitcoin-apex-predator-ethereum-014728081.html',
        'https://ph.news.yahoo.com/sidewalk-labs-launches-pebble-sensor-143008442.html',
        'https://ph.news.yahoo.com/jaguar-land-rover-posts-534-m-profit-thanks-to-strong-sales-in-china-141826324.html',
        'https://newsinfo.inquirer.net/1404248/duterte-empower-filipinas-reject-backward-mindset-that-fuels-oppression-inequality',
        'https://newsinfo.inquirer.net/1385895/minimum-wage-earners-decry-high-food-prices',
        'https://ph.news.yahoo.com/tess-holliday-anorexia-001625754.html',
        'https://thehill.com/homenews/senate/551345-romney-booed-during-speech-to-utah-gop-convention',
        'https://ph.news.yahoo.com/pediatrician-reveals-why-ditch-gender-160023718.html',
        'https://newsinfo.inquirer.net/1353031/duterte-orders-govt-agencies-to-observe-transparency-in-procurement-process',
        'https://ph.news.yahoo.com/manila-chooks-tm-heavy-underdogs-235200896.html',
        'https://ph.news.yahoo.com/mlb-angels-releasing-future-hall-of-famer-albert-pujols-175133334.html',
        'https://news.yahoo.com/ohio-republican-lawmakers-propose-renaming-203844996.html',
        'https://money.yahoo.com/coronavirus-stimulus-gop-plan-for-unemployment-benefits-hits-snag-over-mechanical-issues-170027326.html',
        'https://www.arlnow.com/2020/06/20/county-apologizes-for-removing-girls-black-lives-matter-chalk-art/',
        'https://www.nytimes.com/2020/07/30/opinion/the-argument-authoritarianism-anne-applebaum.html',
        'https://news.yahoo.com/interview-britains-first-tiktok-house-164939960.html',
        'https://money.yahoo.com/arcade-1-up-sales-surge-during-coronavirus-pandemic-122020305.html',
        'https://www.opendemocracy.net/en/opendemocracyuk/boris-johnson-made-politics-awful-then-asked-people-vote-it-away/',
        'https://www.nydailynews.com/sports/basketball/nets/bondy-prokhorov-absence-adding-nets-confusion-article-1.1565134',
        'https://www.middleeastmonitor.com/20200422-global-coronavirus-cases-exceed-2-6m/',
        'https://www.orlandosentinel.com/entertainment/os-halloween-horror-nights-alice-cooper-haunted-house-20120724-story.html',
        'https://www.orlandosentinel.com/opinion/os-ed-letters-012617-20170126-story.html',
        'https://www.theguardian.com/news/2017/apr/26/tulum-mexico-hotel-evictions-instagram-favourite-beach',
        'https://www.chicagotribune.com/nation-world/ct-donald-trump-campaign-promises-20160122-story.html',
        'https://www.arabnews.com/node/1650971/lifestyle\nhttps://globalnation.inquirer.net/40411/china-lauds-ph-pullout-from-shoal',
        'https://www.middleeastmonitor.com/20171026-egypt-population-jumps-16m-people-after-2011-revolution/',
        'https://www.yahoo.com/lifestyle/beauty-blogger-shares-struggle-with-acne-we-fall-in-love-with-her-honesty-183920392.html',
        'https://www.middleeastmonitor.com/20191024-unicef-over-5000-children-killed-injured-in-yemen-war/',
        'https://www.smh.com.au/national/cash-for-calm-canberra-pays-16m-to-counter-budding-jihadists-20150501-1mxv8w.html'

    ]

    st.write('We are now searching through the urls for the keywords that we identifed and returning the new value within the dictionary of the count of how many times these words appeared within the articles.')

    for url in list_of_urls:
        text = requests.get(url).text
        for k, _ in x.items():
            x[k] += text.count(k)
    st.write(x)

    st.write('We know turn this dictionary into a dataframe to graph it, and see the occurence of the words.')
    occurence = pd.DataFrame(list(x.items()), columns=[
                             'Common Words', 'Count'])

    st.write(occurence)

    st.write('## Exploratory Data Analysis:')

    with sns.axes_style("white"):
        plt.style.use('fivethirtyeight')
        fig, ax = plt.subplots(figsize=(20, 10))
        color = ("yellow", "red", "purple", "cadetblue", "darksalmon",
                 "thistle", "aqua", "bisque", "plum", "lightcoral", "coral", "tomato")
        occurence.groupby('Common Words')['Count'].sum().plot(
            kind='bar', color=color)
        ax.set_title(
            "Common Words in Newspapers Throughout Quarantine", size=24)
        ax.set_xlabel('Common Words', size=30)
        ax.set_ylabel('Count', size=30)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
    st.pyplot()

    st.write('## Analyzing the News Articles Within the Last 4 Months')

    st.write('We are going to repeat the steps of the first couple searches to compare within the last quarter of the year,how much hate words have associated with Hate Crime.')

    googled = GoogleNews()
    location = googled.geo_headlines('New York City')
    searches = googled.search('Anti-Asian Hate Crimes', when='4m')
    st.write(searches)

    st.write(searches['entries'])

    results = " "
    for entry in searches['entries']:
        results += entry['title'] + '\n'
    st.write(str(results))

    links_2 = ""
    for entry in search['entries']:
        links_2 += entry['link'] + '\n'
    st.write(str(links_2))

    st.write(
        'We are comparing this amongst the same words that we identified within the last 16 months')
    y = {
        'shooting': 0,
        'assault': 0,
        'attack': 0,
        'death': 0,
        'fight': 0,
        'killed': 0,
        'hate': 0,
        'rape': 0,
        'harmed': 0,
        'harm': 0,
        'violence': 0,
        'violent': 0,
        'hate': 0
    }
    list_of_words = ['shooting', 'assault', 'attack', 'death', 'fight',
                     'killed', 'hate', 'rape', 'harmed', 'harm', 'violence', 'violent', 'hate']

    y = {
        i: 0 for i in list_of_words
    }
    st.write(y)

    list_of_urls = [
        'https://www.boston25news.com/news/health/community-leaders-hold-forum-anti-asian-racism/RMU73KFI6VETJCMH2X6ZOZEEJE/',
        'https://www.cbs58.com/news/more-assaults-on-asian-american-women-reported-in-san-francisco-baltimore-and-new-york',
        'https://finance.yahoo.com/news/nfl-player-taylor-rapp-launching-200854041.html',
        'https://www.crfashionbook.com/beauty/a36202945/14-asian-owned-beauty-brands-to-support/',
        'https://www.daytondailynews.com/local/locals-call-to-end-hate-against-asian-americans/QFXUYEPGTRAS5GU473ZOERPUF4/',
        'https://www.daytondailynews.com/local/greene-county-activists-plan-one-year-memorial-event-for-george-floyd/D3ASLDPJNZELJHZYXHKASQPM6A/',
        'https://www.bbc.co.uk/news/live/world-us-canada-55629665',
        'https://www.ctvnews.ca/world/un-official-terrorists-using-pandemic-to-stoke-extremism-1.5264528',
        'https://www.hrw.org/news/2016/09/13/hungarys-xenophobic-anti-migrant-campaign',
        'https://finance.yahoo.com/news/vehicle-electrification-market-research-report-183400017.html',
        'https://www.justsecurity.org/70952/just-securitys-new-co-editor-in-chief/',
        'https://www.wect.com/2019/02/22/watch-puppy-cries-over-sad-lion-king-scene/',
        'https://www.bbc.com/news/world-us-canada-39732845',
        'https://www.independent.co.uk/news/world/americas/us-politics/trump-china-flu-coronavirus-asian-b1851518.html',
        'https://www.nytimes.com/2019/01/23/sports/lindsey-vonn-wont-retire.html',
        'https://www.ft.com/content/f793f132-96f8-11e7-b83c-9588e51488a0',
        'https://www.sun-sentinel.com/opinion/commentary/fl-op-com-hate-crimes-atlanta-shooting-20210329-fkcohptu2veyvkdpw42xc5jbl4-story.html',
        'https://www.orlandosentinel.com/news/nationworld/ct-aud-nw-nyt-biden-anti-asian-attacks-20210331-aysi4o44hngqnmaouxrrho25nm-story.html',
        'https://news.yahoo.com/man-charged-hate-crimes-kicking-160416510.html',
        'https://news.yahoo.com/entrepreneur-brothers-donate-100-t-203703166.html',
        'https://www.globalcitizen.org/en/content/marvel-introduces-asian-superhero-shang-chi/',
        'https://ph.news.yahoo.com/us-olympian-sakura-kokumai-describes-racist-attack-while-training-at-park-132107093.html',
        'https://news.yahoo.com/asian-american-artist-recorded-racist-133000585.html',
        'https://news.yahoo.com/racist-terrorizes-chinese-familys-children-233828892.html',
        'https://www.mercurynews.com/2021/03/19/tv-tonight-the-falcon-and-the-winter-soldier-blazes-onto-disney',
        'https://thehill.com/changing-america/enrichment/arts-culture/549050-marvel-introduces-asian-superhero-played-by-simu-liu',
        'https://www.pilotonline.com/nation-world/ct-aud-nw-nyt-chinese-grandmother-attacked-san-francisco-20210326-sbuo2ehn65cj7nfyrdg4fv6qme-story.html',
        'https://ph.news.yahoo.com/elderly-fil-am-violently-attacked-011320023.html',
        'https://ph.news.yahoo.com/stock-asian-owned-food-brands-151223463.html',
        'https://www.orlandosentinel.com/news/crime/os-prem-ne-central-florida-capitol-rioters-20210320-t25ecsgoyjddrmxxfgh7eocy2i-story.html',
        'https://money.yahoo.com/gates-opening-simu-liu-having-181059750.html',
        'https://globalnation.inquirer.net/195994/carpio-dutertes-betrayal-of-natl-interest-over-wps-an-impeachable-offense',
        'https://money.yahoo.com/why-costco-may-still-win-140539778.html',
        'https://www.arabnews.com/node/1817731/lifestyle',
        'https://ph.news.yahoo.com/bystander-effect-anti-asian-crime-173833831.html',
        'https://news.yahoo.com/teen-vogue-staffer-supported-mccammond-005806130.html',
        'https://ph.news.yahoo.com/global-tourist-arrivals-down-87-102100559.html',
        'https://ph.news.yahoo.com/lamborghini-kicking-off-electrification-plan-142746906.html',
        'https://www.middleeastmonitor.com/20210404-over-16m-coronavirus-vaccine-doses-administered-in-turkey/',
        'https://floridapolitics.com/archives/421587-sunburn-the-morning-read-of-whats-hot-in-florida-politics-4-20-21/',
        'https://money.yahoo.com/scaramucci-bitcoin-apex-predator-ethereum-014728081.html',
        'https://ph.news.yahoo.com/sidewalk-labs-launches-pebble-sensor-143008442.html',
        'https://ph.news.yahoo.com/jaguar-land-rover-posts-534-m-profit-thanks-to-strong-sales-in-china-141826324.html',
        'https://newsinfo.inquirer.net/1404248/duterte-empower-filipinas-reject-backward-mindset-that-fuels-oppression-inequality',
        'https://newsinfo.inquirer.net/1385895/minimum-wage-earners-decry-high-food-prices',
        'https://ph.news.yahoo.com/tess-holliday-anorexia-001625754.html',
        'https://thehill.com/homenews/senate/551345-romney-booed-during-speech-to-utah-gop-convention',
        'https://ph.news.yahoo.com/pediatrician-reveals-why-ditch-gender-160023718.html',
        'https://newsinfo.inquirer.net/1353031/duterte-orders-govt-agencies-to-observe-transparency-in-procurement-process',
        'https://ph.news.yahoo.com/manila-chooks-tm-heavy-underdogs-235200896.html\nhttps://ph.news.yahoo.com/mlb-angels-releasing-future-hall-of-famer-albert-pujols-175133334.html',
        'https://news.yahoo.com/ohio-republican-lawmakers-propose-renaming-203844996.html',
        'https://money.yahoo.com/coronavirus-stimulus-gop-plan-for-unemployment-benefits-hits-snag-over-mechanical-issues-170027326.html',
        'https://www.arlnow.com/2020/06/20/county-apologizes-for-removing-girls-black-lives-matter-chalk-art/',
        'https://www.nytimes.com/2020/07/30/opinion/the-argument-authoritarianism-anne-applebaum.html',
        'https://news.yahoo.com/interview-britains-first-tiktok-house-164939960.html',
        'https://money.yahoo.com/arcade-1-up-sales-surge-during-coronavirus-pandemic-122020305.html',
        'https://www.opendemocracy.net/en/opendemocracyuk/boris-johnson-made-politics-awful-then-asked-people-vote-it-away/',
        'https://www.nydailynews.com/sports/basketball/nets/bondy-prokhorov-absence-adding-nets-confusion-article-1.1565134',
        'https://www.middleeastmonitor.com/20200422-global-coronavirus-cases-exceed-2-6m/',
        'https://www.orlandosentinel.com/entertainment/os-halloween-horror-nights-alice-cooper-haunted-house-20120724-story.html',
        'https://www.orlandosentinel.com/opinion/os-ed-letters-012617-20170126-story.html',
        'https://www.theguardian.com/news/2017/apr/26/tulum-mexico-hotel-evictions-instagram-favourite-beach',
        'https://www.chicagotribune.com/nation-world/ct-donald-trump-campaign-promises-20160122-story.html',
        'https://www.arabnews.com/node/1650971/lifestyle',
        'https://globalnation.inquirer.net/40411/china-lauds-ph-pullout-from-shoal',
        'https://www.middleeastmonitor.com/20171026-egypt-population-jumps-16m-people-after-2011-revolution/',
        'https://www.yahoo.com/lifestyle/beauty-blogger-shares-struggle-with-acne-we-fall-in-love-with-her-honesty-183920392.html',
        'https://www.middleeastmonitor.com/20191024-unicef-over-5000-children-killed-injured-in-yemen-war/',
        'https://www.smh.com.au/national/cash-for-calm-canberra-pays-16m-to-counter-budding-jihadists-20150501-1mxv8w.html',

    ]

    for url in list_of_urls:
        text = requests.get(url).text
        for k, _ in x.items():
            y[k] += text.count(k)
    st.write(y)

    st.write('Placing the Information into A DataFrame')

    count_of_words = pd.DataFrame(list(y.items()), columns=[
        'Common Words', 'Count'])

    st.write(count_of_words)

    st.write('Graphing the Data')

    with sns.axes_style("white"):
        plt.style.use('fivethirtyeight')
        fig, ax = plt.subplots(figsize=(20, 10))
        color = ("yellow", "red", "purple", "cadetblue", "darksalmon",
                 "thistle", "aqua", "bisque", "plum", "lightcoral", "coral", "tomato")
        count_of_words.groupby('Common Words')[
            'Count'].sum().plot(kind='bar', color=color)
        ax.set_title("Common Words in Newspapers 4 Months of Ago", size=24)
        ax.set_xlabel('Common Words', size=30)
        ax.set_ylabel('Count', size=30)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
    st.pyplot()

    wordclouded = WordCloud().generate(results)

    st.write('Display the generated image:')
    with sns.axes_style("white"):
        plt.imshow(wordclouded, interpolation='bilinear')
        plt.axis("off")
    st.pyplot()

    st.write(
        'We are converting these WordClouds to a png file to integrate into our dashboard')

    wordclouded.to_file('./img/4-Months Ago.png')
    st.image('./img/4-Months Ago.png')

    wordclouded.to_file('16-Months Ago.png')
    st.image('./img/16-Months Ago.png')

    st.write('Now we are comparing the common words in the newspapers within the pandemic, throughout covid-19 and within the last 4 months to see the differences between the last quarter of the year, to analyze how much of an impact it has on the Asian Community')

    with sns.axes_style("white"):
        width = 0.25
        labels = count_of_words["Common Words"]
        x = np.arange(len(labels))
        fig, ax = plt.subplots(figsize=(8, 7))
        ax.bar(x-width/2, occurence["Count"],
               width=width, label='Throughout COVID 19')
        ax.bar(x+width/2, count_of_words["Count"],
               width=width, label='Within the Last 4 Months')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_xlabel('Common Words')
        ax.set_ylabel('Count of Common Words')
        ax.set_title(
            'Comparison of Common Words in Newspapers Within The Pandemic')
        ax.legend()
    st.pyplot()

    st.write('## **Further Analysis and Conclusions:**')
    st.write('### **Analysis:**')

    st.write('Overall within the last couple months, the negative connatation of words within the newspapers have existed in the newspapers.We are able to observe that many of those who are in the Asian community were attacked and harmed and hated on. However, many few were raped. Considering that majority of articles are written in the present tense,we can assume this is why there is a low percentage in the word harmed. We do note that the occurence of the words harm,violence, violent,assault, fight, and shootingall increased by a little bit. The largest difference we see is in the words fight. Meaning that the amount of accidents that many got into were at a greater scale.')

    st.write('### **Was Our Hypothesis Right?**')

    st.write('Our Hypothesis is right, but further analysis has to be done to create a comparison in how this impacted buisness traffic. The amount of negative words did increase therefore showing that there was a larger perspective of Asian crime, therefore showing that many hate crimes are not being reported. This also allows us to show that Asian Americans are still being impacted by this crime.')

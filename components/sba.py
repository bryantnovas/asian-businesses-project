import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io 

sns.set()
def app():
  st.markdown(
  '''
    # **Introduction**:
    What is the SBA Loan? 
    an SBA loan is a small business loan that is partially guaranteed by the government (the Small Business Administration), which eliminates some of the risk for the financial institution who is issuing the loan.
    SBA loans can range in size anywhere from $500 to $5.5 million and can offer APR’s as low as 6.5%. Additionally, repayment terms for SBA loans can range from 5 to 25 years, but 10 years is a standard SBA loan repayment term length.
    This notebook will be analyzing the data from the website below regarding SBA loans in New York.
    [click here](https://web.sba.gov/dsbs/search/dsp_dsbs.cfm)
    # **Hypothesis**:
    My hypothesis is that financial resources such as the SBA loan are not being distributed to the small businesses in the communities that need the assistance the most.
    The data in this notebook will show the how many businesses recieve financial assistance through SBA loans by borough.
  ''')

  pd.set_option('display.max_columns', None)
  df = pd.read_csv('./datasets/SBA_dataset.csv')


  st.dataframe(df.head(3))

  st.write('# **Analysis on our data:**')

  d1 = df['City'] = df['City'].str.lower()
  st.dataframe(d1)



  st.write('# The average year established for these businesses is 2011')
  st.write(df['Year Established'].mean())

  Queens = ['arverne', 'astoria', 'bayside', 'bellerose', 'breezy point', 'cambria heights',
            'college point', 'corona east', 'elmhurst', 'elmhurst', 'far rockaway', 'floral park', 'flushing',
            'forest hills', 'fresh meadows', 'glen oaks', 'hollis', 'howard beach', 'jackson heights', 'jamaica', 'kew gardens',
            'little neck', 'long island city', 'maspeth', 'middle village', 'oakland gardens', 'ozone park', 'queens village', 'rego park',
            'richmond hill', 'ridgewood', 'rockaway park', 'rosedale', 'saint albans', 'south ozone park', 'south richmond hill', 'springfield gardens', 'sunnyside', 'whitestone', 'woodhaven', 'woodside']
 
  df.loc[(df.City.isin(Queens)),'City']='queens'



  Bronx = ['allerton', 'baychester', 'bedford park', 'belmont', 'castle hill', 'city island', 
  'clason point', 'co-op city', 'eastchester', 'edenwald', 'fordham', 'highbridge', 'hunts point', 'kingsbridge', 'longwood', 'marble hill',
  'melrose', 'morris heights', 'morris park', 'morrisania', 'mott haven', 'mount hope', 'norwood', 'parkchester', 'pelham bay', 'riverdale', 'soundview', 'the hub', 'throgs neck', 'tremont', 'university heights', 'wakefield', 'west farms', 'westchester', 'williamsbridge', 'woodlawn']

  df.loc[(df.City.isin(Bronx)),'City']='bronx'



  Staten_Island = ['annadale', 'arden heights', 'arlington', 'arrochar', 'bay terrace', 
  'bloomfield', 'brighton heights', 'bulls head', 'castleton', 'castleton corners', 'charleston', 'chelsea', 'clifton', 'concord', 
  'dongan hills', 'egbertville', 'elm park', 'eltingville', 'emerson hill', 'fort wadsworth', 'graniteville', 'grant city', 'grasmere', 'great kills', 'greenridge', 'grymes hill', 'hamilton park', 'heartland village', 'huguenot', 'lighthouse hill', 'livingston', 'manor heights', 'mariners harbor', 'meiers corners', 'midland beach', 'new brighton', 'new dorp', 'new springville', 'oakwood', 'ocean breeze', 'old place', 'old town', 'pleasant plains', 'port richmond', 'prince’s bay', 'randall manor', 'richmond valley', 'richmondtown', 'rosebank', 'rossville', 'sandy ground', 'shore acres', 'silver lake', 'south beach', 'st.george', 'stapleton', 'stapleton heights', 'sunnyside', 'todt hill', 'tompkinsville']
  
  df.loc[(df.City.isin(Staten_Island)),'City'] = 'staten island'

  Manhattan = '''
  Alphabet City
  Astor Row
  Battery Park City
  Bowery
  Carnegie Hill
  Chelsea
  Chinatown
  Civic Center
  Columbus Circle
  Cooperative Village
  Diamond District
  Downtown Manhattan
  East Harlem
  East Village
  Financial District
  Five Points
  Flatiron District
  Fort George
  Garment District
  Gramercy Park
  Greenwich Village
  Hamilton Heights
  Hell’s Kitchen
  Herald Square
  Hudson Yards
  Inwood
  Kips Bay
  Koreatown
  Lenox Hill
  Lincoln Square
  Little Germany
  Little Italy
  Lower East Side
  Madison Square
  Manhattan Valley
  Marble Hill
  Marcus Garvey Park
  Meatpacking District
  Midtown
  Morningside Heights
  Murray Hill
  NoHo
  Nolita
  NoMad
  Battery Park City
  Radio Row
  Rockefeller Center
  Rose Hilll
  SoHo
  South Street Seaport
  Strivers’ Row
  Stuyvesant Square
  Stuyvesant Town
  Sugar Hill
  Sutton Place
  Tenderloin
  Theater District
  Times Square
  Tribeca
  Tudor City
  Turtle Bay
  Two Bridges
  Union Square
  Upper East Side
  Upper West Side
  Washington Heights
  Waterside Plaza
  West Village
  Yorkville
  '''
  Manhattan_list = Manhattan.lower().split()
  df.loc[(df.City.isin(Manhattan_list)),'City']='manhattan'

  Brooklyn = ['admirals row', 'atura', 'barren island', 'bath beach', 'bay ridge', 'bedford', 'bedford-stuyvesant', 'bensonhurst',
  'bergen beach', 'bococa', 'boerum hill', 'borough park', 'brighton beach', 'brooklyn heights', 'brownsville', 'bushwick', 'cadman plaza',
  'canarsie', 'carroll gardens', 'city line', 'clinton hill', 'cobble hill', 'coney island', 'crown heights', 'cypress hills', 'ditmas park', 
  'downtown dumbo', 'dyker heights', 'east flatbush', 'east new york', 'east williamsburg', 'farragut', 'fiske terrace', 'flatbush', 'flatlands', 'fort greene', 'fort hamilton', 'fulton ferry', 'georgetown', 'gerritsen beach', 'gowanus', 'gravesend', 'greenpoint', 'greenwood heights', 'highland park', 'homecrest', 'kensington', 'little poland', 'madison,', 'manhattan beach', 'marine park', 'midwood', 'mill basin', 'navy yard', 'new lots', 'new utrecht', 'ocean hill', 'ocean parkway', 'park slope', 'pigtown', 'plum beach', 'prospect heights', 'prospect park', 'south prospect', 'lefferts gardens', 'rambo', 'red hook', 'sea gate', 'sheepshead bay', 'south brooklyn', 'south park slope', 'starrett city', 'stuyvesant heights', 'sunset park', 'vinegar hill', 'weeksville', 'white sands', 'williamsburg', 'windsor terrace', 'wingate']

  df.loc[(df.City.isin(Brooklyn)),'City'] = 'brooklyn'

  df.loc[(~df.City.isin(['brooklyn','bronx','queens','staten island',"manhattan"])),'City'] = 'other'

  st.dataframe(df)



  newdf = df[df.City.isin(["bronx", "brooklyn","queens","manhattan","staten island", "other"])]

  buffer = io.StringIO() 
  df.info(buf=buffer, verbose=True)
  s = buffer.getvalue() 
  with open("./sba_info.txt", "w", encoding="utf-8") as f:
      f.write(s)
      st.write(s) 
  data = newdf.groupby("City")['City'].count()

  st.write(data)

  with sns.axes_style("white"):
    pie, ax = plt.subplots(figsize=[10,6])
    labels = data.keys()
    plt.pie(x=data, autopct="%.1f%%", labels=labels, pctdistance=0.5)
    plt.title(" Percentage of Businesses W/ SBA loans by City", fontsize=14);
  st.pyplot()

  st.write('''
    # Conclusion:
    from this pie chart you can see a majority of the SBA loans went to cities in New York that are outside of the 5 boroughs. Therefore from this data I would say more resources should be allocated to small businesses within boroughs such as The Bronx which has only 5 percent 
  ''')
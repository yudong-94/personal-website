<head>
  <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-112502179-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-112502179-1');
</script>
</head>


## Data Visualization -- Makeover Monday 20210412

### About Makeover Monday

[MakeoverMonday](http://www.makeovermonday.co.uk/) is a social data project:
"Each week we post a link to a chart, and its data, and then you rework the chart.
Maybe you retell the story more effectively, or find a new story in the data.
We’re curious to see the different approaches you all take. Whether it’s a simple bar chart or an elaborate infographic, we encourage everyone of all skills to partake.
Together we can have broader conversations about and with data."

Starting from Jan 08, 2018, I decided to put aside one hour on Monday weekly to create some visualization and find some insights from the data.

The datasets are published each week at: [MakeoverMonday Datasets](http://www.makeovermonday.co.uk/data/).

### Makeover Monday 20210412

This week's dataset is about fouls called games by NBA referee. Well, honestly I have no idea what fouls are in basketball lol (I feel it has been a while since last sport-themed dataset). The original viz is from a [Twitter](https://twitter.com/owenlhjphillips/status/1336681714366689280).  

#### My Visualization

I actually like the way the origial viz did it, as it normalized the fouls by game, and show the distribution, highlighted the selected referee. So I essentially remade the viz with my own style.  

--  
<div class='tableauPlaceholder' id='viz1618287053369' style='position: relative'>
<noscript><a href='#'>
  <img alt='Fouls Called by NBA Referees ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MakeOverMonday20210412FoulsCalledByNBAReferees&#47;FoulsCalledbyNBAReferees&#47;1_rss.png' style='border: none' />
</a></noscript>
<object class='tableauViz'  style='display:none;'>
  <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
  <param name='embed_code_version' value='3' /> 
  <param name='site_root' value='' />
  <param name='name' value='MakeOverMonday20210412FoulsCalledByNBAReferees&#47;FoulsCalledbyNBAReferees' />
  <param name='tabs' value='no' />
  <param name='toolbar' value='yes' />
  <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MakeOverMonday20210412FoulsCalledByNBAReferees&#47;FoulsCalledbyNBAReferees&#47;1.png' />
  <param name='animate_transition' value='yes' />
  <param name='display_static_image' value='yes' />
  <param name='display_spinner' value='yes' />
  <param name='display_overlay' value='yes' />
  <param name='display_count' value='yes' />
  <param name='language' value='en' />
  <param name='filter' value='publish=yes' />
</object></div>             
<script type='text/javascript'>       
  var divElement = document.getElementById('viz1618287053369');    
  var vizElement = divElement.getElementsByTagName('object')[0];     
  if ( divElement.offsetWidth > 800 ) { vizElement.style.width='600px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='600px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}    
  var scriptElement = document.createElement('script');            
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';         
  vizElement.parentNode.insertBefore(scriptElement, vizElement);            
</script>

--  

[Dashboard link](https://public.tableau.com/views/MakeOverMonday20210412FoulsCalledByNBAReferees/FoulsCalledbyNBAReferees?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)

#### Insights
* By checking some outliers, we can find some referees with interesting behaviors -- for example, in season 2019-20 regular season, Though referee Bennie Adams showed overall average total fouls, he actually did the highest number of Offensive Charge, Loose Ball, Defensive Goaltending, and Defensive 3 seconds types of fouls per game among all referees.  

--  
[⬅️Previous](https://yudong-94.github.io/personal-website/projects/data viz/MakeOverMonday20210405)  

[Back to Home Page](https://yudong-94.github.io/personal-website/)

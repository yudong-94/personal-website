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


## Data Visualization -- Makeover Monday 20210322

### About Makeover Monday

[MakeoverMonday](http://www.makeovermonday.co.uk/) is a social data project:
"Each week we post a link to a chart, and its data, and then you rework the chart.
Maybe you retell the story more effectively, or find a new story in the data.
We’re curious to see the different approaches you all take. Whether it’s a simple bar chart or an elaborate infographic, we encourage everyone of all skills to partake.
Together we can have broader conversations about and with data."

Starting from Jan 08, 2018, I decided to put aside one hour on Monday weekly to create some visualization and find some insights from the data.

The datasets are published each week at: [MakeoverMonday Datasets](http://www.makeovermonday.co.uk/data/).

### Makeover Monday 20210322

This week's topic is US monthly personal consumption expenditure. It's really interesting to see how COVID has impact people's expense on food. [The original article](https://www.bloomberg.com/opinion/articles/2021-02-24/beyond-grape-nuts-cereal-makers-had-a-very-weird-year) specifically talks about cereal expense, but the datasets contain the data for many other categories.  

#### My Visualization

I made some rose-shape chart to visualize the YoY expenditure change % with the color representing time (deeper as more recent).  

--  
<div class='tableauPlaceholder' id='viz1616476148570' style='position: relative'>
<noscript><a href='#'>
  <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MakeOverMonday20210322YoYMonthlyPersonalConsumptionExpenditures&#47;YoYMonthlyPersonalConsumptionExpenditures&#47;1_rss.png' style='border: none' />
</a></noscript>
<object class='tableauViz'  style='display:none;'>
  <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
  <param name='embed_code_version' value='3' />
  <param name='site_root' value='' />
  <param name='name' value='MakeOverMonday20210322YoYMonthlyPersonalConsumptionExpenditures&#47;YoYMonthlyPersonalConsumptionExpenditures' />
  <param name='tabs' value='no' />
  <param name='toolbar' value='yes' />
  <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MakeOverMonday20210322YoYMonthlyPersonalConsumptionExpenditures&#47;YoYMonthlyPersonalConsumptionExpenditures&#47;1.png' />
  <param name='animate_transition' value='yes' />
  <param name='display_static_image' value='yes' />
  <param name='display_spinner' value='yes' />
  <param name='display_overlay' value='yes' />
  <param name='display_count' value='yes' />
  <param name='language' value='en' />
  <param name='filter' value='publish=yes' />
</object></div>             
<script type='text/javascript'>       
  var divElement = document.getElementById('viz1616476148570');     
  var vizElement = divElement.getElementsByTagName('object')[0];                
  if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}               
  var scriptElement = document.createElement('script');       
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';     
  vizElement.parentNode.insertBefore(scriptElement, vizElement);             
</script>

--  

[Dashboard link](https://public.tableau.com/views/MakeOverMonday20210322YoYMonthlyPersonalConsumptionExpenditures/YoYMonthlyPersonalConsumptionExpenditures?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)

#### Insights
* For cereal category, there is a 25% YOY increase in personal expenditure in March 2021 -- the last time we see a 20% increase was in 1974 (maybe due to the Oil Crisis?);  
* Similar pattern can be seen in other categories -- a significant (and most of the time, historically high) YoY increase is seen in March 2021, then things flatten out but YoY increase still much higher than normal years.  
  
--  
[⬅️Previous](https://yudong-94.github.io/personal-website/projects/data viz/MakeOverMonday20210315)  [➡️Next](https://yudong-94.github.io/personal-website/projects/data viz/MakeOverMonday20210329)  

[Back to Home Page](https://yudong-94.github.io/personal-website/)

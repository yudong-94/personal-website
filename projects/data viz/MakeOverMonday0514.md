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


## Data Visualization -- Makeover Monday 0514

### About Makeover Monday

[MakeoverMonday](http://www.makeovermonday.co.uk/) is a social data project:
"Each week we post a link to a chart, and its data, and then you rework the chart.
Maybe you retell the story more effectively, or find a new story in the data.
We’re curious to see the different approaches you all take. Whether it’s a simple bar chart or an elaborate infographic, we encourage everyone of all skills to partake.
Together we can have broader conversations about and with data."

Starting from Jan 08, 2018, I decided to put aside one hour on Monday weekly to create some visualization and find some insights from the data.

The datasets are published each week at: [MakeoverMonday Datasets](http://www.makeovermonday.co.uk/data/).

### Makeover Monday 0514

This week's topic is traffic jam in Europe - the top 10 cities that commuters spent most time in traffic jam in 2017. You can find the original viz [here](http://www.euronews.com/2018/02/07/which-european-commuters-spend-the-most-time-in-traffic-jams-).
But as the data is just 10 rows with 10 cities and their average commuting time, this viz is essentially a simple bar chart.  


#### My Visualization

For this dashboard, I spent only around 30 minutes, as the data is rather straightforward. 
I marked the top 10 cities in map, and for the first time, used annotation in the dashboard.  
Below is my dashboard.  

--  
<div class='tableauPlaceholder' id='viz1526346194340' style='position: relative'>
<noscript><a href='#'>
  <img alt='traffic jam in EU ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;46&#47;46MGDBD3T&#47;1_rss.png' style='border: none' />
</a></noscript>
<object class='tableauViz'  style='display:none;'>
  <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
  <param name='embed_code_version' value='3' /> 
  <param name='path' value='shared&#47;46MGDBD3T' />
  <param name='toolbar' value='yes' />
  <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;46&#47;46MGDBD3T&#47;1.png' />
  <param name='animate_transition' value='yes' />
  <param name='display_static_image' value='yes' />
  <param name='display_spinner' value='yes' />
  <param name='display_overlay' value='yes' />
  <param name='display_count' value='yes' />
</object></div>               
<script type='text/javascript'>        
  var divElement = document.getElementById('viz1526346194340');           
  var vizElement = divElement.getElementsByTagName('object')[0];           
  vizElement.style.width='800px';vizElement.style.height='827px';        
  var scriptElement = document.createElement('script');              
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';       
  vizElement.parentNode.insertBefore(scriptElement, vizElement);           
</script>  

--  

#### Insights 
* London is definitely the most busy city regarding commuting time, but to my surprise, we have four cities from Germany in the top 10 list, and also two from Switzerland.  
* It is said that overall, commuters in Los Angeles spent the most time stuck in traffic out of the 1,360 global cities included, at 102 hours... I know the pain :(  
  
--  


<a href="https://yudong-94.github.io/personal-website/" title="Back to Home Page">Back to Home Page</a>
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


## Data Visualization -- Makeover Monday 0305

### About Makeover Monday

[MakeoverMonday](http://www.makeovermonday.co.uk/) is a social data project:
"Each week we post a link to a chart, and its data, and then you rework the chart.
Maybe you retell the story more effectively, or find a new story in the data.
We’re curious to see the different approaches you all take. Whether it’s a simple bar chart or an elaborate infographic, we encourage everyone of all skills to partake.
Together we can have broader conversations about and with data."

Starting from Jan 08, 2018, I decided to put aside one hour on Monday weekly to create some visualization and find some insights from the data.

The datasets are published each week at: [MakeoverMonday Datasets](http://www.makeovermonday.co.uk/data/).

### Makeover Monday 0305

This week's data is about a survey on gender equality measurements to the policymakers in five countries (Colombia, India, Indonesia, Kenya, and Senegal). 
This survey asked the policymakers whether they knew about four measurements of gender equality - rate marriage rate for women, share of seats held by women in the parliament, share of women in the labour force, maternal mortality, and secondary education.
And what are their estimates on each measures.
I do find this data very interesting as a female, and as the International Women's Day is coming :)  
The original visualizations and reports could be found [here](http://www.equalmeasures2030.org/products/policymaker-report/).


#### My Visualization

I spent about an hour and a half to make dashboards to answer three questions from the survey data:  
1. How many policymakers think they know each measurement  
2. How good are their estimates to these measurements
3. Do the policymakers said 'I know the answer' really know the answer?  
Below is my dashboard. You can select the measurement/topic on upper right, and hover on each bar and points to get detailed info.

--  
<div class='tableauPlaceholder' id='viz1520310916887' style='position: relative'>
<noscript><a href='#'>
  <img alt='Gender Equality Measures Awareness ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;QQ&#47;QQT3WZRF5&#47;1_rss.png' style='border: none' />
</a></noscript>
<object class='tableauViz'  style='display:none;'>
  <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
  <param name='embed_code_version' value='3' /> 
  <param name='path' value='shared&#47;QQT3WZRF5' />
  <param name='toolbar' value='yes' />
  <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;QQ&#47;QQT3WZRF5&#47;1.png' />
  <param name='animate_transition' value='yes' />
  <param name='display_static_image' value='yes' />
  <param name='display_spinner' value='yes' />
  <param name='display_overlay' value='yes' />
  <param name='display_count' value='yes' />
  <param name='filter' value='publish=yes' />
</object></div>                
<script type='text/javascript'>                    
  var divElement = document.getElementById('viz1520310916887');            
  var vizElement = divElement.getElementsByTagName('object')[0];            
  vizElement.style.width='800px';vizElement.style.height='827px';           
  var scriptElement = document.createElement('script');                
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';        
  vizElement.parentNode.insertBefore(scriptElement, vizElement);               
</script>  
--  

#### Insights 
* Generally speaking, policymakers interviewed in Senegal are the least willing to make an estimates on the measurements, while those in Colombia are the most willing to. Of course, as the sample size is small, this might not be the real case regarding the whole population;    
* In most cases, policymakers in Indonesia are the most confident - the percentage of policymakers stated that they knew the answer is the highest for Indonesia;  
* Among all the measurements, 'share seats held by women' is the one estimated most accurately in all countries - as policymakers, the respondents are definitely more familiar with this measurement;  
* The most extreme estimate deviation case happened for estimating 'maternal mortality rate for women' by Kenya policymakers - there is an estimate deviated by over 1800% (the estimate is not even a reasonable number as a rate);  
* Policymakers stating 'I know the answer' not necessarily make a better estimate than those stating 'Not sure but can find'. They were just stating so...  

--  
<a href="https://yudong-94.github.io/personal-website/" title="Back to Home Page">Back to Home Page</a>

---
title: "From Web Pages to Insights: Integrating Web Scraping and Text Analysis with GPT"
date: 2024-06-02
categories:
  - blog
tags:
  - llm
  - data science
  - analysis
  - nlp
  - web scraping
  - data visualization summary
  - coding
header:
  teaser: /assets/images/article_covers/viz_summary_with_gpt_cover.jpg
excerpt: "Use GPT to summarise content and extract structured data from web pages."
---

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    img {
        margin: 10px;
        max-width: 100%;
        height: auto;
    }
</style>

#### Use GPT to summarise content and extract structured data from web pages

In [a past article](https://yudong-94.github.io/personal-website/blog/TextAnalyticsWithGPT/), I explored how to summarize and categorize text using the OpenAI API. In this post, I will take it one step further and show you how to integrate web scraping into this workflow to extract structured data info from a series of web pages.

### Context

I have been making [one visualization weekly](https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz2024/) since I started my full-time DS job in 2018. Initially, I followed the datasets posted every week by [makeovermonday.co.uk](http://makeovermonday.co.uk). However, they paused the project in September 2021 for about one year. Running this community every week is a huge commitment so I completely understand the need for a break. As a result, starting in October 2021, I have been finding my datasets to visualize every week. The topics are mostly inspired by my interests or experience. It has been 139 visualizations since then, so sometimes I wonder what my favorite data topics and visualization types are.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_tableau_screenshot.png" alt="My Weekly Visualizations" width="600" height="400">
</div>

While I have [visualization catalog pages](https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz2024/) with a running list of visualization titles and data sources, it doesn't tell the visualization topic details and the specific chart types I used. Instead, I need to read through the 139 weekly visualization [posts](https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz20240527/) to identify them, which is not realistic. Therefore, it's time to get help from web scraping and the OpenAI API.

### Step I - Prepare the URL Lists

To get the list of URLs to those visualization posts, it is easiest to scrap the list from my [visualization catalog pages](https://yudong-94.github.io/personal-website/tags/#data-visualization-summary). Let’s start with the [2024 page](https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz2024/). By inspecting the HTML code, you can see the URLs are embedded in the 'table' tags within the 'page__content' class.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_viz_catalog_html.png" alt="Visualization Catalog Pages HTML" width="600" height="400">
</div>

With the help of GPT, I wrote the code below to fetch the URL and the post title using the BeautifulSoup package.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_post_url_example.png" alt="Code to extract blog URL" width="600" height="400">
</div>

Now that we have success with the 2024 visualization catalog page, let’s loop through the pages from 2021 to 2024 to get the full list.

```python
years = ['2021', '2022', '2023','2024']
url = 'https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz'
viz_urls = []
viz_titles = []

for y in years:
    year_url = url+y
    # example URL: https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz2024/

    # Send a request to fetch the content of the web page
    response = requests.get(year_url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the HTML content of the web page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the a tags
    viz_table = soup.find('section', class_='page__content').find('table')
    a_tags = viz_table.find_all('a')

    for t in a_tags:
        href = t.get('href')
        text = t.get_text()
        # filter on tags with blog links
        if href:
            # only keep the ones following the WeeklyViz URL format
            if 'https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz' in href:
                viz_urls.append(href)
                viz_titles.append(text)
```

### Step II - Parse Visualization Blog Content

The next step is to parse out the text body from each visualization blog ([example](https://yudong-94.github.io/personal-website/data%20viz/WeeklyViz20240527/)) so we can feed them to the OpenAI API.

My visualization blogs are written in markdown and the site is published via [GitHub Pages](https://pages.github.com/). Therefore, it might look slightly different from many other websites. In this case, the body text can be found under the 'p' tag in the 'page__content' class. Here is a similar code block to extract the text.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_blog_text_code.png" alt="Code to extract blog content" width="600" height="400">
</div>

### Step III - Text Summarization and Categorization with the OpenAI API

In the above steps, we have prepared the URL list and the code snippet to extract the text content. Now it’s time to ask GPT to conduct some text analysis. We have three objectives:
1. **Summarise the visualization topic**, for example, "Top-rated mobile games by genre". This should usually align with the post title.
2. **Categorize the topics category**, for example, "Entertainment". I prepared a list of predefined categories for GPT to choose from. The list could be created based on your domain knowledge, or you can ask GPT to generate a list as described in the [last post](https://yudong-94.github.io/personal-website/blog/TextAnalyticsWithGPT/).
3. **Extract the visualization type**, for example, "Line chart". This is usually described in the 2nd paragraph of my weekly visualization post. I also prepared a predefined list for this one so GPT doesn’t give me values in slightly different formats (hopefully).

To achieve these goals, the key part is to write the prompt. Here is the final prompt after rounds of iteration. For example, I tried to omit the category descriptions, but it outputted lots of ‘Others’. So one takeaway is always to be specific and detailed if possible.

```python
prompt = f"""
    Below is the text content of my weekly visualization blog post. I describes visualization data source, visualization types, and insights in the post.  
    '''
    {blog_content}
    '''
    Please extract the "visualization topic", "topic category", "visualization type" from the blog post.  

    1. "visualization topic": the topic of the visualizations.

    2. "topic category": the category of the visualization topic. It should be one of the below values:  
    - "Economics": topics related to inflation rates, stock market performance, and housing market trends, etc.
    - "Technology": topics related to AI, cybersecurity, and different softwares, etc.
    - "Education": topics related to schools, online courses, and graduation, etc.
    - "Health": topics related to healthcare trends, medical science, and diseases, etc.
    - "Environment": topics related to temperature, natural disasters, global warming, etc.
    - "Travel": topics related to vacation destinations, and tourism statistics, etc.
    - "Business": topics related to startups, IPO, layoffs, and work habits, etc.
    - "Entertainment": topics related to movie, music, gaming, and social media trends, etc.
    - "Social Issues": topics related to gender equality, racial disparities, and crime rates, etc.
    - "Others": other topics that do not fall under any of the above categories.

    3. "visualization type": the type of the visualization.

    The output MUST follow the JSON format as shown in the example below.

    Example:
    '''
    {"visualization_topic":"Unemployment Rate 2000-2024",
     "topic_category":"Economics",
     "visualization_type":"Line chart"}
    '''
"""
```

I also used the [function calling](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models) capability for consistent JSON output. The code below specifies function arguments. This helps to enforce GPT output to always follow your desired JSON format and reduce data pipeline errors.

```python
func = [
    {
        "name": "extract_visualization_info",
        "description": "Extract visualization information",
        "parameters": {
            "type": "object",
            "properties": {
                "visualization_topic": {
                    "type": "string",
                    "description": "The topic of the visualization",
                },
                "topic_category": {
                    "type": "string",
                    "enum": [
                        "Economics",
                        "Technology",
                        "Education",
                        "Health",
                        "Environment",
                        "Travel",
                        "Business",
                        "Entertainment",
                        "Social Issues",
                        "Others"
                    ],
                    "description": "The category of the visualization topic",
                },
                "visualization_type": {
                    "type": "string",
                    "enum": [
                        "Line chart",
                        "Bar chart",
                        "Scatter chart",
                        "Bubble chart",
                        "Gantt chart",
                        "Bump chart",
                        "Heatmap",
                        "Radial chart",
                        "Map",
                        "Others"
                    ],
                    "description": "The type of the visualization",
                },
            },
            "required": ["visualization_topic", "topic_category", "visualization_type"],
        },
    },
]
```

Now let’s piece together the code -- loop through the blog URLs, extract the three pieces of information, and store them in a data frame. I am using the gpt-3.5-turbo model here for cost reasons, but it is sufficient in this use case.

```python
def extract_info(blog_content, model="gpt-3.5-turbo"):
    ## main function to feed the blog content to the OpenAI API
    ## and extract visualization_topic, topic_category, and visualization_type

    prompt = f"""
    Below is the text content of my weekly visualization blog post. I describes visualization data source, visualization types, and insights in the post.  
    '''
    {blog_content}
    '''
    Please extract the "visualization topic", "topic category", "visualization type" from the blog post.  

    1. "visualization topic": the topic of the visualizations.

    2. "topic category": the category of the visualization topic. It should be one of the below values:  
    - "Economics": topics related to inflation rates, stock market performance, and housing market trends, etc.
    - "Technology": topics related to AI, cybersecurity, and different softwares, etc.
    - "Education": topics related to schools, online courses, and graduation, etc.
    - "Health": topics related to healthcare trends, medical science, and diseases, etc.
    - "Environment": topics related to temperature, natural disasters, global warming, etc.
    - "Travel": topics related to vacation destinations, and tourism statistics, etc.
    - "Business": topics related to startups, IPO, layoffs, and work habits, etc.
    - "Entertainment": topics related to movie, music, gaming, and social media trends, etc.
    - "Social Issues": topics related to gender equality, racial disparities, and crime rates, etc.
    - "Others": other topics that do not fall under any of the above categories.

    3. "visualization type": the type of the visualization.

    The output MUST follow the JSON format as shown in the example below.

    Example:
    '''
    {{"visualization_topic":"Unemployment Rate 2000-2024",
     "topic_category":"Economics",
     "visualization_type":"Line chart"}}
    '''
    """

    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        tools=[{"type":"function", "function":func[0]}], #function calling
        response_format={"type":"json_object"} #force JSON output
    )

    func_response = response.choices[0].message.tool_calls[0].function.arguments
    func_arguments = json.loads(func_response)

    return func_arguments

## loop through the URL lists and store the OpenAI responses
## you should add some error handling logic in a production data pipeline
viz_summary = []

for i in range(len(viz_urls)):
    title = viz_titles[i]
    url = viz_urls[i]
    viz_date = url[-8:]

    # Send a request to fetch the content of the web page
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the HTML content of the web page
    soup = BeautifulSoup(response.text, 'html.parser')
    html_body = soup.find('section', class_='page__content')

    # Get p tags for blog body text
    p_tags = html_body.find_all('p')

    # Concatenate the blog text
    blog_text = '**' + title + '**:'
    for t in p_tags:
        blog_text += t.get_text()

    # add other fields
    viz_classification = extract_info(blog_text)
    viz_classification['id'] = i
    viz_classification['date'] = viz_date
    viz_classification['url'] = url
    viz_classification['title'] = title

    viz_summary.append(viz_classification)

viz_summary_df = pd.DataFrame(viz_summary)
```

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_output_df_screenshot.png" alt="Visualization Summary Dataframe" width="600" height="400">
</div>

It’s also necessary to do a quick data validation on the output. As observed in the [last post](https://yudong-94.github.io/personal-website/blog/TextAnalyticsWithGPT/), there are always cases where GPT outputted values are not in the predefined value lists. For example, here it created a new category ‘Society’, which overlaps with the ‘Social Issues’ value I provided -- well, maybe ‘Society’ is a better name… I ended up making some manual adjustments myself to overwrite those outlier values.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_category_output_count.png" alt="Counts of GPT Generated Visualization Topic Categories" width="600" height="400">
</div>

### Visualization Habit Analysis

Now let’s go back to my visualization habit questions. I shared the cleaned dataset in a CSV file with ChatGPT 4o and it did the analysis and created visualizations automatically for me. I like how it captured the main questions and the table structure accurately. It can make basic charts quickly, but not always in the best way. For example, the two trends over time charts are too messy and hardly readable. Therefore, I had to provide guidance on how to improve them -- yet ChatGPT failed to follow my instruction of not reusing the same label color… It also doesn’t provide any interpretations of the charts. You can find a more comprehensive evaluation of ChatGPT’s data analysis capability [here](https://yudong-94.github.io/personal-website/blog/EvaluatingChatGPTinDataScience/).

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_gpt_analysis1.png" alt="GPT Visualization Habit Analysis 1" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_gpt_analysis2.png" alt="GPT Visualization Habit Analysis 2" width="300" height="400">
</div>

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_gpt_analysis3.png" alt="GPT Visualization Habit Analysis 3" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_gpt_analysis4.png" alt="GPT Visualization Habit Analysis 4" width="300" height="400">
</div>

Here are my main takeaways from this dataset:  

**1. Line and bar charts are the two dominant chart types, followed by Gantt charts**  

It’s not a surprise that line charts and bar charts are the top two common types (47% combined). These are basic, simple, but straightforward ways of visualization. My third favorite chart type is the Gantt chart (14%). The Gantt chart is usually used as a project management tool. However, in Tableau, it is a very powerful tool to make plots that do not start from 0. I often use it to show changes or differences between two groups or two time points.  You can find two Gantt chart examples below. The [first one](https://public.tableau.com/app/profile/yu.dong/viz/20220919CaltrainPeakTimePassengerFlow/CaltrainPeakTimePassengerFlow) visualizes the Caltrain passenger flow at each station during the morning commute time. The [second one](https://public.tableau.com/app/profile/yu.dong/viz/20230417RetirementAgesAroundtheWorld/RetirementAgesAroundtheWorld) plots the differences between men's and women's retirement ages around the world.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_gantt_example1.png" alt="Gantt Chart Example 1" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_gantt_example2.png" alt="Gantt Chart Example 2" width="300" height="400">
</div>

I have also used some less common visualization types like radial charts and bump charts. The prior is used to show comparisons among categories in circular shapes ([Tableau example link](https://public.tableau.com/app/profile/yu.dong/viz/20230724DailyBoxOffice2019-202307/DailyBoxOffice2019-202307)), and the latter is useful to visualize the ranking shifts over time ([Tableau example link](https://public.tableau.com/app/profile/yu.dong/viz/20220110GitHubPopularLanguages2012-2020/GitHubPopularLanguages2012-2020)).

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_radial_example.png" alt="radial Chart Example" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_bump_example.png" alt="Bump Chart Example" width="300" height="400">
</div>

**2. Business is my favorite visualization topic**  

Working at a startup, I am fascinated by entrepreneurship data points. The recent macroeconomics concerns and waves of tech layoffs also inspired several visualization ideas. Here are two examples: the [first one](https://public.tableau.com/app/profile/yu.dong/viz/20240422NewBusiness1-YearSurvivalRates/NewBusiness1-YearSurvivalRates) shows the new business's 1-year survival rate by region, and the [second one](https://public.tableau.com/app/profile/yu.dong/viz/20240311JobPostingonIndeed/JobPostingonIndeed) shows the job postings on Indeed by selected industries.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_biz_example1.png" alt="Business Related Visualization Example 1" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt_viz_summary_biz_example2.png" alt="Business Related Visualization Example 2" width="300" height="400">
</div>

I will write more in the future about my weekly visualization journey. Stay tuned if you are interested!

### Final Thoughts

In the above example, I demonstrated how to integrate web scraping with the text analytics capabilities offered by GPT models. I used my portfolio site to showcase a relatively simple process here, but this approach unlocks many opportunities to extract information in a structured manner from web pages. Whether you are a data scientist, a researcher, or just someone interested in extracting insights from web pages, these techniques can save you significant time and effort.

Last but not least, web scraping could violate a website's terms of service. Please make sure to check out the website's policy first and use official APIs when appropriate.

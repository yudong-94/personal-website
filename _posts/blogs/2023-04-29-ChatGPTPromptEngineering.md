---
title: "Course Notes - ChatGPT Prompt Engineering"
date: 2023-04-29
categories:
  - blog
tags:
  - online courses
  - reading notes
---


ChatGPT has been a very hot topic recently, and has shown great potential to improve productivity. Yesterday, I took the [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) course by DeepLearning.ai. It is a short but very practical course with lots of ChatGPT prompt engineering tactics and code examples. Here are the notes I took during the course.  

## I. Introduction

Two types of LLMs:  
1. Base LLM: predicts next word, based on text training data  
2. Instruction Tuned LLM:
 * tries to follow instructions  
 * Fine-tune on instructions and good attempts at following those instructions  
 * Often refined with RLHF: Reinforcement Learning with Human Feedback  
 * Trained to be ‘Helpful, Honest, Harmless’  
-> Instruction Tuned LLM is generally better for practical uses

## II. Guidelines
**Principles**  
1. Write clear and specific instructions  
 * Clear != short  
2. Give the model time to ‘think’  

Starter code to load openai package with a function to call the completion endpoint:  

```
import openai
openai.api_key  = 'OPENAI_API_KEY'


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
```

### Principle 1 Write clear and specific instructions  

**Tactics:**  
1. Use delimiters to clearly indicate distinct parts of the input  
Delimiters can be anything like ''', “””, <>, :  
This is also useful to avoid prompt injection  

Example:  
```
text = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
'''{text}'''
"""
response = get_completion(prompt)
print(response)
```

2. Ask for structured output  
For example, HTLM or JSON

Example:  
```
prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)
```

3. Ask the model to check whether conditions are satisfied  
Check assumptions required to do the task

Example:  
```
text_1 = f"""
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy.
"""
prompt = f"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …


If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"


\"\"\"{text_1}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 1:")
print(response)
```


4. “Few-shot” prompting  
Give successful examples of completing tasks, then ask model to perform the task

```
prompt = f"""
Your task is to answer in a consistent style.


<child>: Teach me about patience.


<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.


<child>: Teach me about resilience.
"""
response = get_completion(prompt)
print(response)
```

### Principle 2 Give the model time to think

**Tactics:**  
1. Specify the steps required to complete a task  
List the specific steps, or ask for output in a specified format

Example:  
```
text = f"""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""
# example 1
prompt_1 = f"""
Perform the following actions:
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.


Separate your answers with line breaks.


Text:
```{text}```
"""
response = get_completion(prompt_1)
print("Completion for prompt 1:")
print(response)
```

2. Instruct the model to work out its own solution before rushing to a conclusion  

Example:  
```
prompt = f"""
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not.
Don't decide if the student's solution is correct until
you have done the problem yourself.


Use the following format:
Question:
'''
question here
'''
Student's solution:
'''
student's solution here
'''
Actual solution:
'''
steps to work out the solution and your solution here
'''
Is the student's solution the same as actual solution \
just calculated:
'''
yes or no
'''
Student grade:
'''
correct or incorrect
'''


Question:
'''
I'm building a solar power installation and I need help \
working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
'''
Student's solution:
'''
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
'''
Actual solution:
"""
response = get_completion(prompt)
print(response)
```

### Model Limitation: Hallucinations
Hallucinations = Makes statements that sound plausible but are not true  

To reduce hallucinations:  
Ask the model to first find relevant information, then answer the question based on the relevant information  

## III. Iterative Prompt Development  
**Prompt guidelines:**  
* Be clear and specific
* Analyze why the result does not give the desired output
* Refine the idea and the prompt
* Repeat

For example, provide more details in the prompt with the output format, length, focus, examples, etc.  

## IV. Summarizing

One very common use case of LLMs is to summarise the text.
You can modify the prompt to make it focus on a certain espect.

Example:  
```
prompt = f"""
Your task is to extract relevant information from \
a product review from an ecommerce site to give \
feedback to the Shipping department.


From the review below, delimited by triple quotes \
extract the information relevant to shipping and \
delivery. Limit to 30 words.


Review: '''{prod_review}'''
"""


response = get_completion(prompt)
print(response)
```

## V. Inferring

Another common use case is to infer the topic/name/category/sentiment from some text.  

Example: sentiment  
```
prompt = f"""
What is the sentiment of the following product review,
which is delimited with triple backticks?


Give your answer as a single word, either "positive" \
or "negative".


Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Example: extract product and company name from customer reviews  

```
prompt = f"""
Identify the following items from the review text:
- Item purchased by reviewer
- Company that made the item


The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Item" and "Brand" as the keys.
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Example: Doing multiple tasks at once

```
prompt = f"""
Identify the following items from the review text:
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item


The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown" \
as the value.
Make your response as short as possible.
Format the Anger value as a boolean.


Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Example: Infer the topic from a list of pre-defined topics

```
topic_list = [
    "nasa", "local government", "engineering",
    "employee satisfaction", "federal government"
]


prompt = f"""
Determine whether each item in the following list of \
topics is a topic in the text below, which
is delimited with triple backticks.


Give your answer as list with 0 or 1 for each topic.\


List of topics: {", ".join(topic_list)}


Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)
```

## VI. Transformation

We can also use LLMs for text transformation tasks, such as language translation, spelling and grammar checking, tone adjustment, and format conversion.

Example: translation  
ChatGPT is trained with sources in many languages. This gives the model the ability to do translation. Here are some examples of how to use this capability.

```
prompt = f"""
Translate the following English text to Spanish: \
'''Hi, I would like to order a blender'''
"""
response = get_completion(prompt)
print(response)
```

Example: Tone Transformation
```
prompt = f"""
Translate the following from slang to a business letter:
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)
```

Example: Format Conversion  
```
data_json = { "resturant employees" :[
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}


prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response = get_completion(prompt)
print(response)
```

Example: Spellcheck / Grammar check
```
text = [
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    any errors, just say "No errors found". Don't use
    any punctuation around the text:
    '''{t}'''"""
    response = get_completion(prompt)
    print(response)
```

## VII. Expanding

LLMs can also expand a short piece of text to generate a longer piece of text. For example, write a customer service email that is tailored to a customer’s review.

Example:
```
def get_completion(prompt, model="gpt-3.5-turbo",temperature=0): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# given the sentiment from the lesson on "inferring",
# and the original customer message, customize the email
sentiment = "negative"


# review for a blender
review = f"""
So, they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn’t look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush \
very hard items like beans, ice, rice, etc. in the \
blender first then pulverize them in the serving size \
I want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if I need them finer/less pulpy). Special tip when making \
smoothies, finely cut and freeze the fruits and \
vegetables (if using spinach-lightly stew soften the \
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year, the motor was making a funny noise. \
I called customer service but the warranty expired \
already, so I had to buy another one. FYI: The overall \
quality has gone done in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days.
"""


prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service.
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
response = get_completion(prompt)
print(response)
```

**Parameter -- "temperature"**

The degree of exploration or randomness of the model.  
* Temperature = 0 for tasks that require reliability, predictability  
* Higher temperature for tasks that require the variety (more creative)  

Example:  
```
prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service.
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: '''{review}'''
Review sentiment: {sentiment}
"""
response = get_completion(prompt, temperature=0.7)
print(response)
```

## VIII. Chatbot

You can even build a customized chatbot with LLMs.

Example utilizing a modified function with the chat completition endpoint:  
```
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]


response = get_completion_from_messages(messages, temperature=1)
print(response)
```

Example: OrderBot  
We can automate the collection of user prompts and assistant responses to build a OrderBot. The OrderBot will take orders at a pizza restaurant.
```
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)




import panel as pn  # GUI
pn.extension()


panels = [] # collect display


context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages




inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")


interactive_conversation = pn.bind(collect_messages, button_conversation)


dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)


dashboard
```

Please note that all the code blocks above requires OpenAI API key to run. However, you can take the [course](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) yourself and play with the examples in the jupyter notebook embedded in the course.

Hope you find this post helpful :)  

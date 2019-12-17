---
layout: portfolio_entry
title: Python List Comprehension
og_image: images/list_comp.png
category: Career
subtitle: A new power in my arsenal of coding tools.
---
[Image credit](justinlillico.com)

# Hi there!

Thought I'd give a big hi today in apologies for the lack of length that this blog post has in comparison with my somewhat hectic previous one. I can't consistently keep banging out blog posts that long though, I'm pretty busy.

# So… List Comprehensions

Moving right along I have learnt how to use a fantastic paradigm in python for creating lists based on other lists called list comprehensions.

Take the following:

```python
# A list of numbers
old_list = [1,2,3,4,5,6,7,8,9,10]

# Create a new list
new_list = []

# Iterate through previous list and add only the even numbers to the new list.
for number in old_list:
  if number % 2 == 0:
    new_list.append(number)
```

Cool! So obviously what we are trying to do here is extract the even numbers from the old list.

So lets try that out using list comprehensions:

```python
# A list of numbers
old_list = [1,2,3,4,5,6,7,8,9,10]

new_list = [number for number in old_list if number % 2 == 0]
```

Would you look at that? The new list creation is now a one liner!

# Awesome, so how does it work?

Glad you asked. So, as the name suggests, python is capable of 'comprehending' lists in a simplified way that makes reading a breeze (once you get used to it). A basic format might be something like:

```python
list = [ITEM FROM ORIGINAL LIST for ITEM FROM ORIGINAL LIST in ORIGINAL LIST]
```

Alternatively, you could swing in the opposite direction and just go to town on the conditions and chain if statements like so:

```python
new_list = [number for number in old_list if number > 1 if number < 3]
result: [2]
```

# That's all for this week!

Like I said, short and sweet today. Tune in next week for some more geek talk!
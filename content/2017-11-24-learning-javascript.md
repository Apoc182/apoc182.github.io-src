---
layout: portfolio_entry
comments: true
title: Learning JavaScript
category: Career
og_image: images/js.png
main: true
---
<hr>

I know what you're thinking... Clearly, I should also be learning how to use software like Adobe Illustrator and not rely so heavily on MS Paint. But hey, I know it and have been using it for years, seems to do most things I need it to!

So this week I have been getting well stuck into developing this website. They gave me the task of creating a method of arranging thumbnails by date, views and type. This proved to be just the level of challenge I needed.

After sitting in front of my computer for nearly two days researching the things I could do using the JQuery library and vanilla JavaScript, I built a few functions to take care of the job.

---

```javascript
<?php

	echo "var js_views_dates = [";
	for ($i = 0; $i < sizeof($articles_info); $i++) {
		echo " [ " . $articles_info[$i][6] . ", " . strtotime($articles_info[$i][7]) . "] ,";
	}
	echo "];";


?>
```

---

First, I converted the existing array containing the views and dates I needed to know into a JavaScript array. I found a few ways to do this but they were all to complex for me at this level so I came up with this method on my own. Basically just writes the JS on the fly by echoing strings. Pretty simple, but effective.

I won't bore you with the event listeners. I used Jquery for those. Let's skip to the functions I called AFTER the document was ready...

---
```javascript
//Get the elements.
parent = document.getElementById("article_box").children;

//Here, we combine the object in its original form along with the views and date gathered from the php.
//0 : views
//1 : dates
for (var i = 0; i < js_views_dates.length; i++){
	js_article_info[i] = [parent[i], js_views_dates[i][0], js_views_dates[i][1]];
}

//This preserves the original order of the articles
original_order = js_article_info.slice();
```

---

So here I get the elements, attach them to the views and dates I got before and save the list as it currently is. I use this when the user chooses to reset from custom arrangements.

---
```javascript
function setupOrder(original_array, order_by, high_low){

	//This is a sort function that arranges the array by the first dimention, in numeric lowest to highest order
	original_array.sort(function(a, b){
		if (a[order_by] === b[order_by]) {
			return 0;
		} else {
			return (a[order_by] < b[order_by]) ? -1 : 1;
		}
	});

	if(high_low){ 
		original_array.reverse(); 
	}
```

---

So I learned what the sort() function did and how to get it to do my bidding. I feel like this is a function I may end up taking advantage of a lot. This is called when the user chooses the arrangement they want. It sets the order of the list based on an integer value representing their choice.

---

```javascript
function updateArticles(order){

	//This while loop simply removes the contents of the parent div by ID.
	while (document.getElementById("article_box").hasChildNodes()) {
		document.getElementById("article_box").removeChild(document.getElementById("article_box").lastChild);
	}

	//This for loop appends the objects from start to finish of the new array.
	for (var i = 0; i < order.length; i++){
		document.getElementById("article_box").appendChild(order[i][0]);
	}
}
```
---

Finally, this function is called after setupOrder() to update the elements on the page based on the new information.

---

Once I had these functions built, the rest of the logic was only a line or two in the event listeners. I feel like it was efficient, although I'm sure there are many other methods and this is far from the most efficient.

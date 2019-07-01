## Heading

# The largest heading
## The second largest heading
###### The smallest heading

---
## text

**This is bold text**

*This text is italicized*

~~This was mistaken text~~

**This text is _extremely_ important**

---
## Quoting

**Quoting text**

In the words of Abraham Lincoln:
> Pardon my French

+++
## sub-quoting

**Quoting Code**

Use `git status` to list all new or modified files that haven't yet been committed.

Some basic Git commands are:
```
git status
git add
git commit
```

+++
## Python code block

```python
from time import localtime

activities = {8: 'Sleeping', 9: 'Commuting', 17: 'Working',
              18: 'Commuting', 20: 'Eating', 22: 'Resting' }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
```

---
## Links

**Links**

This site was built using [GitHub Pages](https://pages.github.com/).

---
## Lists

**Lists**

- George Washington
- John Adams
- Thomas Jefferson

+++
## Ordered list

1. James Madison
2. James Monroe
3. John Quincy Adams

+++
## Nested list

1. First list item
   - First nested list item
     - Second nested list item

+++
## task list

**Task lists**

- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request


---
## Escapse

**Ignoring Markdown formating**

Let's rename \*our-new-project\* to \*our-old-project\*.


---
## Inline images
![logo](content/assets/logo.png)
+++
<img data-src="content/assets/bg.jpg">


---
<p class="fragment" data-fragment-index="3">Appears last</p>
<p class="fragment" data-fragment-index="1">Appears first</p>
<p class="fragment" data-fragment-index="2">Appears second</p>
+++
<p class="fragment grow">grow</p>
<p class="fragment shrink">shrink</p>
<p class="fragment fade-out">fade-out</p>
<p class="fragment fade-up">fade-up (also down, left and right!)</p>
<p class="fragment fade-in-then-out">fades in, then out when we move to the next step</p>
<p class="fragment fade-in-then-semi-out">fades in, then obfuscate when we move to the next step</p>
<p class="fragment highlight-current-blue">blue only once</p>
<p class="fragment highlight-red">highlight-red</p>
<p class="fragment highlight-green">highlight-green</p>
<p class="fragment highlight-blue">highlight-blue</p>


---
## End

Goodbye!


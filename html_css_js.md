## About this training

- The HTML basics
- The CSS basics
- The JavaScript basics


---
## HTML the basics

+++
**Hypertext Markup Language (HTML)** 

[HTML 5.2](https://www.w3.org/TR/html/) was published as a W3C Recommendation.

![HTML5 logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/120px-HTML5_logo_and_wordmark.svg.png)

+++
## Tags and elements

HTML uses "markup" to annotate text, images, and other content for display in a Web browser. HTML markup includes special "elements" such as 
```html
<head>, <title>, <body>, <header>, <footer>, 
<article>, <section>, <p>, <div>, <span>, <img>, 
<aside>, <audio>, <canvas>, <datalist>, <details>, 
<embed>, <nav>, <output>, <progress>, <video>...
```

+++

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Sample page</title>
  </head>
  <body>
    <h1>Sample page</h1>
    <p>This is a <a href="demo.html">simple</a> sample.</p>
    <!-- this is a comment -->
  </body>
</html>
```

+++
## DOM tree
```bash
├── DOCKTYPE:HTML
└── html
    ├── <head>
    │   ├── #text
    │   └── <title>
    │       └── #text
    ├── #text
    └── <body>
        ├── #text
        ├── <h1>
        │   └── #text
        ├── <p>
        │   ├── #text
        │   ├── <a>href
        │   │   └── #text
        │   └── #text
        ├── #text
        ├── #comment: this is a comment
        └── #text

```

+++
<br><iframe data-src="https://www.liangyulai.cn/demo/learn-html/index.html" style="height:600px;width:800px;"></iframe>


+++
index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
  </head>
  <body>
    <h1>Mozilla is cool</h1>
    <img src="images/firefox-icon.png" alt="The Firefox logo: a flaming fox surrounding the Earth.">

    <p>At Mozilla, we’re a global community of</p>
    
    <ul> <!-- changed to list in the tutorial -->
      <li>technologists</li>
      <li>thinkers</li>
      <li>builders</li>
    </ul>

    <p>working together to keep the Internet alive and accessible, so people worldwide can be informed contributors and creators of the Web. We believe this act of human collaboration across an open platform is essential to individual growth and our collective future.</p>

    <p>Read the <a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a> to learn even more about the values and principles that guide the pursuit of our mission.</p>
  </body>
</html>
```

+++
## references

- [Wikipedia: HTML](https://en.wikipedia.org/wiki/HTML)
- [W3C: HTML 5.2 spec](https://www.w3.org/TR/html/)
- [w3schools: HTML5 Tutorial](https://www.w3schools.com/html/default.asp)
- [MDN: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)


---
## CSS the basics

+++
**Cascading Style Sheets (CSS)**

CSS tells how to display on the screen
- layout
- colors
- fonts

+++
<iframe data-src="https://www.liangyulai.cn/demo/learn-css/index.html" style="height:600px;width:800px;"></iframe>

+++
index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
    <link href="styles/style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>Mozilla is cool</h1>
    <img src="images/firefox-icon.png" alt="The Firefox logo: a flaming fox surrounding the Earth.">

    <p>At Mozilla, we’re a global community of</p>
    
    <ul> <!-- changed to list in the tutorial -->
      <li>technologists</li>
      <li>thinkers</li>
      <li>builders</li>
    </ul>

    <p>working together to keep the Internet alive and accessible, so people worldwide can be informed contributors and creators of the Web. We believe this act of human collaboration across an open platform is essential to individual growth and our collective future.</p>

    <p>Read the <a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a> to learn even more about the values and principles that guide the pursuit of our mission.</p>
  </body>
</html>
```
+++style.css
```css
html {
  font-size: 10px;
  font-family: 'Open Sans', sans-serif;
}


h1 {
  font-size: 60px;
  text-align: center;
}

p, li {
  font-size: 16px;  
  line-height: 2;
  letter-spacing: 1px;
}


html {
  background-color: #00539F;
}

body {
  width: 600px;
  margin: 0 auto;
  background-color: #FF9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}

h1 {
  margin: 0;
  padding: 20px 0;  
  color: #00539F;
  text-shadow: 3px 3px 1px black;
}

img {
  display: block;
  margin: 0 auto;
}
```

+++
## references

- [W3C: CSS spec](https://www.w3.org/TR/CSS/)
- [MDN: CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)


---
## JavaScript the basics

+++
<iframe data-src="https://www.liangyulai.cn/demo/learn-js/index.html" style="height:600px;width:800px;"></iframe>

+++
index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
    <link href="styles/style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>Mozilla is cool</h1>
    <img src="images/firefox-icon.png" alt="The Firefox logo: a flaming fox surrounding the Earth.">

    <p>At Mozilla, we’re a global community of</p>

    <ul> <!-- changed to list in the tutorial -->
      <li>technologists</li>
      <li>thinkers</li>
      <li>builders</li>
    </ul>

    <p>working together to keep the Internet alive and accessible, so people worldwide can be informed contributors and creators of the Web. We believe this act of human collaboration across an open platform is essential to individual growth and our collective future.</p>

    <p>Read the <a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a> to learn even more about the values and principles that guide the pursuit of our mission.</p>
  <button>Change user</button>
  <script src="scripts/main.js"></script>
  </body>
</html>
```


+++
style.css
```css
html {
  font-size: 10px;
  font-family: 'Open Sans', sans-serif;
}


h1 {
  font-size: 60px;
  text-align: center;
}

p, li {
  font-size: 16px;  
  line-height: 2;
  letter-spacing: 1px;
}


html {
  background-color: #00539F;
}

body {
  width: 600px;
  margin: 0 auto;
  background-color: #FF9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}

h1 {
  margin: 0;
  padding: 20px 0;  
  color: #00539F;
  text-shadow: 3px 3px 1px black;
}

img {
  display: block;
  margin: 0 auto;
}
```

+++
main.js
```javascript
// Image switcher code

var myImage = document.querySelector('img');

myImage.onclick = function() {
	var mySrc = myImage.getAttribute('src');
	if(mySrc === 'images/firefox-icon.png') {
      myImage.setAttribute ('src','images/firefox2.png');
	} else {
	  myImage.setAttribute ('src','images/firefox-icon.png');
	}
}

// Personalized welcome message code

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
  var myName = prompt('Please enter your name.');
  localStorage.setItem('name', myName);
  myHeading.innerHTML = 'Mozilla is cool, ' + myName;
}

if(!localStorage.getItem('name')) {
  setUserName();
} else {
  var storedName = localStorage.getItem('name');
  myHeading.innerHTML = 'Mozilla is cool, ' + storedName;
}

myButton.onclick = function() {
  setUserName();
}

```

+++
## references

- [MDN: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [ECMA: ECMAScript 2019 Language Sepc](https://tc39.github.io/ecma262/)

---
## How browsers works

To be continued...

+++
## references
- [CoolShell: 浏览器的渲染原理简介](https://coolshell.cn/articles/9666.html)
- [How Browsers Work: Behind the scenes of modern web browsers](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/)

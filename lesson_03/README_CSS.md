# Cascading Style Sheets

## What is CSS?

CSS (Cascading Style Sheets) is a styling language used to control the appearance and layout of HTML elements. It seperates content (HTML) from presentation, making web development more efficient and organized. CSS is read by the browser in a cascading order, meaning styles are applied in the following sequence:

1. **Inline styles**: Applied directly within HTML elements and have the highest precedence.

2. **Internal styles** Defined within a `<style>` tag in the `<head>` of an HTML document.

3. **External stylesheets**: Linked via a `<link>` tag and provide a centralized location for styles.

4. **Browser defaults**: The styles provided by the browser when no custom CSS is defined.

When reading a CSS file you read it from top to bottom. Styling applied at the very top will be overriden by styles at the bottom.

CSS is used to:

* Style HTML elements with colors, fonts, and layouts

* Create responsive designs for various devices

* Seperate the visual presentation of a webpage from its content

* HTML is the Skeleton, while CSS is the appearance of our website
## How CSS Works

CSS styles are applied to HTML elements via `selectors`. Styles are defined in rulesets that consist of:

* **Selector**: Specifies the HTML element(s) to style.

* **Declaration Block**: Contains one or more declarations enclosed in curly braces `{}`.

* **Declarations**: Define the styles (color, font-size) in `property: value; pairs.

**EXAMPLE**:

```css
h1 {
    color: blue;
    font-size: 24px;
}
```

## CSS Syntax

A CSS rule has the following structure:

```css
selector {
    property: value;
}
```

* **Selector**: Targets the HTML element(s).

* **Property**: Specifies the aspect to style (ex: color).

* **Value**: Defines the style (ex: red).

**EXAMPLE**

```css
p {
    color: red;
    margin: 10px;
}
```

## Ways to Apply CSS

1. **Inline CS**: Directly in the HTML element using the `style` attribute.
```html
<p style="color: red; font-size: 20px;"> This is a styled paragraph.</p>
```

2. **Internal CSS**: Inside a `<style>` tag within the `<head>` of the HTML document.
```html
<style>
    body {
        background-color: lightgray;
    }
</style>
```

3. **External CSS**: In a seperate file linked with the `<link>` tag.
```html
<link rel="stylesheet" href="styles.css">
```
Example `styles.css` file:
```css
body {
    font-family: Arial, sans-serif;
}
```


## Commonly Used CSS Properties

1. **Color and Background**:

* `color`: Text color.

* `background-color`: Background color.
```css
h1 {
    color: navy;
    background-color: lightyellow;
}
```

2. **Text and Font**:

* `font-size`: Size of text.

* `font-family`: Font type.

* `text-align`: Alignment of text.
```css
p {
    font-size: 16px;
    text-align: center;
}
```

3. **Spacing**:

* `margin`: Space outside the element.

* `padding`: Space inside the element.
```css
div {
    margin: 20px;
    padding: 10px;
}
```

4. **Borders and Dimensions**:

* `border`: Border style, width, and color.

* `width` and `height`: Element dimensions.
```css
img {
    border: 2px solid black;
    width: 200px;
}
```

## CSS Units

CSS allows various units to define sizes and spaces:

1. **Absolute Units**: Fixed sizes (ex: px, cm).
    - `10px`: 10 pixels

2. **Relative Units**: Based on the parent element or viewport (ex: em, %, vh, vw).
    - `2em`: Twice the size of the current font

Example:
```css
.container {
    width: 80%;
    height: 50vh;
    font-size: 1.5em;
}
```

## Specificity in CSS

CSS specificity determines which styles are applied when multiple rules target the element. Specificty is calculated as follows:

1. **Inline styles**: These have the highest specificty (ex: `<p style="color: red;">`)

2. **ID selectors**: Ranked next highest (ex: `#header`)

3. **Class selectors, attributes, and pseudo-classes**: These are in the middle (ex: `.highlight`, `[type="text"]`, `:hover`)

4. **Type selectors and pseudo-elements**: These have the lowest specificty (ex: `p`, `::after`)

Example:
```css
/* Low specificity */
h1 {
    color: black;
}

/* Higher specificity */
.highlight {
    color: blue;
}

/* Highest specificity */
#main {
    color: red;
}
```

## Selectors in CSS

Selectors determine which HTML elements are styled. Common selectors include:

1. **Type Selector**: Targets an element by its name.
```css
h1 {
    color: blue;
}
```

2. **Class Selector**: Targets elements with a specific class.
```css
.highlight {
    background-color: yellow;
}
```

3. **ID Selector**: Targets an element with a specific ID.
```css
#main {
    font-size: 18px;
}
```

4. **Group Selector**: Targets multiple elements.
```css
h1, h2, h3 {
    font-weight: bold;
}
```

## The Box Model

Every HTML element is treated as a box, consisting of:

1. **Content**: The innermost area containing text or other elements.

2. **Padding**: Space between the content and the border.

3. **Border**: Surrounds the padding (or content if no padding).

4. **Margin**: Space outside the border.

Example:
```css
.box {
    margin: 20px;
    border: 2px solid black;
    padding: 10px;
    width: 200px;
}
```


## Conclusion

CSS is essential for creating visually appealing and user-friendly webpages. By combining HTML and CSS, you can create layouts, add colors, and imporve overall design
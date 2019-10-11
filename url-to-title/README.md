# URL to Title Converter

- Status: Code tested and working as of 2019-10-11

## What

The simple function code in `index.py` takes website URLs as input, and produces page titles (from the site's `<title>` tag) as output. **The code demonstrates how you can create a *custom function compute runtime* that contains additional libraries or software needed by your function**.

The code is loosely based on this Alibaba Cloud blog article: [Develop Function Compute by Installing Third-Party Dependencies
](https://www.alibabacloud.com/blog/develop-function-compute-by-installing-third-party-dependencies_595253)

## How To Use This Code

You'll need to have the `funfun ` and `fcli` commands installed. Further, the `fun` command requires Docker to be installed in order for `fun install` to work, so be sure to install Docker as well!
 
There are *3 steps* to use this code:

### 1 - Run `fun install`

Install the BeautifulSoup library using the `fun install` command. First, we need to generate a `fun.yml` file:

```
fun install --runtime python3 --package-type pip --save bs4
```

Next, we run the command without any parameters to install the packages listed in `fun.yml`:

```
fun install
```

### 2 - Run 'fun deploy`

```
fun deploy
```

This will read the `template.yml` file to determine how to deploy the function and its related service. See `template.yml` for details.

### 3 - Call your function using `fcli`

Note: take a look at the code in `template.yml` to see what the *function* and *service* names are (unless you have made changes, they should match the names used in the example below):

```
fcli function invoke -s get_title_svc -f get_title_fcn --event-str 'https://www.google.com'
```

You can replace 'https://www.google.com' with the URL of your choice. Try it out!

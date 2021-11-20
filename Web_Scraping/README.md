# IEEE Web Scraping Workshop

This workshop outlines the steps of scraping contents from webpages in both
javascript and python using <b>BeautifulSoup</b> (python) and <b>cheerio</b> (javacsript).

## Setup

This code uses the dotenv library in both languages to keep users and passwords
secure (aka not hardcoded). As such, you will need to set up your own `.env`
file in the root of the project: `web_scraping` (not `javascript` or `python`).

<pre>
└───Web_Scraping
    │   >>> <mark><b><u>.env</u></b></mark> <<<
    │   .gitignore
    │   README.md
    │
    ├───javascript
    │   │   index.js
    │   │   package-lock.json
    │   │   package.json
    │   │
    │   └───node_modules
    │
    └───python
            app.py
</pre>

The file should include:

```
GM_USERNAME=sender_email@email.com
GM_PASSWORD=sender_password
GM_RECIPIENT=recipient_email@email.com
```

##### Javascript

The file `package.json` is used to install dependencies:

```json
"dependencies": {
    "cheerio": "^1.0.0-rc.10",
    "dotenv": "^10.0.0",
    "node-fetch": "^2.6.6",
    "nodemailer": "^6.7.1"
}
```

If you have node and npm installed already just open a terminal, navigate to the
`javascript` directory and run:

```shell
> npm install
> node index.js
```

This references `package.json` for the dependencies listed above and installs
them. You then run the code in `index.js`.

##### Python

Navigate to the `python` directory and use `pip` to install the necessary
dependencies:

```shell
> pip install python-dotenv requests beautifulsoup4
> py app.py
```

## Installing NodeJS and Python

If you don't already have NodeJS or Python installed, here are some brief
instructions on how to do so:

1. Download the LTS version of node and npm [here](https://nodejs.org/en/download/).
2. You can click through the installer and make sure you check the box to
   automatically install the necessary tools. - One of these tools is Python, so it should also be installed automatically
   later on.
3. When the command window appears to install the additional tools, press a key
   to continue to the next step.

Run the following commands to ensure that they were installed properly. They
should return the version numbers:

```shell
> node -v
v14.15.1

> npm -v
6.14.8

> python --version
Python 3.9.5
```

The reason we need node is because Javascript is an interpreted language that
can only be run in internet browsers. Node allows us to run .js files locally.

`pip` and `npm` are package managers which make it very easy to install
libraries for use in your projects. You can browse the available packages at
[pypi.org](https://pypi.org/) and [npmjs.com](https://www.npmjs.com/) respectively.

## Future Steps

Implement your own conditions to suit your needs.

-   Do you want to truly automate this and be notified on a timer?
    -   Use the `time` library in Python or Date functions in Javascript to
        notify yourself daily, weekly, etc. Or use Task Scheduler and a shell script
        to run your code as often as needed.
    -   Buy a Raspberry Pi, run the code and throw it in a desk drawer so it's
        always running.
-   Do you want to be notified when prices drop?
    -   Set up global variables to store the prices and only email if they dropped
        since the last query.

## License

All workshops for the Villanova Chapter of IEEE (all code within this
repository and specifically this web scraping workshop) are licensed under the
[GNU General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html), also included within the [`COPYING`](https://github.com/davisgriffin/IEEE_Workshops/blob/main/COPYING) file.

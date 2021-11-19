# IEEE Web Scraping Workshop

This workshop outlines the steps of scraping contents from webpages in both
javascript and python using BeautifulSoup (python) and cheerio (javacsript).

## Setup

This code uses the dotenv library in both languages to keep users and passwords
secure (aka not hardcoded). As such, you will need to set up your own `.env`
file in the root of the project: `web_scraping` (not `javascript` or `python`).

<pre>
└───Web_Scraping
    │   <mark><b>.env</b></mark>
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

## Future Steps

Implement your own conditions to suit your needs.

-   Do you want to truly automate this and be notified on a timer?
    -   Setup a timer or use the `time` library to notify yourself daily, weekly,
        etc.
    -   Buy a Raspberry Pi, run the code and throw it in a desk drawer so it's
        always running.
-   Do you want to be notified when prices drop?
    -   Set up global variables to store the prices and only email if they dropped
        since the last query.

## License

All workshops for the Villanova Chapter of IEEE (all code within this
repository) are licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html),
also included within the `COPYING` file.

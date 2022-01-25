# GA PID Server
This repository contains the Apache rewrite rules & static HTML homepage for a persistent identifier (PID) server implemented by [Geoscience Australia](https://www.ga.gov.au) for the `pid.geoscience.gov.au` domain which GA administers for geoscience matters on behalf of Australian geoscience community.

**NOTE**: this server is currently in development and it online not at <http://pid.geoscience.gov.au> but at <http://surroundaustralia.com>.

## Repository content

### static web pages

* [htdocs/](htdocs) folder

### redirect rules

The main server configuration file is [conf/httpd.conf](conf/httpd.conf). It _includes_ (`IncludeOptional conf/sites/*.conf`) files in the [conf/sites](conf/sites) folder. Currently, there is only one site supported by the server: `pid.geosciecne.gov.au`.

### tests

There is one data file, `rule-cases.json` that contains tests for all implemented rules. The test case format is:

```
"<KEY>":[
   {
      "label": "<LABEL>}",
      "from": "{HOST}/<FROM-IRI>",
      "to": "<TO-IRI>",
      "headers": {<HEADERS>}
   }
],
```

`<KEY>` - just an ID for a case, could be anything
`<LABEL>` - a label for each test case that must be unique as it is needed to indicate which tests faile, if any
`<FROM-IRI>` - an IRI that is matched by a RedirectRule in the redirect server. Must include Query String Arguments if used
`<TO-IRI>` - where the full IRI of `{HOST}/<FROM-IRI>` is expected to redirect to
`<HEADERS>` - any HTTP headers needed to make the redirect, e.g. `Accept: text/turtle`

There are two testing files:

1. `test_redirects.py` - tests only that the `<FROM-IRI>` redirects to `<TO-IRI>`. Doesn't matter if the `<TO-IRI>` doesn't exist
2. `test_resolutions.py` - tests that redirect to `<TO-IRI>` receive an HTTP 200 code, i.e. that the `<TO-IRI>` works

#### localhost testing
If a local Apache server is established, e.g. localhost on a Windows, Linux or Mac desktop, then the PID rules can be tested with it by just loading the file in the [conf/sites](conf/sites) folder into that local server's sites and ensuring it is configured to see it (e.g. an `Include` statement to that file in your main `httpd.conf` file).

#### Docker testing
You can use the Dockerfile with Docker Desktop to create a Docker container locally and run tests with that.

#### Remote testing
You can set the `host` variable in the two testing files to test not locally (http://localhost) but remotely, e.g. http://pid.geoscience.gov.au.

### GitHub Actions
An Apache server loaded with this repository's static content and redirect rules can be deployed with GitHub Actions using the `deployment.yaml` file. One Action is used to validate new rules, the other reloads the server online:

1. On pull request to the `main` branch:
    - Run a test Docker image to run `pytest` tests
2. On push to the `main` branch:
    - Build Docker image, push to AWS ECR & deploy to a Kubernetes cluster

### Docker image
The file `Dockerfile` is used to create a Docker container that can be run locally for testing or pushed remotely.

## License
This code is licensed using the Apache licence. See the [LICENSE](LICENSE) file for the deed.

## Contact

*owner:*  
![](https://www.ga.gov.au/__data/assets/image/0013/16510/ga-logo.jpg)  
**Geoscience Australia**  
<https://www.ga.gov.au>  
<dataman@ga.gov.au>  

*creator:*  
![](https://vocexcel.surroundaustralia.com/static/media/logo-dark.41edee3d.svg)  
**SURROUND Australia Pty. Ltd.**  
<https://surroundaustralia.com>  
<info@surroundaustralia.com>  
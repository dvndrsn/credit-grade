Code Test Guidelines
====================

Bond Street Code Test
---------------------

Welcome to the Bond Street Code Test!
This test helps us understand your technical proficiency at the role
you're applying for. We believe this approach allows you to
present your skills in the best possible light with the tools and
languages you're most comfortable with.
If you have any questions at all, please let us know!

Credit Grade Data Analysis & Web Service
========================================

Overview
--------

Create a RESTful web service that returns a credit grade when fed data about an individual business. Credit grade is a measure of credit quality with A1 being the highest and D5 being the lowest.

`sample_data.csv` is historical data on loans that have already been underwritten, including the final `credit_grade` that was assigned to them. Use this historical data to inform the design of your new credit grading algorithm.

Implementation
--------------

I chose to use flask for ease of implementation for REST web services. Data was analyzed and processed using Pandas, selecting key numerical features to use for training a simple Linear Regression model through Scikit Learn. Test Cases were implemented using Unit Test and Mock.

Train the model:

```
python init_model.py sample_data.csv
```

Start the server locally:

```
python runserver.py
```

Send a sample request:

```
curl 'http://localhost:5000/CreditGrade?approved_amount=1&term_months=1&dscr=1&vantage_score=1&fico_score=1&intelliscore=1&bdfs_score=1&annual_revenue=1&business_founding_years=1'
```

Sample response:

```
{
    "credit_grade": "D5"
}
```

How you'll be evaluated
=======================

Functionality
-------------

* Does the project provide the functionality asked for?
* Does it look like the Screenshots provided (if applicable)?

Design
------

* How do you design and lay out your code?
* Is the code well organized with easy to understand
interfaces?
* Are models/views/templates organized in a way that
increases cohesiveness and loose coupling?

Cleanliness and Clarity
-----------------------

* Is the code cleanly formatted and follow language
conventions?
* Are variables, functions and files well named?

Tooling
-------

* Does your project use the tools you selected effectively?
* Can you explain your rationale for using these tools?

Packaging
---------

* Is the final project presented in a way that's easy to
understand?
* Do you communicate why you made important decisions?

Submitting your test
--------------------

Our preferred way to evaluate code tests is on Github, via a pull
request. This makes it easy for us to have a conversation with you
about your code.

The best way to set this up is to create a new repository when you
start, with the contents of this zip file on the master branch. You
can then branch off to add your code and when you're done, create
a pull request from your feature branch to the master branch. It's
helpful if you annotate the PR with comments of important
decisions you made, or other places you find necessary.
If you have concerns about privacy and don't have any private
repos to spare, we recommend BitBucket provides free private
repositories.

Extra credit
------------

In each code test we’ve provided a few opportunities to go above
and beyond. These provide more opportunities to show your
strengths and are by no means required – if you don’t know how to
do them, that’s ok!

## Noverde - Challenge


 + Install Postgresql in your local machine
	+ In Postgres execute:
		+ `Create databases "chaallenge";`
		+ `Create databases "challenge_test";`
		+ `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

 + Clone repository
	+ `git clone git@bitbucket.org:lendicobrasil/cdc-manager.git`

 + Create and activate "virtualenv"

 + Install "requirements":
	+ `(pip install -r requirements-dev.txt)`

 + Set environment variable:
	+ DATABASE_URI=postgresql://<user>:<password>@localhost:5432/<database>
	+ DATABASE_URI_TEST= postgresql://<user>:<password>@localhost:5432/<database>_URI_FOR_TESTS
	+ CREDIT_ANALISES_ENGINE_URI= <url for credit-engine>

 + Execute
	+ `flask db migrate`

 + Start server
	+ `flask run`

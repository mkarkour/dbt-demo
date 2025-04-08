Welcome to your new dbt project!

### Using the starter project

To test the connection:
$ dbt debug

Execute a model by running the following command:
$ dbt run
or
$ dbt build --select model_name

Then after executing you can show the result by doing (make sure you are have dbt v1.7+ installed):
$ dbt show --select model_name

To generate the documentation:
$ dbt docs generate
$ dbt docs serve



### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

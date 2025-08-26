from flask import Flask, render_template, request
from models.nl_to_sql import nl_to_sql
from utils.db import run_query


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]

        # Convert the natural language question to SQL
        sql_query = nl_to_sql(question)

        # Execute the SQL query and get results
        results = run_query(sql_query)

        # Render the results in the template
        return render_template("index.html", question=question, sql_query=sql_query, results=results.to_html(classes="table table-striped") if isinstance(results, pd.DataFrame) else results)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
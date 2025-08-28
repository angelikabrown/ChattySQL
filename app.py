from flask import Flask, render_template, request
from models.nl_to_sql import nl_to_sql
from utils.db import run_query
from utils.viz import plot_chart
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    
    Main page where users ask their natural language questions, receive SQL queries, and view results.

    """
    if request.method == "POST":
        question = request.form["question"]

        # Convert the natural language question to SQL
        sql_query = nl_to_sql(question)

        # Execute the SQL query and get results
        results = run_query(sql_query)

        # Render the results in the template
        return render_template("index.html", question=question, sql_query=sql_query, results=results.to_html(classes="table table-striped") if isinstance(results, pd.DataFrame) else results)
    
    return render_template("index.html")


@app.route("/visualize", methods=["POST"])
def visualize():
    """

    Visualization page where users can create charts based on SQL query results.

    """
    sql = request.form.get("sql", "").strip()
    chart_type = request.form.get("chart_type", "bar").strip().lower()

    allowed_chart_types = ["bar", "line", "pie", "scatter"]
    if chart_type not in allowed_chart_types:
        chart_type = "bar"  

    # Execute the SQL query and get results
    results = run_query(sql)    
    if isinstance(results, str): # Error handling
        return render_template("results.html", question="(visualization step)", sql=sql, results=results)
    
    img = plot_chart(results, chart_type)
    if not img:
        #error handling
        return render_template("vizualize.html", chart=None, chart_type=chart_type, error="Could not generate chart.")
    return render_template("visualize.html", chart=img, chart_type=chart_type)




if __name__ == "__main__":
    app.run(debug=True)
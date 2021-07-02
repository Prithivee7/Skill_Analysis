from flask import Flask, render_template, request
from sqlalchemy import and_
from insert_data import *
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://mzzmarljuuoopa:a16ef88c2745021b4785d24b02b6331c751ff1c611a3a26694e3a97f7146a04a@ec2-107-21-10-179.compute-1.amazonaws.com:5432/d1vn3evkvfn2k7'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

dict_full = {}
with app.app_context():
    data_set = Data.query.order_by(Data.serial).all()
    for data in data_set:
        dict_full[data.serial] = [data.job_name, data.experience,
                                  data.skill, data.count, data.total_count]

pd.options.display.float_format = '{:,.2f}'.format


def write_html():
    with open('templates/plots.html', 'r') as f:
        temp = ''.join(f.readlines())
    return {"page": temp}


def data_science_func(experience):
    list_ds = []
    for i in dict_full:
        if(dict_full[i][0] == 'Data Science'):
            list_ds.append(i)
    y_list = []
    x_list = []
    percent = []
    val = 0
    for i in list_ds:
        if(dict_full[i][1] == int(experience)):
            val = dict_full[i][4]
            y_list.append(dict_full[i][2])
            x_list.append(dict_full[i][3])
            p = format(((dict_full[i][3]/dict_full[i][4])*100), '.2f') + '%'
            percent.append(p)
    fig3 = go.Figure(go.Bar(
        x=x_list,
        y=y_list,
        text=percent,
        textposition='outside',
        orientation='h'
    ))
    t = ''
    if(experience == '1'):
        t = '0-2 years'
    elif(experience == '2'):
        t = '3-5 years'
    elif(experience == '3'):
        t = '6-8 years'
    elif(experience == '4'):
        t = '9-12 years'
    else:
        t = 'more than 12 years '

    txt = "Top 10 skills for data scientist having experience of " + \
        t+"\n"+". Extracted from "+str(val)+" Job Requirements"
    fig3.update_layout(
        title={
            'text': txt,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='Top skills',
            autorange="reversed"
        ),
        xaxis=dict(
            title='Number of Occurences',
        )
    )
    fig3.update_layout(
        autosize=False,
        width=1500,
        height=690,)
    page = open('templates/plots.html', 'w')
    page.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    return write_html()


def frontend_func(experience):
    list_ds = []
    for i in dict_full:
        if(dict_full[i][0] == 'Front end'):
            list_ds.append(i)
    y_list = []
    x_list = []
    percent = []
    val = 0
    for i in list_ds:
        if(dict_full[i][1] == int(experience)):
            val = dict_full[i][4]
            y_list.append(dict_full[i][2])
            x_list.append(dict_full[i][3])
            p = format(((dict_full[i][3]/dict_full[i][4])*100), '.2f') + '%'
            percent.append(p)
    fig3 = go.Figure(go.Bar(
        x=x_list,
        y=y_list,
        text=percent,
        textposition='outside',
        orientation='h'
    ))
    t = ''
    if(experience == '1'):
        t = '0-2 years'
    elif(experience == '2'):
        t = '3-5 years'
    elif(experience == '3'):
        t = '6-8 years'
    elif(experience == '4'):
        t = '9-12 years'
    else:
        t = 'more than 12 years '

    txt = "Top 10 skills for frontend developer having experience of " + \
        t+"\n"+". Extracted from "+str(val)+" Job Requirements"
    fig3.update_layout(
        title={
            'text': txt,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='Top skills',
            autorange="reversed"
        ),
        xaxis=dict(
            title='Number of Occurences',
        )
    )
    fig3.update_layout(
        autosize=False,
        width=1500,
        height=690,)
    page = open('templates/plots.html', 'w')
    page.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    return write_html()


def backend_func(experience):
    list_ds = []
    for i in dict_full:
        if(dict_full[i][0] == 'Backend'):
            list_ds.append(i)
    y_list = []
    x_list = []
    percent = []
    val = 0
    for i in list_ds:
        if(dict_full[i][1] == int(experience)):
            val = dict_full[i][4]
            y_list.append(dict_full[i][2])
            x_list.append(dict_full[i][3])
            p = format(((dict_full[i][3]/dict_full[i][4])*100), '.2f') + '%'
            percent.append(p)
    fig3 = go.Figure(go.Bar(
        x=x_list,
        y=y_list,
        text=percent,
        textposition='outside',
        orientation='h'
    ))
    t = ''
    if(experience == '1'):
        t = '0-2 years'
    elif(experience == '2'):
        t = '3-5 years'
    elif(experience == '3'):
        t = '6-8 years'
    elif(experience == '4'):
        t = '9-12 years'
    else:
        t = 'more than 12 years '

    txt = "Top 10 skills for backend developer having experience of " + \
        t+"\n"+". Extracted from "+str(val)+" Job Requirements"
    fig3.update_layout(
        title={
            'text': txt,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='Top skills',
            autorange="reversed"
        ),
        xaxis=dict(
            title='Number of Occurences',
        )
    )
    fig3.update_layout(
        autosize=False,
        width=1500,
        height=690,)
    page = open('templates/plots.html', 'w')
    page.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    return write_html()


def machine_learning_func(experience):
    list_ds = []
    for i in dict_full:
        if(dict_full[i][0] == 'Machine Learning'):
            list_ds.append(i)
    y_list = []
    x_list = []
    percent = []
    val = 0
    for i in list_ds:
        if(dict_full[i][1] == int(experience)):
            val = dict_full[i][4]
            y_list.append(dict_full[i][2])
            x_list.append(dict_full[i][3])
            p = format(((dict_full[i][3]/dict_full[i][4])*100), '.2f') + '%'
            percent.append(p)
    fig3 = go.Figure(go.Bar(
        x=x_list,
        y=y_list,
        text=percent,
        textposition='outside',
        orientation='h'
    ))
    t = ''
    if(experience == '1'):
        t = '0-2 years'
    elif(experience == '2'):
        t = '3-5 years'
    elif(experience == '3'):
        t = '6-8 years'
    elif(experience == '4'):
        t = '9-12 years'
    else:
        t = 'more than 12 years '

    txt = "Top 10 skills for machine learning engineer having experience of " + \
        t+"\n"+". Extracted from "+str(val)+" Job Requirements"
    fig3.update_layout(
        title={
            'text': txt,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='Top skills',
            autorange="reversed"
        ),
        xaxis=dict(
            title='Number of Occurences',
        )
    )
    fig3.update_layout(
        autosize=False,
        width=1500,
        height=690,)
    page = open('templates/plots.html', 'w')
    page.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    return write_html()


def data_analysis_func(experience):
    list_ds = []
    for i in dict_full:
        if(dict_full[i][0] == 'Data Analyst'):
            list_ds.append(i)
    y_list = []
    x_list = []
    percent = []
    val = 0
    for i in list_ds:
        if(dict_full[i][1] == int(experience)):
            val = dict_full[i][4]
            y_list.append(dict_full[i][2])
            x_list.append(dict_full[i][3])
            p = format(((dict_full[i][3]/dict_full[i][4])*100), '.2f') + '%'
            percent.append(p)
    fig3 = go.Figure(go.Bar(
        x=x_list,
        y=y_list,
        text=percent,
        textposition='outside',
        orientation='h'
    ))
    t = ''
    if(experience == '1'):
        t = '0-2 years'
    elif(experience == '2'):
        t = '3-5 years'
    elif(experience == '3'):
        t = '6-8 years'
    elif(experience == '4'):
        t = '9-12 years'
    else:
        t = 'more than 12 years '

    txt = "Top 10 skills for data analyst having experience of " + \
        t+"\n"+". Extracted from "+str(val)+" Job Requirements"
    fig3.update_layout(
        title={
            'text': txt,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis=dict(
            title='Top skills',
            autorange="reversed"
        ),
        xaxis=dict(
            title='Number of Occurences',
        )
    )
    fig3.update_layout(
        autosize=False,
        width=1500,
        height=690,)
    page = open('templates/plots.html', 'w')
    page.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
    return write_html()


@app.route("/")
def index():
    return render_template("index_page.html")


@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == 'POST':
        experience = request.form.get("experience")
        category = request.form.get("category")
        if category == 'data_science':
            return data_science_func(experience)
        elif category == 'frontend':
            return frontend_func(experience)
        elif category == 'backend':
            return backend_func(experience)
        elif category == 'machine_learning':
            return machine_learning_func(experience)
        elif category == 'data_analysis':
            return data_analysis_func(experience)


if __name__ == "__main__":
    app.run(debug=True)

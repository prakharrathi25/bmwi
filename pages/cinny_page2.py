# Import necessary libraries 
from typing import Optional
import pandas as pd 
import streamlit as st 
import base64
import geopandas as gpd
import json
import matplotlib.pyplot as plt
import json
import plotly.express as px

# Custom modules 
from .utils import *

# Suppress warnings in streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Create the app that would be run 
def app():

    st.write("Hi, I am Cinny.")

    # ''' Section to upload all the data file '''
    # st.markdown("## Data Upload and Map Viz.")

    # # Upload the dataset and save as csv
    # st.markdown("### Upload a csv file for analysis.") 
    # st.write("\n")

    # # Code to read a single file 
    # uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
    # global data
    # if uploaded_file is not None:
    #     try:
    #         data = pd.read_csv(uploaded_file, encoding='latin_1')
    #     except Exception as e:
    #         print(e)
    #         data = pd.read_excel(uploaded_file, encoding='latin_1')
    
    # ''' Load the data and save the dataset in a separate folder to allow for quick reloads '''
    
    # # Save the data
    # data.to_csv('data/main_data.csv', index=False, encoding='latin_1')

    # # Raw data display  
    # st.dataframe(data)

    # # Show data statistics 
    # st.write("**Data Size:**", data.shape)

    # ''' Display the features of the data which can be visualized '''

    # # Collect the columns
    # data_cols = data.columns
    # col_to_display = st.selectbox("Select which column to visualise on the map",
    #                              options=data_cols, 
    #                              index=4, 
    #                              # format_func = lambda x: get_english_term(x)
    #                              )

    # ''' Display the document containing the various column descriptions '''
    
    # # Check if the data description needs to be displayed 
    # display_doc = st.radio("Display Column Descriptions", options=["Yes", "No"], index=1)
    # if display_doc == "Yes":

    #     # Read a pdf of the data dictionary
    #     pdf_file_path = 'documents\pdf\coronadata_description.pdf'
    #     with open(pdf_file_path,"rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
    #     # HTML for the file to be displayed 
    #     pdf_display = f'<embed src="data:application/pdf;base64, {base64_pdf}" width="700" height="1000" type="application/pdf">'
    #     st.markdown(pdf_display, unsafe_allow_html=True)

    html_string = """
<body>
    <script src="https://d3js.org/d3.v3.js"></script>
    <div class="col center-block" id = "gg"></div>
    
    <script>
      
//Constants for the SVG
var width = 1000,
  height = 800;

//Set up the colour scale
var color = d3.scale.category20b();

//Set up the force layout
var force = d3.layout
  .force()
  .charge(-480)
  .linkDistance(100)
  .size([width, height]);

//Append a SVG to the body of the html page. Assign this SVG as an object to svg
var svg = d3
  .select("#gg")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

//Read the data from data.json
//d3.json("{{ url_for('static', filename= 'assets/data/')}}{{SCHOOL_ + '.json' }}", function (data) {
d3.json("network.json", function (data) {
  force.nodes(data.nodes).links(data.links).start();

  var link = svg
    .selectAll(".link")
    .data(data.links)
    .enter()
    .append("line")
    .attr("class", "link")
    .style("stroke-width", function (d) {
      return Math.sqrt(d.value);
    });

  var node = svg
    .selectAll(".node")
    .data(data.nodes)
    .enter()
    .append("g")
    .attr("class", "node")
    .call(force.drag);

  node
    .append("circle")
    .attr("stroke", "black")
    .attr("stroke-width", 1)
    .attr("r", function (d) {
      //return d.size / 10;
      return Math.sqrt(d.size) * 3;
    })
    .style("fill", function (d) {
      return color(d.group);
    })
    .on('click', function(d,i) {
        if (event.defaultPrevented) return;
        window.open("/" + d.name)
    
      })

    

  node
        .append("text")
        .attr("dx", function (d) {
        //return d.size / 10;
        return Math.sqrt(d.size) * 3 + 5;
        })
        .attr("dy", ".35em")
        .text(function (d) {
        return d.name;
        })
        
    ;

  force.on("tick", function () {
    link
      .attr("x1", function (d) {
        return d.source.x;
      })
      .attr("y1", function (d) {
        return d.source.y;
      })
      .attr("x2", function (d) {
        return d.target.x;
      })
      .attr("y2", function (d) {
        return d.target.y;
      });

    //Changed

    d3.selectAll("circle")
      .attr("cx", function (d) {
        return d.x;
      })
      .attr("cy", function (d) {
        return d.y;
      });

    d3.selectAll("text")
      .attr("x", function (d) {
        return d.x;
      })
      .attr("y", function (d) {
        return d.y;
      });

    //End Changed
  });
});
</script>

</body>
    """

    st.markdown(html_string, unsafe_allow_html=True)
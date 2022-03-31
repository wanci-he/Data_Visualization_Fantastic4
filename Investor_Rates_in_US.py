import streamlit as st
import streamlit.components.v1 as components



# structuring the side bar menu
def sidebar_info():
    st.sidebar.subheader('Fantastic Four')
    st.sidebar.markdown("""
                   This visualization is for Data Visualization Assignment 4 .


                   **Context**: Investor Rates in US


                   **Tool Used**: Tableau embedded
                   """)
    
#the body of the page
def main():

     
    st.header('Who Becomes an Inventor in America? Important factors nurturing future inventors')
    
    st.markdown(f'Who becomes an investor in the US? is a visualization that showcases the important factors nurturing future investors across the US. It emphasizes the impact of social environmental factors in terms of parent income and geographical location on innovation during childhood or adolescence. ')

    st.markdown(f'For the map, it shows the average inventor rate (%) distribution across American states. The colors of the states indicate the levels of inventor rate. The higher the rate, the darker the color. Users can also filter the map by industries. Once the user chooses the specific industry, the map changes accordingly. Also, users can zoom in and zoom out on the map. By adjusting the range bar, users can filter the inventor rates. Also, when users click on the specific location on the map, the bar charts of parent income will change accordingly. The two charts are linked.')
    
   
    html_map = """
    <div class='tableauPlaceholder' id='viz1648757926865' style='position: relative'><noscript><a href='#'><img alt='仪表板 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;dv&#47;dvfinal2&#47;1_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='dvfinal2&#47;1_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;dv&#47;dvfinal2&#47;1_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648757926865');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    components.html(html_map, width=1000, height=500)
    
    st.markdown(f'For the box plot, it shows the overall distribution of parent income. The user can hover on the box to check the median and mean of the inventor rates by parent income quintile.')

    st.markdown(f'For the scatter plots, it illustrates the correlations between teacher student ratio and inventor rates in America. A regression line is added to indicate the relations. The user can hover on the dots to check the teacher student ratio and commuting zone information.')
    
    html_temp = """
    <div class='tableauPlaceholder' id='viz1648732607764' style='position: relative'><noscript><a href='#'><img alt='仪表板 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;A2&#47;A2_eudcation&#47;1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='A2_eudcation&#47;1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;A2&#47;A2_eudcation&#47;1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648732607764');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    components.html(html_temp, width=1000, height=500)
    

    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)

# the controller
def load_page():
    main()


    

if __name__ == "__main__":
    load_page()

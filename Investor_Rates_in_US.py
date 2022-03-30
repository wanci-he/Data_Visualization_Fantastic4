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

     
    st.write("""The below interactive dashboard displays the investor rates in US.
    """)

    html_temp = """
    <div class='tableauPlaceholder' id='viz1648677778419' style='position: relative'><noscript><a href='#'><img alt='仪表板 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;A2&#47;A2_eudcation&#47;1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='A2_eudcation&#47;1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;A2&#47;A2_eudcation&#47;1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648677778419');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    components.html(html_temp, width=1130, height=700)
    st.markdown(f'Link to the public dashboard [here](https://public.tableau.com/views/DataVisualization_16482205230750/2_1?:language=en-GB&publish=yes&:display_count=n&:origin=viz_share_link)')
    
    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)

# the controller
def load_page():
    sidebar_info()
    main()


    

if __name__ == "__main__":
    load_page()

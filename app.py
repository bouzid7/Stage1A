from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import plotly.express as px 
#"Horodateur","Adresse e-mail","App name","Rating this version","Rating all versions ","Developper",
# "N rating this version","N rating all versions","Version","Cost - basic version","Cost - upgrade version",
# "Platform","Brief description","Focus: what the app targets (select all that apply)",
# "Theoretical background/Strategies (all that apply)","Affiliations","Age group",
# "Technical aspects of app (all that apply)",
# "1. Entertainment: Is the app fun/entertaining to use? Does it use any strategies to increase engagement 
# through entertainment (e.g. through gamification)?","2. Interest: Is the app interesting to use? Does it use any strategies 
# to increase engagement by presenting its content in an interesting way?","3. Customisation: Does it provide/retain all necessary 
# settings/preferences for apps features (e.g. sound, content, notifications, etc.)?","4. Interactivity: Does it allow user input,
# provide feedback, contain prompts (reminders, sharing options, notifications, etc.)? Note: 
# these functions need to be customisable and not overwhelming in order to be perfect.","5. 
# Target group: Is the app content (visual information, language, design) appropriate for your target audience?",
# "A. Engagement mean score =","6. Performance: How accurately/fast do the app features (functions) and components
# (buttons/menus) work?","7. Ease of use: How easy is it to learn how to use the app; how clear are the menu labels/icons
# and instructions?","8. Navigation: Is moving between screens logical/accurate/appropriate/ uninterrupted; 
# are all necessary screen links present?","9. Gestural design: Are interactions (taps/swipes/pinches/scrolls) 
# consistent and intuitive across all components/screens?","B. Functionality mean score =",
# "10. Layout: Is arrangement and size of buttons/icons/menus/content on the screen appropriate or zoomable if needed?",
# "11. Graphics: How high is the quality/resolution of graphics used for buttons/icons/menus/content?","12. Visual appeal:
# How good does the app look?","C. Aesthetics mean score =","13. Accuracy of app description (in app store): Does app contain 
# what is described?","14. Goals: Does app have specific, measurable and achievable goals (specified in app store description or 
# within the app itself)?","15. Quality of information: Is app content correct, well written, and relevant to the goal/topic of 
# the app?","16. Quantity of information: Is the extent coverage within the scope of the app; and comprehensive but concise?",
# "17. Visual information: Is visual explanation of concepts – through charts/graphs/images/videos, etc. – clear, logical,
# correct?","18. Credibility: Does the app come from a legitimate source (specified in app store description or within 
# the app itself)?","19. Evidence base: Has the app been trialled/tested; must be verified by evidence (in published 
# scientific literature)?","D. Information mean score = ","20. Would you recommend this app to people who might benefit from it?",
# "21. How many times do you think you would use this app in the next 12 months if it was relevant to you?",
# "22. Would you pay for this app?","23. What is your overall star rating of the app?","A: Engagement Mean Score ",
# "B: Functionality Mean Score ","C: Aesthetics Mean Score ","D: Information Mean Score ","App quality mean Score","App subjective quality Score","1. Awareness: This app is likely to increase awareness of the importance of addressing [insert target health behaviour]","2. Knowledge: This app is likely to increase knowledge/understanding of [insert target health behaviour]","3. Attitudes: This app is likely to change attitudes toward improving [insert target health behaviour]","4. Intention to change: This app is likely to increase intentions/motivation to address [insert target health behaviour]","5. Help seeking: Use of this app is likely to encourage further help seeking for [insert target health behaviour] (if it’s required)","6. Behaviour change: Use of this app is likely increase/decrease [insert target health behaviour]"

data = pd.read_csv("MARS_handling.csv")
data = data.rename(columns=
                   {
                       
                       "App name": "AppName",
                       "Rating this version": "RatingThisVersion", 
                       "Rating all versions ": "RatingAllVersions", 
                       "N rating this version": "NRatingThisVersion",
                       "N rating all versions":"NRatingAllVersions",
                       "Cost - basic version":"CostBasicVersion",
                       "Cost - upgrade version":"CostUpgradeVersion",
                       "Age group":"AgeGroup",
                       "B. Functionality mean score =":"FunctionalityMeanScore",
                       "A. Engagement mean score =":"EngagementMeanScore",
                       "C: Aesthetics Mean Score ":"AestheticsMeanScore",
                       "D. Information mean score = ":"InformationMeanScore",
                       "App quality mean Score":"AppQualityMeanScore",
                       "App subjective quality Score":"AppSubjectiveQualityScore"
                       
                       },
                   inplace=False
                   )

app = Dash(__name__)
app.layout = html.Div(
    children=[
        
        html.Center(children="MARS Analytics"),
        html.Center(children="Analyze the MARS data applications for oceanography."),
        
        dcc.Graph(
            figure=go.Figure(data=[
                go.Scatter3d(
                    x=data["AppQualityMeanScore"],
                    y=data["CostBasicVersion"],
                    z=data["AgeGroup"],
                    mode="markers",
                    marker=dict(
                        size=8,
                        color=data["AppQualityMeanScore"],
                        colorscale="Viridis",
                        opacity=0.7,
                        colorbar=dict(title="App Quality mean score")
                    ),
                    text=data["AppName"]
                )
            ], layout=go.Layout(
                title="App Quality vs. Cost vs. Age Group",
                scene=dict(
                    xaxis_title="App quality mean Score",
                    yaxis_title="Cost - basic version",
                    zaxis_title="Age group"
                )
            ))
        ),
        dcc.Markdown("""
        **Comment**: This visualization could potentially reveal trends such as:
        
        - Whether higher quality apps tend to have a higher cost.
        - How the age group of users correlates with app quality and cost.
        """),
        
        dcc.Graph(
            figure=go.Figure(data=[
                go.Scatter3d(
                    x=data["Developper"],
                    y=data["Version"],
                    z=data["RatingThisVersion"],
                    mode="markers",
                    marker=dict(
                        size=8,
                        color=data["RatingThisVersion"],
                        colorscale="hot",
                        opacity=0.7,
                        colorbar=dict(title="Rating app")
                    ),
                    text=data["AppName"],
                )
            ], layout=go.Layout(
                title="App Ratings vs. Developer vs. Version",
                scene=dict(xaxis_title="Developer", yaxis_title="Version", zaxis_title="Rating this version")
            ))
        ),
        dcc.Markdown("""
        **Comment**: This visualization could help us to identify patterns such as:
        
        - How different developers' apps perform across different versions.
        - Whether certain versions consistently receive higher or lower ratings from users.
        """),
        dcc.Graph(
    figure=go.Figure(data=[
        go.Scatter3d(
            z=data["AppQualityMeanScore"],
            y=data["Version"],
            x=data["AppSubjectiveQualityScore"],
            mode="lines+markers",
         marker=dict(
                        size=8,
                        color=data["AppQualityMeanScore"],
                        colorscale="hot",
                        opacity=0.7,
                        colorbar=dict(title="App quality mean Score")
                    ),
         text=data["AppName"],
        )
    ], layout=go.Layout(
        title="App subjective quality Score vs. Version vs. App quality mean Score",
        scene=dict(xaxis_title="App subjective quality Score", yaxis_title="Version", zaxis_title="App quality mean Score")
    ))
),
         dcc.Markdown("""
        **Comment**: This visualization could help us to identify patterns such as:
        - the more App quality mean score and version  increase app subjective quality score increases too and vice versa .
        """),
            dcc.Graph(
    figure=go.Figure(data=[
        go.Scatter3d(
            z=data["AgeGroup"],
            y=data["EngagementMeanScore"],
            x=data["AppQualityMeanScore"],
            mode="markers",
         marker=dict(
                        size=8,
                        color=data["EngagementMeanScore"],
                        colorscale="curl",
                        opacity=0.7,
                        colorbar=dict(title="Engagement Mean Score")
                    ),
         text=data["AppName"],
        )
    ], layout=go.Layout(
        title="Engagement Mean Score vs. App quality mean Score vs. Age group",
        scene=dict(xaxis_title="Age group", yaxis_title="App quality mean score", zaxis_title="Engagement Mean Score")
    ))
),
    dcc.Markdown("""
        **Comment**:This visualization could help us uncover insights like:
        
        - Whether certain app quality aspects are more important for engaging different age groups.
        - If there's a correlation between engagement scores and specific quality aspects.
        - How engagement and quality aspects differ across various age groups.

        """)
            
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
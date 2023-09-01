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

# ------------------------------------------------------------------------------
#"App name","Rating this version","Rating all versions ","Developper",
# "N rating this version","N rating all versions","Version","Cost - basic version","Cost - upgrade version"
# B. Functionality mean score =
# A. Engagement mean score =
# C. Aesthetics mean score =
# D. Information mean score = 
# "App quality mean Score","App subjective quality Score"
# -------------------------------------------------------------------------------
import numpy as np
import pandas as pd

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
                       "B. Functionality mean score =":"FunctionalityMeanScore",
                       "A. Engagement mean score =":"EngagementMeanScore",
                       "C: Aesthetics Mean Score ":"AestheticsMeanScore",
                       "D. Information mean score = ":"InformationMeanScore",
                       "App quality mean Score":"AppQualityMeanScore",
                       "App subjective quality Score":"AppSubjectiveQualityScore"
                       },
                   inplace=True
                   )

# print(data.head())   Display the first few rows
# print(data[['AppName', 'AppSubjectiveQualityScore']])   Display specific columns
# x= data[data['AppSubjectiveQualityScore'] >10]  Display rows with a specific value
# print(x[['AppName', 'AppSubjectiveQualityScore']]) display data with condition 
# data.at[row_index, 'column_name'] = new_value   modify data 
#  data['column1'] = data['column1'] + 10         modify data 
#  data.sort_values(by='column_name', ascending=True, inplace=True)    sorting data 
# data.sort_values(by=['column1', 'column2'], ascending=[True, False], inplace=True) sorting data with multiple columns 
# data.dropna(inplace=True)   Drop rows with missing values
# data.fillna(value, inplace=True)  Fill missing values with a specific value






# Opportunate: A Data-Driven AI Solution to Canada's Immigration Crisis

Opportunate is engineered by over 7 merged datasets from StatsCan and uses Gemini's API to provide a frontend where individuals can ask the AI assistant questions and it will answer through utilizing the dataset.

## Objective:

The primary goal of this project is to figure out why many Canadians have such a paradoxical mindset regarding immigration. Some argue that it is necessary to grow the nation, while others highlight how we are unable to support it extensively due to a lack of infrastructure, high cost of living, and less job opportunities. Opportunaet provides a solution to that as it uses my engineered dataset to highlight how there are numerous economic regions within Canada that can truly benefit from immigrants and where immigrants can obtain many opportunities for their goals.

## Solution:

My project functions based of the many new columns I engineered; specifically, the **Canadian Opportunity Index.** This index provides a weightage to each economic region in Canada basedupon its cost of living and available jobs. This helps an individual considering to migrate to the nation analyze how they can get the best out of their decision through utilizing the Canadian Opportunity Index. 

## Data Analysis

My data analysis highlighted a crucial nuance that can help both the nation and individuals moving to Canada alike: rural areas & Atlantic Canada need immigrants the most. This is due to their extensively high Canadian Opportunity Index demonstrating that there is a lack of people supporting that region, and it can truly benefit from an influx of migrants. 

I further utilized Seaborn through creating heatmaps and a barplot. Specifically, the following heatmap provides us with countless insight:


<img width="4174" height="5966" alt="heat" src="https://github.com/user-attachments/assets/1abe53a8-596d-477b-aada-40e7e03a2ff2" />

Through this heatmap, we are able to highlight which economic regions excel in the corresponding columns the most, helping show the contrast between rural and urban regions in Canada.

Moreover, we can also see how urban regions rank in comparison to rural regions in Canada according to the Canadian Opportunity Index:


<img width="3567" height="2968" alt="opportunity_index_bar" src="https://github.com/user-attachments/assets/aa434ccc-69e2-4259-9ff0-380a736dfe94" />

Like the previous diagram, this barplot further highlights how rural regions are the ones that need immigration extensively more than urban ones within Canada.

## Feature Engineering:

The raw data from Statistics Canada gave much insight into the regions yet lacked correlation with how this information could be benefitial for individuals and be utilized by my target group: immigrants. To help tackle this, I engineered over 12 new columns to truly help answer the question "Where should an immigrant move?" 

### Derived features

Job_Growth_Potential: Calculated through finding the ratio between the Job_Vacancy for Q3 2025 to the Payroll_Employees in Q3 2025. This column helps highlight whether a region truly holds untouched opportunities for an individual that can be beneficial to a person trying to survive in the nation.

Net_Migration_Rate: Calculated through finding the ratio between interprovincial migration and population. This derived column further signifies whether a community is growing, since the larger a community is getting the more likely it is to excel in the future and benefit an immigrant.

Natural_Growth_Rate: Calculated through finding the ratio between the amount of births in a region to population. The larger birth rate represents a higher living lifestyle, a growing population, and a region that can support families. 

Delta_Immigrant_Per_Capita: Calculated through finding the ratio between the change in the number of immigrants in the region to the overall population. This shows that if people are immigrating to a region, then it is more likely to hold opportunities for other immigrants as well.

Immigrant_Density: Calculated through finding the ratio in the change of immigrants to the population. Highlights whether a region has a large immigrant community that can support other immigrants as well. 

Lastly, I used MinMaxScaler to normalize all these values and other columns already within the dataset to between 0-1 so that their weightage would be equal and they could equally contribute to the Canadian Opportunity Index.

## Canadian Opportunity Index:

All data and derived columns contribute to this weightage system and act as the final composite score, the pillar of the dataset:

Canadian_Opportunity_Index = (
    # Employment — 40%
    Job_Growth_Potential * 0.40 +

    # Migration Signals — 20%
    Net_Migration_Rate * 0.12 +
    Delta_Immigrant_Per_Capita * 0.08 +

    # Affordability — 25%
    (1 - Shelter_Expenditure_Scaled) * 0.12 +
    (1 - Food_Expenditure_Scaled) * 0.05 +
    (1 - Transportation_Expenditure_Scaled) * 0.05 +
    Public_Transport_Expenditure_Scaled * 0.03 +

    # Community & Quality of Life — 15%
    Natural_Growth_Rate * 0.05 +
    (1 - Healthcare_Expenditure_Scaled) * 0.05 +
    Education_Expenditure_Scaled * 0.05
)

This value is then normalized to 0-1 using MinMaxScaler, with 1 representing the best region for Immigrants.

## Conclusion

The merged dataset contains over 72 economic regions, 57 columns, and combines over seven StatsCan datasets. 

**Resources for the dataset:**

https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=1710015101
https://www150.statcan.gc.ca/t1/tbl1/en/tv.actionpid=1410039801&pickMembers%5B0%5D=2.2&cubeTimeFrame.startMonth=07&cubeTimeFrame.startYear=2024&cubeTimeFrame.endMonth=07&cubeTimeFrame.endYear=2025&referencePeriods=20240701%2C20250701
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710015001
https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=1110022201


Overal, this project taught me a lot regarding Data Analysis & Data Engineering, and I hope to continue exploring these fields!

import pandas as pd
import streamlit as st
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123kam456@localhost/project1")
conn = engine.connect()

st.title('1ST PROJECT Global Seismic Trends')
opt = st.selectbox(
    'Choose Case Study',
    ('Q1','Q2','Q3','Q5','Q6','Q7','Q8','Q9','Q10',
     'Q11','Q13','Q14','Q15','Q16','Q18','Q19','Q20',
     'Q21','Q22','Q23','Q24','Q25','Q26','Q27','Q28','Q30'))

if opt=='Q1':
    st.write("Top 10 strongest EQ")
    q1="""select place,mag from earthquakes_1  order by mag desc limit 10; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q2":
    st.write("Top 10 deepest EQ")
    q1="""select place,depth_km from earthquakes_1 order by depth_km  desc limit 10; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q3":
    st.write("shallow EQ<50km and mag>7.5")
    q1="""select place,depth_km,mag from earthquakes_1  where depth_km<50 and mag>7.5 ; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q5":
    st.write("Average magnitude per magnitude type")
    q1="""select mag_Type,avg(mag) as avg from earthquakes_1 group by mag_Type; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
   
elif opt=="Q6":
    st.write("Year with most EQ")
    q1="""select year(time) as year,count(*) as total 
        from earthquakes_1
        group by year(time)
        order by total desc; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q7":
    st.write("Month with highest number of EQ")
    q1="""select month(time) as month,count(*) as total 
        from earthquakes_1
        group by month(time)
        order by total desc limit 1; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)


elif opt=="Q8":
    st.write("Day of week with most EQ")
    q1="""select dayname(time) as day_of_week,count(*) as total 
        from earthquakes_1 
        group by dayname(time) 
        order by total desc; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q9":
    st.write("Count of EQ hour of day")
    q1="""select hour(time) as hour_day,count(*) as total 
            from earthquakes_1 
            group by hour(time) 
            order by total desc; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q10":
    st.write("Most active reporting network")
    q1="""select net as active_network,count(*) as total  
        from earthquakes_1
        group by net 
        order by count(*)  desc limit 1; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q11":
    st.write("Top 5 place with highest casuality")
    q1="""select place,max(felt) as high_casuality 
        from earthquakes_1
        group by (place) 
        order by high_casuality desc limit 5;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q13":
    st.write("Top 5 place with highest casuality")
    q1="""select alert as avg_ecomnomic_loss,count(*) as total 
        from earthquakes_1 
        group by alert;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q14":
    st.write("Count of reviewed vs automatic EQ")
    q1="""select status,count(*) as total
        from earthquakes_1
        group by status;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)

elif opt=="Q15":
    st.write("Count of EQ type")
    q1="""select type,count(*) as total
        from earthquakes_1
        group by type ;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)


elif opt=="Q16":
    st.write("No.of EQ by data type")
    q1="""select types,count(*) as total
        from earthquakes_1
        group by types;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q18":
    st.write("Event with high station coverage")
    q1="""select nst from earthquakes_1
        where nst>50;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q19":
    st.write("No.of tsunamis triggered by year")
    q1="""select year(time) as year,count(*) as tsunamis 
        from earthquakes_1
        where tsunami=1
        group by year(time);"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q20":
    st.write("Count of EQ by alert level")
    q1="""select alert,count(*) as numberof_eq from earthquakes_1 
        group by alert;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q21":
    st.write("Top 5 countries with highest avg magnitude  of EQ for past 10 yaer")
    q1="""select place,avg(mag) as highest_avg_mag from earthquakes_1 
        group by place
        order by avg(mag) desc limit 10;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q22":
    st.write("Country experiance both shallow and deep EQ within the same month")
    q1="""select place from earthquakes_1
        group by place,year(time),month(time)
        having  sum(depth_km < 70)  and sum(depth_km > 300) ;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q23":
    st.write("Compute year over year growth rate in otal no.of EQ")
    q1="""select  year,total,
            lag(total) over (order by year) AS previous_year,
            round(((total - lag(total) over (order by year)) / lag(total) over (order by year)) * 100, 2) as growth_rate
        from (
            select year(time) as year, count(*) AS total
            from earthquakes_1
            group by year
        ) as yearly;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q24":
    st.write("List 3 most sesmically region by combine both frequency and avg mag")
    q1="""select place,
        count(*) as frequency,
        avg(mag) as avg_mag,
        (count(*)* (avg(mag))) as score from earthquakes_1
        group by place
        order by score desc limit 3;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q25":
    st.write("For each country calculate avg.depth of EQ within +-5")
    q1="""select place,avg(depth_km) as avg_depth from earthquakes_1 
        where latitude between -5 and +5
        group by place;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q26":
    st.write("country having highest ratio of shallow to deep EQ")
    q1="""select place,
        sum(depth_km < 70)as shallow,
        sum(depth_km > 300)as deep,
        sum(depth_km < 70) / nullif(sum(depth_km > 300), 0) AS ratio
        from  earthquakes_1
        group by place
        order by ratio desc;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q27":
    st.write("Find avg mag difference between EQ with tsunami alert and those without")
    q1="""select
            (select AVG(mag) from earthquakes_1 where tsunami = 1) as tsunami_avg,
            (select AVG(mag) from earthquakes_1 where tsunami = 0) as no_tsunami_avg,
            (select AVG(mag) from earthquakes_1 where tsunami = 1) -
            (select AVG(mag) from earthquakes_1 where tsunami = 0) as difference; """
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q28":
    st.write("Event with lowest data reliability")
    q1=""" select round(gap,2) as gap,rms from earthquakes_1
        order by gap desc,rms limit 20;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
elif opt=="Q30":
    st.write("Region with highest frequency of deep-focus EQ")
    q1="""select place,count(*) as deep_eq from earthquakes_1
         where depth_km>300
        group by place
        order by deep_eq desc;"""
    df = pd.read_sql(q1, conn)
    st.dataframe(df)
   



    




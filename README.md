# dive_in_shark_tank

Today we will work on the dataset taken from the kaggle website.
The dataset that we will dive into today would be on the “Shark Tank” TV show.
For some of you, who aren’t similar with the TV show “Shark Tank” series, the show is a show where entrepreneurs present their product or service to a panel of lenders or “sharks” for money. Then, they do a presentation in front of the panel of sharks. After the presentation, the entrepreneurs will seek money in return for a percentage of their company.

This mainstreaming of angel investment (  = a high net worth individual who invests their own money along with their time) in this entertaining format , gives us a bigger picture of how we can learn from the discussion of equity, funding, valuation and growth strategies.

Now, Let’s see a glimpse of the **angel investor** process

This data presents us with useful information about the show series taken on the ABC channel.
As we can see below, the dataset includes 18 columns 450 rows ( matrix of 450 *18 ). Each row gives us information about the next entrepreneur who is willing to succeed in the big world,


Here are the columns names:
'Deal'
'description'
 'Episode'
 'Category'
 'Entrepreneurs'
 'Location',
 'website' 
'Askedfor'
 'Exchangeforstake'
 'Valuation'
 'Season'
 'shark1', 'shark2' 'shark3' 'shark4' 'shark5'
 'Title'
 'Episode_season',
 'multiple_entreprenuers'







In the next chart I would like to know the number of investments made by the sharks in each season. Therefore, I would reveal this element and illustrate it by using  the pie chart.
We can notice, there is an increase in the number of investments made by the sharks as the TV show progressed over the seasons.
As we can see, the number of investments taken in the first and second season was 27 and 19 .
And on the opposite side, in the fifth season  and sixth season we can notice a big increase in numbers : 61 and 63.
Seasons 1+2  = 27+19 = 46
Seasons 5+6 = 61 + 63 = 124

In the next chart I want to dive into the information about the investing part of each shark getting into their pocket in order to invest in each entrepreneur project.
We can see here below in every waffle diagram the amount of money a specific shark invested in a relevant season vs the rest of investments made by the rest of the sharks.


![image](https://user-images.githubusercontent.com/28948369/234967869-da3aeb9b-3e4a-4710-9ff1-7a20b988f1ff.png)





# Analysis the new data 
As we go over the multiindex data we can notice an hierarchical indexing under the header of “ASK” and “DEAL” multiindex.
The “ASK” columns presents all the aspects ( Amount, acuity and valuation ) given by the entrepreneurs as they give their peches offer to the sharks.
The “DEAL”columns present the same aspects, but after a negotiation between the entrepreneurs and the sharks. Usually the sharks will try to “cut off “ the asking price valuation or reduce the amount of money they are willing to pay, In order to hedge their investments.

Therefore, I decided to drill down, and to focus on the negotiation part.

As we go over the multiindex data we can notice an hierarchical indexing under the header of “ASK” and “DEAL” multiindex.
The “ASK” columns presents all the aspects ( Amount, acuity and valuation ) given by the entrepreneurs as they give their peches offer to the sharks.
The “DEAL”columns present the same aspects, but after a negotiation between the entrepreneurs and the sharks. Usually the sharks will try to “cut off “ the asking price valuation or reduce the amount of money they are willing to pay, In order to hedge their investments.

Therefore, I decided to drill down, and to focus on the negotiation part.


The chart below displays the number of deals made by each shark in the panel over the years during entrepreneur presentations. Specifically, we are interested in determining the number of closed deals made by each shark, categorized by gender (male and female). For instance, Kavin had the highest number of deals with 132, this number doesn’t excluding those made with multiple entrepreneurs. Out of these, 93 deals (70.4%) were with male entrepreneurs, while the remaining 39 (29.6%) were with female entrepreneurs.

![image](https://github.com/AnalyticsForPleasure/dive_into_shark_tank/assets/28948369/3fa16a8b-5c46-4e9a-9d3c-bb828af803aa)


The next thing we are willing to find out is out the investments made ny each shark upon the entrepreneurs. This mean we ae willing to know which shark preference to invest apon a solo entrepreneurs VS  multiple entreprenuers.





![image](https://user-images.githubusercontent.com/28948369/236793307-0a116837-577a-4398-abc6-d9108eb23819.png)


The next thing that we would like to dive into is to find out for each deal which has been closed by each shark, what was the amount of equity settled during the negotiation process between the entrepreneur VS the shark. 
Therefore, we decided to add another element to the equation - for each closed deal by each  shark we will divide the deals by the gender of the entrepreneur. For example : Mark Cuban, during 10 seasons of the show that has been aired on TV, he made 68 investment deals with entrepreneurs over the show. As we can notice below, The average equity (%) for a male entrepreneur was 28.6%, while the average equity (%) for a female entrepreneur was 26.4%.

![image](https://github.com/AnalyticsForPleasure/dive_into_shark_tank/assets/28948369/ecc19377-a3da-41f0-b224-ffd21aab5f29)




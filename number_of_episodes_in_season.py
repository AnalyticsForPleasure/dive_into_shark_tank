import numpy as np
import pandas as pd
import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap # in order to add the gradient color

# **************************************************************************************************************
# Function  name: get_number_of_investments_each_season_over_the_years
# input:
# return value:
# ****************************************************************************************************************
def get_number_of_investments_each_season_over_the_years(df):
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    res = all_the_deals_closed['Season'].value_counts().to_frame()
    res = res.reset_index(level=0)
    res.rename(columns={res.columns[0]: 'season_number'}, inplace=True)
    res.rename(columns={res.columns[1]: 'Amount_of_investments_over_each_season'}, inplace=True)
    res['season_number'] = res['season_number'].apply(lambda x: int(x))
    res.sort_values(by='season_number', inplace=True, ascending=True)
    dfi.export(res,'result_investment_per_season.png')
    print('*')

    return res
# **************************************************************************************************************
# Function  name: creating a gradient area bar for the number of investments made during the seasons
# input:
# return value:
# ****************************************************************************************************************
def creating_gradient_area_bar_chart_for_the_investments_over_the_seasons(table):
    print('*')
    number_of_season = list(table.loc[:,'season_number'])
    number_of_investments_over_each_season = list(table.loc[:,'Amount_of_investments_over_each_season'])

    # Adding blue gradient color:
    x=np.arange(1,11,1)
    y1= np.array(number_of_investments_over_each_season)
    y2= np.repeat(0, 10)
    print('*')
    cm1 = LinearSegmentedColormap.from_list('Temperature Map', ['navy','skyblue'])
    polygon = plt.fill_between(x, y1, y2, lw=0, color='none')
    xlim = (x.min(), x.max())
    ylim = plt.ylim()
    verts = np.vstack([p.vertices for p in polygon.get_paths()])
    gradient = plt.imshow(np.linspace(0, 1, 256).reshape(-1, 1), cmap=cm1, aspect='auto', origin='lower',
                          extent=[verts[:, 0].min(), verts[:, 0].max(), verts[:, 1].min(), verts[:, 1].max()])
    gradient.set_clip_path(polygon.get_paths()[0], transform=plt.gca().transData)

    plt.plot(number_of_season,
             number_of_investments_over_each_season,
             color="Gray",
             alpha=0.6,
             linewidth=3)
    plt.tick_params(labelsize=12)
    plt.xticks(number_of_season, number_of_season)

    plt.xlabel('Season Number', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.ylabel('Number of Investments', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.ylim(bottom=0)
    plt.title('Number of investments made during each season' ,fontsize=22, weight='bold',fontname='Franklin Gothic Medium Cond')
    print('*')
    plt.xlim(xlim)
    plt.ylim(ylim)

# annotate
    # for x, v in table.iterrows():
    #     cs = v.cumsum()[::-1]  # get the cumulative sum of the row and reverse it to provide the correct y position
    #     for i, a in enumerate(v[::-1]):  # reverse the row values for the correct annotation
    #         plt.annotate(text=f'${a:0.2f}', xy=(x, cs[i]))

    # Displaying the chart
    plt.show()

if __name__ == '__main__':

    pd.set_option('display.max_rows', 900)

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')  # Ten seasons

    my_result =get_number_of_investments_each_season_over_the_years(df)
    creating_gradient_area_bar_chart_for_the_investments_over_the_seasons(my_result)
    print('*')





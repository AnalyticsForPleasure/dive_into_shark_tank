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
# Example 4: Make Negative Numbers red + positive number in green
# red if negative
def color_negative_red(value):
    if isinstance(value, str) :
        color = 'black'
        return 'color: %s' % color
    if isinstance(value, float):
        if value >= 0:
            color = "green"
            return 'color: %s' % color
        if value < 0:
            color = "red"

            return 'color: %s' % color
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
    res.rename(columns={res.columns[1]: 'Amount of investments made'}, inplace=True)
    res['season_number'] = res['season_number'].apply(lambda x: int(x))
    res.sort_values(by='season_number', inplace=True, ascending=True)
    print('*')
    # Creating a column which calculate the diff of each row:
    res['Percentage Difference'] = res['Amount of investments made'].pct_change() * 100
    res['Percentage Difference'] =res['Percentage Difference'].apply(lambda x: "{0:.2f}".format(x))
    res.reset_index(inplace=True)
    res['Percentage Difference'][0]= '0'
    print('*')

    res = res.iloc[:5,]
    print('*')

    res['Percentage Difference'] = res['Percentage Difference'].astype(float)
    print('*')

    d = dict.fromkeys(res.select_dtypes('float').columns, "{:.2f}" + '%')
    style_by_coloring_negative_red = res.style.applymap(color_negative_red).format(d)#.hide_index()
    dfi.export(style_by_coloring_negative_red, filename='c:/Users/Gil/PycharmProjects/dive_into_shark_tank/chart_1_readme/images/style_by_coloring_negative_red_part_2.png')
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
    cm1 = LinearSegmentedColormap.from_list('Temperature Map', ['navy','skyblue']) # We can add here several colors
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

    #Adding 2 vertical lines for each season:
    vertical_lines = np.arange(2, 10, 1)+0.03
    for vline in vertical_lines:
        plt.axvline(x=vline, color='White',linestyle=':')

    vertical_lines_2 = np.arange(2, 10, 1)-0.03
    for vline_2 in vertical_lines_2:
        plt.axvline(x=vline_2, color='White',linestyle=':')



    plt.xlabel('Season Number', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.ylabel('Number of Investments', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.ylim(bottom=0)
    plt.title('How many investments were made for each season of the TV show?' ,fontsize=26, weight='bold',fontname='Franklin Gothic Medium Cond')
    print('*')
    plt.xlim(xlim)
    plt.ylim(ylim)

    # Adding annotation values
    offset_x = 0.08
    offset_y = 0.75
    fontdict_input = {'fontsize': 13, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'Gray'}
    for season,amount_investment in zip(number_of_season,number_of_investments_over_each_season):
        plt.text(x=season - offset_x, y=amount_investment + offset_y, s=amount_investment, ha='left', va='bottom', fontdict=fontdict_input)

    # settings
    plt.rcParams["figure.figsize"] = (21, 8)
    # Save the image
    plt.savefig('area_chart.jpg',dpi=450, bbox_inches='tight')
    # settings


    # Displaying the chart
    plt.show()

if __name__ == '__main__':

    pd.set_option('display.max_rows', 900)

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')  # Ten seasons
    column_headers = list(df.columns.values)
    print('*')

    my_result =get_number_of_investments_each_season_over_the_years(df)
    #creating_gradient_area_bar_chart_for_the_investments_over_the_seasons(my_result)
    print('*')





import numpy as np
import pandas as pd
import dataframe_image as dfi



if __name__ == '__main__':


    df = pd.DataFrame({'A': [1,-2,3,-4,5,-6,7,-8,9,-10],
                       'B': np.random.rand(10),
                       'C': np.arange(10),
                       'D': [-5,np.nan,5,np.nan,-5,5,-5,np.nan,np.nan,5]})
    df


########################################################################################################################
    # Example 1: Remove row indices
    df_1 = df.style.hide(axis="index")
    dfi.export(df_1, filename='hide_index.png')



########################################################################################################################
    # Example 2: Format Table
    df_2 = df.style.set_properties(**{'background-color': 'dodgerblue',
                                      'color': 'white',
                                      'border-color': 'white',
                                      'border-width': '1px',
                                      'border-style': 'solid'})

    dfi.export(df_2, filename='output_images/Example_Format Table.png')

########################################################################################################################

    # Example 3: Highlight Specific number under constrains
    def highlight_number(number):
        criteria = number == 7

        return ['background-color: springgreen' if i else '' for i in criteria] # Color kind - springgreen

    df_3 = df.style.apply(highlight_number)

    dfi.export(df_3, filename='output_images/Highlight_Specific_Number.png')

########################################################################################################################

    # Example 4: Make Negative Numbers Red
    # red if negative
    def color_negative_red(number):
        # returns a string with the css property 'color: red' for negative strings, black otherwise
        color = 'red' if number < 0 else 'black'
        return f'color: {color}'

    # looks at each value to find negative numbers
    df_4 =df.style.applymap(color_negative_red)
    dfi.export(df_4, filename='output_images/Make_Negative_Numbers_Red.png')

########################################################################################################################

    # Example 5: Highlight NAN
    df_5 =df.style.highlight_null(null_color='red')
    dfi.export(df_5, filename='output_images/Highlight_NAN.png')


########################################################################################################################

    # Example 8:Size Bars

    # size of bar corresponds to number in cell - in the specific column
    highlight = df.style.bar(subset=['A', 'B', 'C'], color='yellow')
    #highlight = df.style.bar(subset=['B'], color='yellow') <-- we can choose only one column

    # to html with style
    html = highlight.render()
    with open('output_images/highlight.html', 'w') as f:
        f.write(html)

    df_6 = highlight
    dfi.export(df_6, filename='../size_of_bar_corresponds.png')

########################################################################################################################

    # Example 7: Highlight Max

    # highlight max
    # 0 = down the rows for each column
    # 1 = across the columns for each row
    df_7 =df.style.highlight_max(axis=0)
    dfi.export(df_7, filename='output_images/max_value_colored.png')


########################################################################################################################

    # Example 8: Highlight Min

    # 0 = down the rows for each column
    # 1 = across the columns for each row
    df_8 =df.style.highlight_min(axis=0)
    dfi.export(df_8, filename='output_images/min_value_colored.png')

########################################################################################################################

    # Example 9: painting relevant columns highlighter

    def relevant_columns_highlighter(x):
        my_style = "background-color: #1E90FF; " \
                   "color: white; " \
                   "font-weight: bold;"
        return [my_style] * len(x)

    df_9 = df.style.apply(func=relevant_columns_highlighter, subset=['A', 'D'])

    dfi.export(df_9, filename='output_images/highlight_columns.png')

########################################################################################################################

    # Example 10: mean_highlighter

    # Color the cell red if the value is less than or equal to the mean
    # Color the cell green if the value is greater than the mean
    # Make the text white and bold in cases

    def mean_highlighter(x):
        # lt = less than
        style_lt = "background-color: #EE2E31; " \  
                   "color: white; " \
                   "font-weight: bold;"
        # gt =greater than
        style_gt = "background-color: #31D843; " \
                    "color: white; " \
                    "font-weight: bold;"
        gt_mean = x > x.mean()
        return [style_gt if i else style_lt for i in gt_mean]


    df_10 = df.style.apply(mean_highlighter)
    dfi.export(df_10, filename='output_images/mean_highlighter.png')


########################################################################################################################

    # Example 11: bold column  + color column + removing index column

    def relevant_columns_highlighter(x):
        my_style = "color: #1E90FF;" \
                   "font-weight: bold;"
        return [my_style] * len(x)

    df_11 = df.style.apply(func=relevant_columns_highlighter, subset=['C']).hide_index()
    dfi.export(df_10, filename='output_images/bold_color_without_index.png')
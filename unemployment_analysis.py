import pandas as pd
import matplotlib.pyplot as plt
import folium




# Showing figure and save figure for Estimated Unemployment Rate and calling this function by unemployment_analysis_function()
def show_fig_estimated_unemployment_rate(unique_data_df):
    """
        This function shows a figure of the Estimated Unemployment Rate data and saves it as a PNG file.
        
        Args:
            data_df (DataFrame): The DataFrame containing the Estimated Unemployment Rate data.
    """
    # Plot the data in bar diagram with x-axis as Region and y-axis as Minimum Estimated Unemployment Rate
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Minimum Estimated Unemployment Rate'])
    plt.xlabel('Region')
    plt.ylabel('Minimum Estimated Unemployment Rate')
    plt.title('Minimum Estimated Unemployment Rate by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Minimum-Estimated-Unemployment-Rate-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Minimum Estimated Unemployment Rate
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Minimum Estimated Unemployment Rate'])
    plt.xlabel('States')
    plt.ylabel('Minimum Estimated Unemployment Rate')
    plt.title('Minimum Estimated Unemployment Rate by States')
    plt.xticks(rotation=90)
    plt.savefig('Minimum-Estimated-Unemployment-Rate-by-States.png')
    plt.show()


    # Plot the data in bar diagram with x-axis as Region and y-axis as Average Estimated Unemployment Rate
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Average Estimated Unemployment Rate'])
    plt.xlabel('Region')
    plt.ylabel('Average Estimated Unemployment Rate')
    plt.title('Average Estimated Unemployment Rate by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Average-Estimated-Unemployment-Rate-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Average Estimated Unemployment Rate
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Average Estimated Unemployment Rate'])
    plt.xlabel('States')
    plt.ylabel('Average Estimated Unemployment Rate')
    plt.title('Average Estimated Unemployment Rate by States')
    plt.xticks(rotation=90)
    plt.savefig('Average-Estimated-Unemployment-Rate-by-States.png')
    plt.show()


    # Plot the data in bar diagram with x-axis as Region and y-axis as Maximum Estimated Unemployment Rate
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Maximum Estimated Unemployment Rate'])
    plt.xlabel('Region')
    plt.ylabel('Maximum Estimated Unemployment Rate')
    plt.title('Maximum Estimated Unemployment Rate by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Maximum-Estimated-Unemployment-Rate-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Maximum Estimated Unemployment Rate
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Maximum Estimated Unemployment Rate'])
    plt.xlabel('States')
    plt.ylabel('Maximum Estimated Unemployment Rate')
    plt.title('Maximum Estimated Unemployment Rate by States')
    plt.xticks(rotation=90)
    plt.savefig('Maximum-Estimated-Unemployment-Rate-by-States.png')
    plt.show()


# Showing figure and save figure for Estimated Employed and calling this function by unemployment_analysis_function()
def show_fig_estimated_employed(unique_data_df):
    """
    This function shows a figure of the Estimated Employed data and saves it as a PNG file.
    
    Args:
        df (DataFrame): The DataFrame containing the Estimated Employed data.
    """
        
    # Plot the data in bar diagram with x-axis as Region and y-axis as Minimum Estimated Employed
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Minimum Estimated Employed'])
    plt.xlabel('Region')
    plt.ylabel('Minimum Estimated Employed')
    plt.title('Minimum Estimated Employed by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Minimum-Estimated-Employed-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Minimum Estimated Employed
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Minimum Estimated Employed'])
    plt.xlabel('States')
    plt.ylabel('Minimum Estimated Employed')
    plt.title('Minimum Estimated Employed by States')
    plt.xticks(rotation=90)
    plt.savefig('Minimum-Estimated-Employed-by-States.png')
    plt.show()


    # Plot the data in bar diagram with x-axis as Region and y-axis as Average Estimated Employed
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Average Estimated Employed'])
    plt.xlabel('Region')
    plt.ylabel('Average Estimated Employed')
    plt.title('Average Estimated Employed by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Average-Estimated-Employed-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Average Estimated Employed
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Average Estimated Employed'])
    plt.xlabel('States')
    plt.ylabel('Average Estimated Employed')
    plt.title('Average Estimated Employed by States')
    plt.xticks(rotation=90)
    plt.savefig('Average-Estimated-Employed-by-States.png')
    plt.show()


    # Plot the data in bar diagram with x-axis as Region and y-axis as Maximum Estimated Employed
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Maximum Estimated Employed'])
    plt.xlabel('Region')
    plt.ylabel('Maximum Estimated Employed')
    plt.title('Maximum Estimated Employed by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Maximum-Estimated-Employed-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Maximum Estimated Employed
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Maximum Estimated Employed'])
    plt.xlabel('States')
    plt.ylabel('Maximum Estimated Employed')
    plt.title('Maximum Estimated Employed by States')
    plt.xticks(rotation=90)
    plt.savefig('Maximum-Estimated-Employed-by-States.png')
    plt.show()


# Showing figure and save figure for Estimated Employed and calling this function by unemployment_analysis_function()
def show_fig_estimated_labour_participation_rate(unique_data_df):
    """
    This function shows a figure of the Estimated Labour Participation Rate data and saves it as a PNG file.
    
    Args:
        df (DataFrame): The DataFrame containing the Estimated Labour Participation Rate.
    """
        
    # Plot the data in bar diagram with x-axis as Region and y-axis as Minimum Estimated Labour Participation Rate
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Minimum Estimated Labour Participation Rate'])
    plt.xlabel('Region')
    plt.ylabel('Minimum Estimated Labour Participation Rate')
    plt.title('Minimum Estimated Labour Participation Rate by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Minimum-Estimated-Labour-Participation-Rate-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Minimum Estimated Labour Participation Rate
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Minimum Estimated Labour Participation Rate'])
    plt.xlabel('States')
    plt.ylabel('Minimum Estimated Labour Participation Rate')
    plt.title('Minimum Estimated Labour Participation Rate by States')
    plt.xticks(rotation=90)
    plt.savefig('Minimum-Estimated-Labour-Participation-Rate-by-States.png')
    plt.show()


    # Plot the data in bar diagram with x-axis as Region and y-axis as Average Estimated Labour Participation Rate
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Average Estimated Labour Participation Rate'])
    plt.xlabel('Region')
    plt.ylabel('Average Estimated Labour Participation Rate')
    plt.title('Average Estimated Labour Participation Rate by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Average-Estimated-Labour-Participation-Rate-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Average Estimated Labour Participation Rate
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Average Estimated Labour Participation Rate'])
    plt.xlabel('States')
    plt.ylabel('Average Estimated Labour Participation Rate')
    plt.title('Average Estimated Labour Participation Rate by States')
    plt.xticks(rotation=90)
    plt.savefig('Average-Estimated-Labour-Participation-Rate-by-States.png')
    plt.show()


    # Plot the data in bar diagram with x-axis as Region and y-axis as Maximum Estimated Labour Participation Rate
    # showing by Region wise
    plt.bar(unique_data_df['Region'], unique_data_df['Maximum Estimated Labour Participation Rate'])
    plt.xlabel('Region')
    plt.ylabel('Maximum Estimated Labour Participation Rate')
    plt.title('Maximum Estimated Labour Participation Rate by Regions')
    plt.xticks(rotation=90)
    plt.savefig('Maximum-Estimated-Labour-Participation-Rate-by-Regions.png')
    plt.show()

    # Plot the data in bar diagram with x-axis as States and y-axis as Maximum Estimated Labour Participation Rate
    # showing by states wise
    plt.bar(unique_data_df['States'], unique_data_df['Maximum Estimated Labour Participation Rate'])
    plt.xlabel('States')
    plt.ylabel('Maximum Estimated Labour Participation Rate')
    plt.title('Maximum Estimated Labour Participation Rate by States')
    plt.xticks(rotation=90)
    plt.savefig('Maximum-Estimated-Labour-Participation-Rate-by-States.png')
    plt.show()

    
# showing data visualization with map
def data_visualization_with_map(unique_data_df):
    """
    This function shows a data visualization with map and save it as a state_map.html file.
    
    Args:
        df (DataFrame): The DataFrame containing the all data.
    """

    # Create a folium map centered at the mean latitude and longitude of the dataset
    UNEMPLOYMENT_MAP = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    # Add click method to display state information
    for index, row in unique_data_df.iterrows():
        state_info = f"<h5><b>Region: {row['Region']}</b></h3>\
            <h6><b>State: {row['States']}</b></h4>\
            <strong>Min Unemployment Rate</strong> <b>{row['Minimum Estimated Unemployment Rate']:.2f}</b><br>\
            <strong>Avg Unemployment Rate:</strong> <b>{row['Average Estimated Unemployment Rate']:.2f}</b><br>\
            <strong>Max Unemployment Rate:</strong> <b>{row['Maximum Estimated Unemployment Rate']:.2f}</b><br>\
            <strong>Min Employed:</strong> <b>{row['Minimum Estimated Employed']:.2f}</b><br>\
            <strong>Avg Employed:</strong> <b>{row['Average Estimated Employed']:.2f}</b><br>\
            <strong>Max Employed:</strong> <b>{row['Maximum Estimated Employed']:.2f}</b><br>\
            <strong>Min Labour Participation Rate:</strong> <b>{row['Minimum Estimated Labour Participation Rate']:.2f}</b><br>\
            <strong>Avg Labour Participation Rate:</strong> <b>{row['Average Estimated Labour Participation Rate']:.2f}</b><br>\
            <strong>Max Labour Participation Rate:</strong> <b>{row['Maximum Estimated Labour Participation Rate']:.2f}</b>"
        
        folium.Marker(
            location=[row['longitude'],row['latitude']],
            tooltip=row['States'],
            popup=folium.Popup(state_info, max_width=300)
        ).add_to(UNEMPLOYMENT_MAP)

    
    # UNEMPLOYMENT_MAP.save('state_map.html')  # Save the map as an HTML file
    # Display the map
    UNEMPLOYMENT_MAP.show_in_browser()
    



# main function for data analysis and visualization
def unemployment_analysis_function():
    df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
    print("\nFirst 5 rows of the dataset: \n")
    print(df.head())
    print("\nLast 5 rows of the dataset: \n")
    print(df.tail())
    print("\nShape of the dataset: \n")
    print(df.shape)
    print("\nDescriptive statistics of the dataset: \n")
    print(df.describe())
    print("\nInformation about the dataset: \n")
    print(df.info())
    print("\nNull values in the dataset: \n")
    print(df.isnull().sum())
    print("\nData types of the dataset: \n")
    print(df.dtypes)

    df.columns= ["States", "Date", "Frequency",  
            "Estimated Unemployment Rate", "Estimate Employed",  
            "Estimated Labour Participation Rate", "Region",  
            "longitude", "latitude"] 
    
    
    # Calculate mean for each group and create new columns
    df["Minimum Estimated Unemployment Rate"] = df.groupby('States')['Estimated Unemployment Rate'].transform('min')
    df['Average Estimated Unemployment Rate'] = df.groupby('States')['Estimated Unemployment Rate'].transform('mean')
    df['Maximum Estimated Unemployment Rate'] = df.groupby('States')['Estimated Unemployment Rate'].transform('max')

    df["Minimum Estimated Employed"] = df.groupby('States')["Estimate Employed"].transform('min')
    df['Average Estimated Employed'] = df.groupby('States')["Estimate Employed"].transform('mean')
    df['Maximum Estimated Employed'] = df.groupby('States')["Estimate Employed"].transform('max')

    df["Minimum Estimated Labour Participation Rate"] = df.groupby('States')["Estimated Labour Participation Rate"].transform('min')
    df['Average Estimated Labour Participation Rate'] = df.groupby('States')["Estimated Labour Participation Rate"].transform('mean')
    df['Maximum Estimated Labour Participation Rate'] = df.groupby('States')["Estimated Labour Participation Rate"].transform('max')
    

    # Create a new DataFrame without duplicate rows
    unique_data_df = df.drop_duplicates(subset=['States']).reset_index(drop=True)

    # List of columns to drop
    columns_to_drop = ["Date", "Frequency",  
            "Estimated Unemployment Rate", "Estimate Employed",  
            "Estimated Labour Participation Rate",]  # Add columns you want to drop

    # Drop unnecessary columns
    unique_data_df = unique_data_df.drop(columns=columns_to_drop)
    print("\nShape of the dataset after dropping unnecessary columns: \n")
    print(unique_data_df.shape)
    print("\nUnique data(without duplicate rows) with new columns and dropped unnecessary columns: \n")
    print(unique_data_df.head())

    # Save the updated DataFrame to a new CSV file
    # unique_data_df.to_csv("updated_data.csv", index=False)



    # Show figure and save figure for Estimated Unemployment Rate 
    show_fig_estimated_unemployment_rate(unique_data_df)

    # Show figure and save figure for Estimated Employed
    show_fig_estimated_employed(unique_data_df)

    # Show figure and save figure for Estimated Labour Participation Rate
    show_fig_estimated_labour_participation_rate(unique_data_df)

    # show data in map
    data_visualization_with_map(unique_data_df)




# program execution starts from here
if __name__ == '__main__':
    print("\nWelcome to Unemployment Analysis With Python\n")
    unemployment_analysis_function()
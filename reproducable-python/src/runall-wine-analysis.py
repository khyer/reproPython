import importlib
import recipy

subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

starting_file = 'data/raw/winemag-data-130k-v2.csv'
country = 'Chile'

if __name__ == '__main__':
    print(f'Raw data file {starting_file}')
    subset_file = subset.process_data_GBP(starting_file)
    print(f'Subset file {subset_file}')      
    plotwines.create_plots(subset_file)
    print(f'Creating them lovely plots')      
    country_sub_file = country_sub.get_country(subset_file, 'country')
    print(f'Country subset file for {country}: {country_sub_file}')      



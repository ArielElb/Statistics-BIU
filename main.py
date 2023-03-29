############################################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
data = pd.read_csv('Tomato.csv')


def build_plot(year):
    data2 = data[data['Date'].str.contains(year)]
    fixed_data = np.array_split(np.array(sorted(data2['Average'])), 10)
    price_ranges = [(i[0], i[-1]) for i in fixed_data]
    bar_edges = []
    bar_widths = []
    for i in range(10):
        min_price, max_price = price_ranges[i]
        bar_edges.append(min_price + (max_price - min_price) / 2)
        bar_widths.append(max_price - min_price)
    fig, ax = plt.subplots(1, 1, figsize=(19.2, 15))
    tomato_prices = data2['Average']
    relative_freq = [0.1 for _ in range(10)]
    for j in range(10):
        ax.bar(bar_edges[j], relative_freq[j], width=bar_widths[j], alpha=0.3, edgecolor='black')
        ax.bar(bar_edges[j], relative_freq[j], width=bar_widths[j], alpha=0.8, edgecolor='black',
               fill=False)
    #change the font size of the y axis
    ax.tick_params(axis='y', labelsize=15)
    ax.set_title(f"Tomato prices in {data2['Date'].iloc[0]}", fontsize=20)
    ax.set_xlabel("Tomato price range", fontsize=20)
    ax.set_ylabel("Relative frequency", fontsize=20)
    ax.set_xticks(bar_edges)
    ax.set_xticklabels([f"{price_ranges[j][0]:.1f}-{price_ranges[j][1]:.1f}" for j in range(10)],
                          rotation=45, ha='right',
                            fontsize=15)

    # print the maximum average price
    print(f"Maximum average price in {year}: {data2['Average'].max()}")
    # print the narrowest price range
    print(f"Narrowest price range in {year}: {min(bar_widths)}")
    #print the widest price range
    print(f"Widest price range in {year}: {max(bar_widths)}")

    # print the largest range of prices



build_plot('2014')
build_plot('2020')



plt.show()

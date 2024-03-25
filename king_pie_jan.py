import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

all_data = pd.read_csv('king_pie_all_data_feb.csv')
vouchers = pd.read_csv('king_pie_vouchers_dec.csv')
chip_v = pd.read_excel('King Pie Loyalty - Chip Vouchers.xlsx')
coke_v = pd.read_excel('King Pie Loyalty - Coke Vouchers.xlsx')

chip_v['Cell_Number'] = chip_v['Cell Number']
chip_v['code'] = chip_v['Voucher']
coke_v['Cell_Number'] = coke_v['Cell Number']
coke_v['code'] = coke_v['Voucher']

# Merge dataframes on voucher code
chips_df = pd.merge(vouchers, chip_v, on='code', how='inner')
chips_redeemed_df = chips_df[['Cell_Number']]
coke_df = pd.merge(vouchers, coke_v, on='code', how='inner')
coke_redeemed_df = coke_df[['Cell_Number']]



# Merge dataframes on user_id
chips_df = pd.merge(all_data, chips_redeemed_df, on='Cell_Number', how='inner')
chips_customer_tracker_df = chips_df[['Cell_Number', 'item_description', 'item_description2', 'item_description3', 'item_description4', 'item_description5', 'item_description6']]
coke_df = pd.merge(all_data, coke_redeemed_df, on='Cell_Number', how='inner')
coke_customer_tracker_df = coke_df[['Cell_Number', 'item_description', 'item_description2', 'item_description3', 'item_description4', 'item_description5', 'item_description6']]

# Counting occurrences of each user_id
chips_user_counts = chips_customer_tracker_df['Cell_Number'].value_counts().head(10)
all_chips_user_counts = chips_customer_tracker_df['Cell_Number'].value_counts()
coke_user_counts = coke_customer_tracker_df['Cell_Number'].value_counts().head(10)
all_coke_user_counts = coke_customer_tracker_df['Cell_Number'].value_counts()

#hips_customer_tracker_df['Cell_Number'] = chips_customer_tracker_df['Cell_Number'].astype(str)
#coke_customer_tracker_df['Cell_Number'] = coke_customer_tracker_df['Cell_Number'].astype(str)

# Function to filter and count items
def chips_count_items(df):
    # Filter rows based on multiple conditions for each item column
    filtered_df = chips_customer_tracker_df[((chips_customer_tracker_df['item_description'].str.contains('Meal')) & (chips_customer_tracker_df['item_description'] != 'Super Saver Meal Buddy')) |
                 ((chips_customer_tracker_df['item_description2'].str.contains('Meal')) & (chips_customer_tracker_df['item_description2'] != 'Super Saver Meal Buddy')) |
                 ((chips_customer_tracker_df['item_description3'].str.contains('Meal')) & (chips_customer_tracker_df['item_description3'] != 'Super Saver Meal Buddy')) |
                 ((chips_customer_tracker_df['item_description4'].str.contains('Meal')) & (chips_customer_tracker_df['item_description4'] != 'Super Saver Meal Buddy')) |
                 ((chips_customer_tracker_df['item_description5'].str.contains('Meal')) & (chips_customer_tracker_df['item_description5'] != 'Super Saver Meal Buddy')) |
                 ((chips_customer_tracker_df['item_description6'].str.contains('Meal')) & (chips_customer_tracker_df['item_description6'] != 'Super Saver Meal Buddy')) |
                 (chips_customer_tracker_df['item_description'] == 'Burger Pie + Chips') | (chips_customer_tracker_df['item_description2'] == 'Burger Pie + Chips') | (chips_customer_tracker_df['item_description3'] == 'Burger Pie + Chips') |
                 (chips_customer_tracker_df['item_description4'] == 'Burger Pie + Chips') | (chips_customer_tracker_df['item_description5'] == 'Super Saver Meal Buddy') | (chips_customer_tracker_df['item_description6'] == 'Burger Pie + Chips')]

    # Count total items
    total_items = len(filtered_df)
    
    # Count breakfast
    #breakfast_count = chips_customer_tracker_df[chips_customer_tracker_df.apply(lambda row: 'Super Saver Meal Buddy' in row.values, axis=1)].shape[0]
    # Count breakfast
    chips_only_df = chips_customer_tracker_df[chips_customer_tracker_df.apply(lambda row: 'Super Saver Meal Buddy' in row.values, axis=1)]
    chips_only_count = chips_only_df.shape[0]
    #chips_only_count['Cell_Number'] = chips_only_count['Cell_Number'].astype(str)
    chips_only_unique_persons = chips_only_df['Cell_Number'].unique()

    return filtered_df['Cell_Number'].unique(), total_items, chips_only_count, chips_only_unique_persons

    #return filtered_df['Cell_Number'].unique(), total_items, breakfast_count
def coke_count_items(df):
    # Filter rows based on multiple conditions for each item column
    coke_filtered_df = coke_customer_tracker_df[((coke_customer_tracker_df['item_description'].str.contains('Meal')) & (coke_customer_tracker_df['item_description'] != 'Super Saver Meal Buddy')) |
                 ((coke_customer_tracker_df['item_description2'].str.contains('Meal')) & (coke_customer_tracker_df['item_description2'] != 'Super Saver Meal Buddy')) |
                 ((coke_customer_tracker_df['item_description3'].str.contains('Meal')) & (coke_customer_tracker_df['item_description3'] != 'Super Saver Meal Buddy')) |
                 ((coke_customer_tracker_df['item_description4'].str.contains('Meal')) & (coke_customer_tracker_df['item_description4'] != 'Super Saver Meal Buddy')) |
                 ((coke_customer_tracker_df['item_description5'].str.contains('Meal')) & (coke_customer_tracker_df['item_description5'] != 'Super Saver Meal Buddy')) |
                 ((coke_customer_tracker_df['item_description6'].str.contains('Meal')) & (coke_customer_tracker_df['item_description6'] != 'Super Saver Meal Buddy')) |
                 (coke_customer_tracker_df['item_description'] == 'Burger Pie + Chips') | (coke_customer_tracker_df['item_description2'] == 'Burger Pie + Chips') | (coke_customer_tracker_df['item_description3'] == 'Burger Pie + Chips') |
                 (coke_customer_tracker_df['item_description4'] == 'Burger Pie + Chips') | (coke_customer_tracker_df['item_description5'] == 'Super Saver Meal Buddy') | (coke_customer_tracker_df['item_description6'] == 'Burger Pie + Chips')]

    # Count total items
    total_coke_items = len(coke_filtered_df)
    
    # Count breakfast
    #coke_only_count = chips_customer_tracker_df[chips_customer_tracker_df.apply(lambda row: 'Super Saver Meal Buddy' in row.values, axis=1)].shape[0]
    # Count breakfast
    coke_only_df = coke_customer_tracker_df[coke_customer_tracker_df.apply(lambda row: 'Super Saver Meal Buddy' in row.values, axis=1)]
    coke_only_count = coke_only_df.shape[0]
    coke_only_unique_persons = coke_only_df['Cell_Number'].unique()
    return coke_filtered_df['Cell_Number'].unique(), total_coke_items, coke_only_count, coke_only_unique_persons

st.title('King Pie Analysis on the Chips and Coke Vouchers For February')

tab1, tab2 = st.tabs(["People who got Chips Vouchers", "People who got Coke Vouchers"])

with tab1:
    unique_persons, total_items, breakfast_count, breakfast_unique_persons = chips_count_items(chips_customer_tracker_df)
    st.write("Total count of Meal items (excluding 'Super Saver Meal Buddy'): ", total_items)
    # Download button for unique persons
    if st.button('Download Unique Persons(CHIPS)'):
        unique_persons_df = pd.DataFrame(unique_persons, columns=['Unique Persons'])
        csv = unique_persons_df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name='unique_persons.csv', mime='text/csv')

    st.write("Total of Super Saver Meal Buddy: ", breakfast_count)

    # Download button for unique persons associated with breakfast count
    if st.button('Download Unique Persons (Super Saver Meal Buddy)(CHIPS)'):
        breakfast_unique_persons_df = pd.DataFrame(breakfast_unique_persons, columns=['Unique Persons (Breakfast Count)'])
        csv = breakfast_unique_persons_df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name='super_saver_mealt_unique_persons.csv', mime='text/csv')

    # Visualize top 10 users' purchases from chips
    fig, ax = plt.subplots()
    bars = ax.bar(chips_user_counts.index.astype(str), chips_user_counts.values)
    # Add numbers on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    ax.set_xlabel('User ID')
    ax.set_ylabel('Purchase Count')
    ax.set_title('Top 10 Users Purchases From Chips Voucher')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Display top 10 users' purchases table
    st.subheader("Top 10 Users' Purchases(From Chips Voucher):")
    st.write(chips_customer_tracker_df[chips_customer_tracker_df['Cell_Number'].isin(chips_user_counts.index)].reset_index(drop=True))

    # Display all users' purchases table
    st.subheader("All Users' Purchases(From Chips Voucher):")
    chips_all = chips_customer_tracker_df[chips_customer_tracker_df['Cell_Number'].isin(all_chips_user_counts.index)].reset_index(drop=True)
    st.write(chips_all)
    # Download button for top 10 users' purchases table
    csv_data = chips_all.to_csv(index=False).encode()
    st.download_button(label="Download All Chips Purchases CSV", data=csv_data, file_name='chips_all_data.csv', mime='text/csv')
    

with tab2:
    unique_persons_coke, total_coke_items, coke_only_count, coke_only_unique_persons = coke_count_items(coke_customer_tracker_df)
    st.write("Total count of Meal items (excluding 'Super Saver Meal Buddy'): ", total_coke_items)
    # Download button for unique persons
    if st.button('Download Unique Persons(COKE)'):
        unique_persons_coke_df = pd.DataFrame(unique_persons_coke, columns=['Unique Persons'])
        csv = unique_persons_coke_df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name='unique_persons.csv', mime='text/csv')

    st.write("Total of Super Saver Meal Buddy: ", coke_only_count)

    # Download button for unique persons associated with breakfast count
    if st.button('Download Unique Persons (Super Saver Meal Buddy)(COKE)'):
        breakfast_unique_persons_df = pd.DataFrame(coke_only_unique_persons, columns=['Unique Persons (Breakfast Count)'])
        csv = breakfast_unique_persons_df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name='super_saver_mealt_unique_persons.csv', mime='text/csv')

    # Visualize top 10 users' purchases from coke
    fig, ax = plt.subplots()
    bars = ax.bar(coke_user_counts.index.astype(str), coke_user_counts.values)
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Purchase Count')
    ax.set_title('Top 10 Users Purchases From Coke Voucher')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Display top 10 users' purchases table
    st.subheader("Top 10 Users' Purchases(From Coke Voucher):")
    st.write(coke_customer_tracker_df[coke_customer_tracker_df['Cell_Number'].isin(coke_user_counts.index)].reset_index(drop=True))

    # Display all users' purchases table
    st.subheader("All Users' Purchases(From Coke Voucher):")
    coke_all = coke_customer_tracker_df[coke_customer_tracker_df['Cell_Number'].isin(all_coke_user_counts.index)].reset_index(drop=True)
    st.write(coke_all)
    # Download button for top 10 users' purchases table
    csv_data = coke_all.to_csv(index=False).encode()
    st.download_button(label="Download All Coke Purchases CSV", data=csv_data, file_name='coke_all_data.csv', mime='text/csv')
    

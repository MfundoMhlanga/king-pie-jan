import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

all_data = pd.read_csv('king_pie_all_jan.csv')
chip_v = pd.read_excel('King Pie Loyalty - Chip Vouchers.xlsx')
coke_v = pd.read_excel('King Pie Loyalty - Coke Vouchers.xlsx')

chip_v['Cell_Number'] = chip_v['Cell Number']
coke_v['Cell_Number'] = coke_v['Cell Number']

# Merge dataframes on user_id
chips_df = pd.merge(all_data, chip_v, on='Cell_Number', how='inner')
chips_customer_tracker_df = chips_df[['Cell_Number', 'item_description', 'item_description2', 'item_description3', 'item_description4', 'item_description5', 'item_description6']]
coke_df = pd.merge(all_data, coke_v, on='Cell_Number', how='inner')
coke_customer_tracker_df = coke_df[['Cell_Number', 'item_description', 'item_description2', 'item_description3', 'item_description4', 'item_description5', 'item_description6']]

# Counting occurrences of each user_id
chips_user_counts = chips_customer_tracker_df['Cell_Number'].value_counts().head(10)
all_chips_user_counts = chips_customer_tracker_df['Cell_Number'].value_counts()
coke_user_counts = coke_customer_tracker_df['Cell_Number'].value_counts().head(10)
all_coke_user_counts = coke_customer_tracker_df['Cell_Number'].value_counts()



st.title('King Pie Analysis on the Chips and Coke Vouchers')

tab1, tab2 = st.tabs(["Chips", "Coke"])
with tab1:
   # Visualize top 10 users' purchases from chips
    fig, ax = plt.subplots()
    ax.bar(chips_user_counts.index.astype(str), chips_user_counts.values)
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
    st.write(chips_customer_tracker_df[chips_customer_tracker_df['Cell_Number'].isin(all_chips_user_counts.index)].reset_index(drop=True))


with tab2:
   # Visualize top 10 users' purchases from coke
    fig, ax = plt.subplots()
    ax.bar(coke_user_counts.index.astype(str), coke_user_counts.values)
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
    st.write(coke_customer_tracker_df[coke_customer_tracker_df['Cell_Number'].isin(all_coke_user_counts.index)].reset_index(drop=True))



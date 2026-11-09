import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💸",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}
.block-container {
    padding-top: 2rem;
}
[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e8edf5;
}
</style>
""", unsafe_allow_html=True)


# Session State
if "expenses" not in st.session_state:
    st.session_state.expenses = []

expenses = st.session_state.expenses


# Header
st.title("💸 Expense Tracker")
st.caption("Manage and monitor your daily expenses.")


# Calculate Summary
total = sum(e["amount"] for e in expenses)
count = len(expenses)
average = total / count if count else 0


# Dashboard Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Expenses", f"₹{total:,.2f}")
col2.metric("Number of Expenses", count)
col3.metric("Average Expense", f"₹{average:,.2f}")

st.divider()


# Main Layout
left, right = st.columns([1, 1.5])


# ADD EXPENSE
with left:

    st.subheader("➕ Add Expense")

    with st.form("add_expense", clear_on_submit=True):

        item = st.text_input("Expense Name")

        amount = st.number_input(
            "Amount (₹)",
            min_value=0.01,
            step=10.0
        )

        submit = st.form_submit_button(
            "Add Expense",
            use_container_width=True
        )

        if submit:

            if not item.strip():
                st.error("Enter expense name")

            else:
                new_id = max(
                    [e["id"] for e in expenses],
                    default=0
                ) + 1

                expenses.append({
                    "id": new_id,
                    "name": item.strip(),
                    "amount": amount
                })

                st.success("Expense added successfully!")
                st.rerun()


    # DELETE EXPENSE
    st.subheader("🗑️ Delete Expense")

    if expenses:

        selected = st.selectbox(
            "Select Expense",
            options=[e["id"] for e in expenses],
            format_func=lambda x: next(
                f'{e["name"]} - ₹{e["amount"]}'
                for e in expenses if e["id"] == x
            )
        )

        if st.button("Delete Expense", use_container_width=True):

            st.session_state.expenses = [
                e for e in expenses
                if e["id"] != selected
            ]

            st.success("Expense deleted!")
            st.rerun()

    else:
        st.info("No expenses available")


# VIEW EXPENSES
with right:

    st.subheader("📋 Your Expenses")

    if expenses:

        df = pd.DataFrame([
            {
                "Expense": e["name"],
                "Amount (₹)": e["amount"]
            }
            for e in expenses
        ])

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No expenses added yet")


    # MAX AND MIN EXPENSE
    st.subheader("📊 Expense Insights")

    if expenses:

        highest = max(
            expenses,
            key=lambda x: x["amount"]
        )

        lowest = min(
            expenses,
            key=lambda x: x["amount"]
        )

        c1, c2 = st.columns(2)

        c1.metric(
            "Highest Expense",
            f'₹{highest["amount"]:,.2f}'
        )
        c1.caption(highest["name"])

        c2.metric(
            "Lowest Expense",
            f'₹{lowest["amount"]:,.2f}'
        )
        c2.caption(lowest["name"])


        # CHART
        st.subheader("Spending Chart")

        chart_df = pd.DataFrame([
            {
                "Expense": e["name"],
                "Amount": e["amount"]
            }
            for e in expenses
        ])

        st.bar_chart(
            chart_df.set_index("Expense")
        )


# EXPORT AND CLEAR
if expenses:

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        csv = pd.DataFrame([
            {
                "Expense": e["name"],
                "Amount": e["amount"]
            }
            for e in expenses
        ]).to_csv(index=False)

        st.download_button(
            "⬇️ Export CSV",
            csv,
            file_name="expenses.csv",
            mime="text/csv",
            use_container_width=True
        )

    with c2:

        if st.button(
            "Clear All Expenses",
            use_container_width=True
        ):

            st.session_state.expenses = []
            st.rerun()


st.caption("Expense Tracker | Built with Python and Streamlit")